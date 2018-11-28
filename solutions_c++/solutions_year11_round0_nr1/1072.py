#include <iostream>
#include <fstream>
#include <algorithm>
//#include <map>
//#include <string>
//#include <cmath>
#include <vector>

using namespace std;

class Bot {
public:
	vector<int> goals;
	int goal_index;
	int position;
	
	Bot() {
		goal_index = 0;
		position = 1;
	}
	
	int distance_to_next() {
		if (goal_index >= goals.size()) { //i.e. done
			return 0; // no need to move
		} else {
			return abs(goals[goal_index] - position);
		}
	}
	
	void move_to_next_goal() {
		if (goal_index >= goals.size()) {
			// no need
		} else {
			position = goals[goal_index];
		}
	}
	
	void move_towards_next_goal(int time) { // time is constrained
		int distance = distance_to_next();
		if (distance <= time) {
			move_to_next_goal(); // made it:
		} else {
			if(position < goals[goal_index]) {
				position += time;
			} else {
				position -= time;
			}
		}
	}	
};

int main(int argc, const char* argv[])  {
    ofstream fout ("bottrust.out");
    ifstream fin ("bottrust.in");

	int num_trials;
	fin >> num_trials;
	
	for (int trial = 1; trial <= num_trials; trial++) {
		Bot bot[2]; // bot[0] = O, bot[1] = B
		
		int num_steps;
		fin >> num_steps;
		
		int* bot_order;
		bot_order = new int[num_steps];
		
		for (int i = 0; i < num_steps; i++) {
			char next_bot;
			int next_goal;
			fin >> next_bot >> next_goal;
			
			int next_bot_as_int;
			if (next_bot == 'O') {
				next_bot_as_int = 0;
			} else {
				next_bot_as_int = 1;
			}
			
			bot_order[i] = next_bot_as_int;
			bot[next_bot_as_int].goals.push_back(next_goal);
		}
		
		// DONE WITH INPUT
		
		int total_time = 0;
		for (int i = 0; i < num_steps; i++) {
			
			
			int focused_bot = bot_order[i];
			int not_focused_bot;
			if (focused_bot == 0) {
				not_focused_bot = 1;
			} else {
				not_focused_bot = 0;
			}
			
			// focused bot
			int time_to_move_and_press = bot[focused_bot].distance_to_next() + 1; // plus 1 for button pressing!
			bot[focused_bot].move_to_next_goal();
			bot[focused_bot].goal_index++;
			
			// not-focused bot
			bot[not_focused_bot].move_towards_next_goal(time_to_move_and_press);
			
			total_time += time_to_move_and_press;
		}
		fout << "Case #" << trial << ": " << total_time << endl;
		cout << "Case #" << trial << ": " << total_time << endl;
	}
	

}
