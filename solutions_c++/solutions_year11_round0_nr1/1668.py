#include <iostream>
#include <sstream>
#include <utility>

using namespace std;
void main (int argc, char **argv){
	int test;
	cin >> test;
	

	for (int i = 0; i < test; i++){
		int n;
		cin >> n;

		pair <char, int> next_ins;
		pair <int, int> last_pos(0, 0);
		pair <int, int> last_step(0, 0);
		int cur_step = 0;

		for (int j = 0; j < n; j++){
			cin >> next_ins.first;
			cin >> next_ins.second;
			next_ins.second --;			// Solving on 0 base

			if (next_ins.first == 'B'){
				// Handle charachter B
				int shift = next_ins.second - last_pos.first;
				shift = (shift > 0) ? shift : (-1 * shift);

				int step = cur_step - last_step.first;
				if (step < shift){
					cur_step = last_step.first + shift;
				}
				cur_step ++;
				last_step.first = cur_step;
				last_pos.first = next_ins.second;
			}
			else{
				// Handle charachter O
				int shift = next_ins.second - last_pos.second;
				shift = (shift > 0) ? shift : (-1 * shift);

				int step = cur_step - last_step.second;
				if (step < shift){
					cur_step = last_step.second + shift;
				}
				cur_step++;
				last_step.second = cur_step;
				last_pos.second = next_ins.second;
			}
		}

		cout << "Case #" << i+1 << ": " << cur_step;
		if (i != test - 1){
			cout << endl;
		}
	}	
}
