#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int T,N,p;
	char v;

	vector<char> turn;
	vector<int> pos;

	scanf("%d", &T);
	for (int var = 1; var <= T; ++var) {

		scanf("%d", &N);
		for (int k = 0; k < N; ++k) {
			cin>>v;
			turn.push_back(v);

			cin>>p;
			pos.push_back(p);
		}
		int opos = 1, bpos = 1;
		int time = 0,lag;
		int oevent = 0,bevent = 0;
		char ch = turn.front();
		do {
			ch = turn.front();
			if (ch == 'O') {
				if (oevent == time) {
					time += fabs(pos.front() - opos);
					time++;
					opos = pos.front();
					turn.erase(turn.begin());
					pos.erase(pos.begin());
					oevent = time;
				}
				else {
					lag = time - oevent;
					if (fabs(opos - pos.front()) <= lag) {
						opos = pos.front();
						turn.erase(turn.begin());
						pos.erase(pos.begin());
						time++;
					}
					else {
						if (pos.front() > opos + lag)
							opos += lag;
						else if (pos.front() < opos - lag)
							opos -= lag;
					}
					oevent = time;
				}
			}
			else {
				if (bevent == time) {
					time += fabs(pos.front() - bpos);
					time++;
					bpos = pos.front();
					turn.erase(turn.begin());
					pos.erase(pos.begin());
					bevent = time;
				}
				else {
					lag = time - bevent;
					if (fabs(bpos - pos.front()) <= lag) {
						bpos = pos.front();
						turn.erase(turn.begin());
						pos.erase(pos.begin());

						time++;
					}
					else {
						if (pos.front() > bpos + lag)
							bpos += lag;
						else if (pos.front() < bpos - lag)
							bpos -= lag;
					}
					bevent = time;
				}
			}
		}while(!turn.empty());
		printf("Case #%d: %d\n", var, time);
	}

	return 0;
}

