#include<cstdio>
#include<queue>
#include<algorithm>

using namespace std;

inline int modulo(int n) {
	return (n < 0 ? (-n) : n);
}

int total(queue<char> rob, queue<int> fir, queue<int> sec) {
	int res = 0;
	int tFir = -50, tSec = -50;	// the number of seconds acumulated from each robot since the other have acted
	int cFir = 1, cSec = 1;	// the current button that the robot is in front of

	while ( ! rob.empty() ) {
		char curr = rob.front();
		rob.pop();

		if (curr == 'O') {
			int but = fir.front();
			fir.pop();

			// the last one was it too
			if (tFir > 0) {
				tFir += modulo(cFir - but)+1;
				res += modulo(cFir - but)+1;
			}
			else {
				tFir = max( modulo(cFir - but)+1, tSec+1);
				res += max( modulo(cFir - but)+1, tSec+1);
				if (tSec > 0) {
					tFir -= tSec;
					res -= tSec;
				}
			}

			cFir = but;
			tSec = 0;
		}
		else {
			int but = sec.front();
			sec.pop();

			// the last one was it too
			if (tSec > 0) {
				tSec += modulo(cSec - but)+1;
				res += modulo(cSec - but)+1;
			}
			else {
				tSec = max( modulo(cSec - but)+1, tFir+1);
				res += max( modulo(cSec - but)+1, tFir+1);
				if (tFir > 0) {
					tSec -= tFir;
					res -= tFir;
				}
			}

			cSec = but;
			tFir = 0;
		}

/*
		printf("tFir = %d; tSec = %d\n", tFir, tSec);
		printf("cFir = %d; cSec = %d\n", cFir, cSec);
		printf("res = %d\n", res);
*/
	}
//	printf("\n");

	return res;
}

int main() {
	int T = 0;
	scanf("%d", &T);

	for (int caseNum = 1; caseNum <= T; caseNum++) {
		int n = 0;
		scanf("%d ", &n);

		queue<char> robots;
		queue<int> first, second;

		for (int i = 0; i < n; i++) {
			char x = '\0';
			int y = 0;
			scanf("%c %d ", &x, &y);

			robots.push(x);
			if (x == 'O') first.push(y);
			else second.push(y);
		}

		printf("Case #%d: %d\n", caseNum, total(robots, first, second));
	}

	return 0;
}
