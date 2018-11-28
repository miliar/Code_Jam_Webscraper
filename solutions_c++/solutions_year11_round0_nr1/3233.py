#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main() 
{
	int cases;
	cin >> cases;
	
	for (int i = 0; i < cases; ++i) {
		int buts;
		cin >> buts;
		
		vector< pair<bool, int> > seq;
		
		// O is 0, B is 1
		
		int pos[] = {1, 1};
//		int ind[] = {-1, -1};
		int time[] = {0, 0};
		
		int lastr = 0;
		for (int b = 0; b < buts; b++) {
		
			// setup
			char rob;
			int but, r;
			cin >> rob >> but;
			if (rob == 'O') {
				r = 0;
			} else {
				r = 1;
			}
			
			// calculation
			int d = abs(pos[r] - but); // distance to walk
//			cout << "distance to walk: " << d << endl;
			time[r] += d + 1; // we also need to push the button
//			cout << "time not considering other: " << time[r] << endl;
			time[r] = max(time[r], time[1-r]+1);
//			cout << "time considering other: " << time[r] << endl;

			// update position!
			pos[r] = but;
		}
		
		int ttime = max(time[0], time[1]);
		
		cout << "Case #" << i+1 << ": " << ttime << endl;

	}
		
}

