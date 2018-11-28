#include <iostream>
#include <fstream>
#include <algorithm>
//#include <map>
//#include <string>
//#include <cmath>
#include <vector>

using namespace std;

int num_trials;

int googlers;
int surprise;
int best;

int score[100];

int main(int argc, const char* argv[])  {
    ofstream fout ("b.out");
    ifstream fin ("b.in");

	fin >> num_trials;

	for (int trial = 1; trial <= num_trials; trial++) {
		fin >> googlers >> surprise >> best;
		for (int i = 0; i < googlers; i++) {
			fin >> score[i];
		}
		
		int count = 0;
		int surprise_left = surprise;
		
		for (int i = googlers - 1; i >= 0; i--) {
			if (best == 0) {
				count++;
			} else if (best == 1) {
				if (score[i] >= 1) {
					count++;
				}
			} else { 
				if (score[i] >= 3 * best - 2) { // remember round down!
					count++;
				} else if (score[i] >= 3 * best - 4) {
					if (surprise_left <= 0) {
						// nothing!
					} else {
						count++;
						surprise_left--;
					}
				}
			}
		}
				 
		fout << "Case #" << trial << ": " << count << endl;
	}
	
}
