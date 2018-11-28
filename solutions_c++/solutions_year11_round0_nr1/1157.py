#include <cstdlib>
#include <iostream>

using namespace std;

int main() {

	int T;

	cin >> T;

	for (int t = 1; t <= T; ++t) {
	
		int n, time = 0;
		int orange = 1, blue = 1;

		char last_r = 'N';
		int interval = 0;

		cin >> n;

		for (int i = 0; i < n; ++i) {
			char r;
			int  p, inter, tmp;

			cin >> r >> p;
		
			if (r == 'O') {
				tmp = orange;
				orange = p;
			}
			else {
				tmp = blue;
				blue = p;
			}

			inter = abs(p-tmp) + 1;
			
			if (r == last_r) {
				time += inter;
				interval += inter;
			}
			else {
				if (inter <= interval) inter = 1;
				else inter -= interval;
				time += inter;
				interval = inter;
			}

			last_r = r;

		}

		cout << "Case #" << t << ": " << time << endl;

	}

}


