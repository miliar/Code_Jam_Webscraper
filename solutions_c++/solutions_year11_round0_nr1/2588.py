#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct JOB {
	int button;
	int num;
};

int main() {
	int T;
	cin >> T;

	for (int i = 0; i < T; i ++){
		char hall[100] = {0};
		JOB job[2][100];
		for (int i = 0; i < 2; i ++)
			for (int j = 0; j < 100; j ++)
				job[i][j].num = -1;

		int idx_robot[2] = {0};

		int N; // num of job
		cin >> N;
		for (int j = 0; j < N; j ++) {
			char robot;
			int button, r;
			cin >> robot >> button;
			
			if (robot == 'O') {
				r = 0;
			} else r = 1;

			job[r][idx_robot[r]].button = button;
			job[r][idx_robot[r]].num = j;
			idx_robot[r] ++;
		}

		// simulation
		int pos[2];
		pos[0] = pos[1] = 1;
		int result = 0;

		int now_idx[2] = {0};
		int now_job = 0;

		for (;now_job < N; result ++) {
			int f = 0;
			for (int i = 0; i < 2; i ++) {
				if (job[i][now_idx[i]].num == now_job && job[i][now_idx[i]].button == pos[i] && f == 0) {
					// push button!
					now_idx[i] ++;
					now_job ++;

					f = 1;
					
				} else {
					if (job[i][now_idx[i]].button < pos[i]) {
						// go left
						pos[i] --;
					} else if (job[i][now_idx[i]].button > pos[i]) {
						// go right
						pos[i] ++;
					} else {
						// wait
					}
				}
			}
		}

		cout << "Case #" << (i + 1) << ": " << result << endl;
	}

	return 0;
}