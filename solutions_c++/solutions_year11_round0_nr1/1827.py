#include <iostream>
#include <cstdio>
#include <queue>
#include <cmath>

namespace gcj {
	using namespace std;

	struct rebot {
		int passTime;
		int position;
	};

	queue<bool> all;
	queue<int> qo, qb;

	void solve () {
		int t, n, pos, time, tt;
		char rot;
		scanf("%d", &t);
		rebot o, b;

		for (int  i = 0; i < t; i ++) {
			while(qo.empty() == false)
				qo.pop();
			while(qb.empty() == false)
				qb.pop();

			o.passTime = b.passTime = 0;
			o.position = b.position = 1;
			time = 0;

			scanf("%d", &n);
			while (n --) {
				scanf(" %c %d", &rot, &pos);
				bool isO = (rot == 'O');
				all.push(isO);
				if (isO)
					qo.push(pos);
				else
					qb.push(pos);
			}

			while (all.size() > 0) {
				bool isO = all.front();
				all.pop();

				if(isO) {
					tt = max(0, abs(qo.front() - o.position) - o.passTime) + 1;
					time += tt;
					b.passTime += tt;
					o.position = qo.front();
					o.passTime = 0;
					qo.pop();
				} else {
					tt = max(0, abs(qb.front() - b.position) - b.passTime) + 1;
					time += tt;
					o.passTime += tt;
					b.position = qb.front();
					b.passTime = 0;
					qb.pop();
				}
			}

			printf("Case #%d: %d\n", i + 1, time);
		}
	}
}



int main () {

	freopen("d:/A-large.in", "r", stdin);
	freopen("d:/A-large.out", "w", stdout);

	gcj::solve();
	return 0;
}