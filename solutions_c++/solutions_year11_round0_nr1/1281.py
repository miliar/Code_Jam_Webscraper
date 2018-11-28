#include <iostream>
#include <vector>
#include <cmath>

struct datum {
	int id;
	int id_next;

	char botname;
	int pos;
};

using namespace std;

const int MAX = 256;

int my_sign(int n) {
	return (n>0)-(n<0);
}

int my_abs(int n) {
	return n*my_sign(n);
}

int main(void) {
	int T; cin >> T;

	for(int t = 0; t < T; ++t) {
		int work_prev[MAX];
		work_prev['O'] = work_prev['B'] = -1;

		int pos[MAX];
		pos['O'] = pos['B'] = 1;

		int work_next[MAX];
		work_next['O'] = work_next['B'] = -1;

		int N; cin >> N;
		vector<datum> data;
		for(int i = 0; i < N; ++i) {
			string ts; cin >> ts;
			int ti; cin >> ti;
			datum d;
			d.id = i;
			d.id_next = -1;
			d.botname = ts[0];
			d.pos = ti;

			if(work_next[d.botname] < 0) {
				work_next[d.botname] = d.id;
			}
			if(work_prev[d.botname] >= 0) {
				data[work_prev[d.botname]].id_next = d.id;
			}
			work_prev[d.botname] = d.id;

			data.push_back(d);
		}

		int soln = 0;
		for(int i = 0; i < N; ++i) {
			datum d = data[i];
			int time_move_push = 1+my_abs(pos[d.botname]-d.pos);
			pos[d.botname] = d.pos;
			work_next[d.botname] = d.id_next;

			char other = d.botname^'O'^'B';
			if(work_next[other] >= 0) {
				int pos_target = data[work_next[other]].pos;
				int time_warp = my_abs(pos[other]-pos_target);
				if(time_warp <= time_move_push) {
					pos[other] = pos_target;
				}
				else {
					pos[other]+=time_move_push*((pos[other]<pos_target)*2-1);
				}
			}
			soln += time_move_push;
		}
		cout << "Case #" << (t+1) << ": " << soln << endl;
	}
	return 0;
}
