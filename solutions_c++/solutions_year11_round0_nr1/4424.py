/*#include <iostream>

using namespace std;

int main() {
	cout << "Start" << endl;
}
*/

#include <iostream>
#include <stdlib.h>
using namespace std;

int main ()
{
	int cases;
	cin >> cases;

	for ( int t = 1; t <= cases; t++) {
		int moves;
		cin >> moves;
		
		int o_pos = 1;
		int o_mov_time = 0;
		int b_pos = 1;
		int b_mov_time = 0;

		int time = 0;
		
		char bot_name;
		int button;

		for (int j = 0; j < moves; j++) {
			cin >> bot_name;
			cin >> button;
			
			int move_dist, move_time;
						
			if (bot_name == 'O') {
				move_dist = button - o_pos;
				move_time = abs(move_dist) - (time - o_mov_time);
				time += max(move_time, 0) + 1;
				o_pos = button;
				o_mov_time = time;
			} else {
				move_dist = abs(button - b_pos);
				move_time = move_dist - (time - b_mov_time);
				time += max(move_time, 0) + 1;
				b_pos = button;
				b_mov_time = time;
			}
			// cout << move_dist << " " << move_time << " "  << time << endl;
		}

		cout << "Case #" << t << ": " << time << endl;
	}


}
