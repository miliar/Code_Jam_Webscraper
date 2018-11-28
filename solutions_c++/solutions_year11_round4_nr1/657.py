#include <iostream>
#include <fstream>
#include <algorithm>
//#include <map>
//#include <string>
//#include <cmath>
#include <vector>

using namespace std;

class Walkway {
public:
	int length;
	int speed;
};

bool operator< (Walkway w1, Walkway w2) {
	return w1.speed < w2.speed;
}

int num_trials;

int length;
int v_walk;
int v_run;
double run_time;
int num_walkways;


int main(int argc, const char* argv[])  {
    ofstream fout ("a.out");
    ifstream fin ("a.in");

	fin >> num_trials;
	
	for (int trial = 1; trial <= num_trials; trial++) {
		fin >> length >> v_walk >> v_run >> run_time >> num_walkways;

		vector<Walkway> walkways(num_walkways+1);
		
		int walkway_total_length = 0;
		for (int i = 0; i < num_walkways; i++) {
			//walkways[i] = new Walkway();
			int start, end, speed;
			fin >> start >> end >> speed;
			walkway_total_length += (end - start);
			walkways[i].length = end - start;
			walkways[i].speed = speed;
		}
		
		walkways[num_walkways].length = length - walkway_total_length;
		walkways[num_walkways].speed = 0;
		num_walkways++; // add fake one
		
		sort (walkways.begin(), walkways.end());
		
		bool can_still_run = true;
		double time_ran = 0;
		double total_time = 0;
		for (int i = 0; i < num_walkways; i++) { // go through walkways in order of speed
			if (can_still_run) {
				double next_run_time = (double) walkways[i].length / (walkways[i].speed + v_run);
				if (time_ran + next_run_time <= run_time) {
					// good! made it through this walkway;
					time_ran += next_run_time;
					total_time += next_run_time;
				} else {
					next_run_time = run_time - time_ran;
					double distance_ran = next_run_time * (walkways[i].speed + v_run);
					double distance_left = walkways[i].length - distance_ran;
					double walk_time = distance_left / (walkways[i].speed + v_walk);
					total_time += (next_run_time + walk_time);
					can_still_run = false;
				}
			} else {
				double walk_time = (double) walkways[i].length / (walkways[i].speed + v_walk);
				total_time += (walk_time);				
			}
		}
		
		cout.precision(10); 
		fout.precision(10); 
		cout << "Case #" << trial << ": " << total_time << endl;
		fout << "Case #" << trial << ": " << total_time << endl;
	}

}
