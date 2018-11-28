#include <iostream>
#include <vector>

#include <string>

using namespace std;

int pos[50], speed[50];
int select_flag[50];
double move_time[50][50];

int main()
{
	int C, N, K, B, T, i, j, j1;

	cin>>C;
	for (i = 0; i < C; i++) {
		cin>>N>>K>>B>>T;
		for (j = 0; j < N; j++) {
			cin>>pos[j];
			select_flag[j] = 0;
		}
		int could_finish = 0;
		for (j = 0; j < N; j++) {
			cin>>speed[j];
			if (speed[j] * T + pos[j] >= B) {
				select_flag[j] = 1;
				could_finish++;
			}
		}

		if (could_finish < K) {
			cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
			continue;
		}

		memset(move_time, 0, sizeof(move_time));

		int start_pos = 0;
		for (j = N-1; j >= 0; j--) {
			start_pos += select_flag[j];
			if (start_pos == K) {
				start_pos = j;
				break;
			}
		}
		
		for (j = start_pos; j < N; j++) {
			if (select_flag[j] == 0) {
				continue;
			}
			for (j1 = j+1; j1 < N; j1++) {
				if (select_flag[j1] == 1) {
					continue;
				}
				if ((B-pos[j]) * speed[j1] < (B-pos[j1]) * speed[j]) {
					move_time[j][j1] = (pos[j1] - pos[j]) / (speed[j] - speed[j1]);
				}
			}
		}

		int res = 0;
		vector<double> tmp;
		for (j1 = start_pos; j1 < N; j1++) {
			tmp.clear();
			for (j = start_pos; j < j1; j++) {
				if (move_time[j][j1] > 0.00000001) {
					tmp.push_back(move_time[j][j1]);
				}
			}
			if (tmp.size() > 0) {
				sort(tmp.begin(), tmp.end());
				vector<double>::iterator it;
				double last = 0;
				for (it = tmp.begin(); it != tmp.end(); it++) {
					if (*it - last > 0.00000001) {
						res++;
						last = *it;
					}
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	return 0;
}
