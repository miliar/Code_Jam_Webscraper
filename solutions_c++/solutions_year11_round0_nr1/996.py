/*
 *  File: BotTrust.cpp
 *  ------------------
 *
 *  Created by Elina Robeva on 5/6/11.
 *
 */

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <vector>
using namespace std;


int main() {
	freopen("/Users/erobeva/Downloads/A-large.in","r",stdin);
	freopen("/Users/erobeva/Downloads/AAAAAout.txt", "w", stdout);
	
	int T;
	cin >> T;
	for(int i =0 ; i < T; ++i) { 
		int N;
		cin >> N;
		vector <char> robots(N);
		vector <int> positions(N);
		vector <int> BluePositions(N+1);
		vector <int> OrangePositions(N+1);
		int steps = 0;
		int blue = 0;
		int orange = 0;
		for(int j = 0; j < N; ++j) {
			cin >> robots[j];
			cin >> positions[j];
			if(robots[j] == 'B') {
				BluePositions[blue++] = positions[j];
			} else {
				OrangePositions[orange++] = positions[j];
			}
		}
		BluePositions[blue] = -1;
		OrangePositions[orange] = -1;
		blue = 0;
		orange = 0;
		int blueCur = 1;
		int orangeCur = 1;
		for(int j = 0; j < N; ++j) {
			int turnDone = 0;
			while(turnDone == 0) {
				if (robots[j] == 'B') {
					if (blueCur < positions[j]) {
						blueCur++;
					} else if (blueCur > positions[j]) {
						blueCur--;
					} else {
						turnDone = 1;
						blue++;
					}
					if(OrangePositions[orange] != -1 && orangeCur < OrangePositions[orange]) {
						orangeCur++;
					} else if (OrangePositions[orange] != -1 && orangeCur > OrangePositions[orange]) {
						orangeCur--;
					}
				} else {
					if (orangeCur < positions[j]) {
						orangeCur++;
					} else if (orangeCur > positions[j]) {
						orangeCur--;
					} else {
						turnDone = 1;
						orange++;
					}
					if(BluePositions[blue] != -1 && blueCur < BluePositions[blue]) {
						blueCur++;
					} else if (BluePositions[blue] != -1 && blueCur > BluePositions[blue]) {
						blueCur--;
					}
				}
				steps++;
			}
		}	
		
		cout << "Case #" << i + 1 << ": " << steps << endl;
	}
	return 0;
}