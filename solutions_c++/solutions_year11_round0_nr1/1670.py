#include <iostream>
#include <cstdlib>

using namespace std;

struct tuple {
	char player;
	int button;
};

const char * ob = "OB";

int main() {
	
	int num_case;
	cin >> num_case;
	
	for (int i = 0; i < num_case; i++) {
		int num_step;
		cin >> num_step;
		
		tuple* test = new tuple[num_step];
		
		for (int j = 0; j < num_step; j++) {
			cin >> test[j].player;
			cin >> test[j].button;
		}
		
		/* 0 for orange, 1 for blue */
		int cycles = 0;
		int cur[2] = {0, 0};
		bool has_task[2] = {false, false};
		int pos[2] = {1, 1};
		while (1) {
			/* assign current task */
			for (int j = 0; j < 2; j++) {
				if (!has_task[j]) {
					while ((cur[j] < num_step) && test[cur[j]].player != ob[j]) {
						cur[j]++;
					}
					if (cur[j] < num_step) {
						has_task[j] = true;
//						cout << "Task assigned: " << ob[j] << " " << cur[j] << "(" << test[cur[j]].button << ")" << endl;
					}
				}
			}
			
			if (has_task[0] || has_task[1]) {
				if (cur[0] < cur[1]) {
					/* orange move */
					int diff = abs(test[cur[0]].button - pos[0]) + 1;
					cycles += diff;
//					cout << "Move Orange: " << "from " << pos[0] << " by " << diff << " at " << cycles << endl;
					pos[0] = test[cur[0]].button;
					has_task[0] = false;
					cur[0]++;
					if (has_task[1]) {
						if (diff >= (abs(test[cur[1]].button - pos[1])) ) {
							pos[1] = test[cur[1]].button;
						} else {
							pos[1] = (test[cur[1]].button > pos[1]) ? (pos[1] += diff) : (pos[1] -= diff);
						}
//						cout << "Move Blue to " << pos[1] << endl;
					}
				} else if (cur[0] > cur[1]) {
					/* blue move */
					int diff = abs(test[cur[1]].button - pos[1]) + 1;
					cycles += diff;
//					cout << "Move Blue: " << "from " << pos[1] << " by " << diff << " at " << cycles << endl;
					pos[1] = test[cur[1]].button;
					has_task[1] = false;
					cur[1]++;
					if (has_task[0]) {
						if (diff >= (abs(test[cur[0]].button - pos[0])) ) {
							pos[0] = test[cur[0]].button;
						} else {
							pos[0] = (test[cur[0]].button > pos[0]) ? (pos[0] += diff) : (pos[0] -= diff);
						}
//						cout << "Move Orange to " << pos[0] << endl;
					}
				}
			} else {
				break;
			}
		}
		
		cout << "Case #" << i+1 << ": " << cycles << endl;
		
		delete[] test;
	}

	return 0;
}
