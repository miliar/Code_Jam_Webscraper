#include <iostream>

#define REP(i,n) for (int (i)=0; (i)<(n); (i)++)

using namespace std;

pair<int,int> ROBOTS[2];
int L;

int main(int argn, char *argv[])
{
	int T; cin >> T;
	
	REP(t,T) {
		int N; cin >> N;
		int lastPO = 1, lastPB = 1, lastO = 0, lastB = 0;
		ROBOTS[0].first = 1; ROBOTS[1].first = 1;
		ROBOTS[0].second = 0; ROBOTS[1].second = 0;
		L = 0;
		REP(n,N) {
			char R; int P; cin >> R >> P;
			pair<int,int> robot = (R=='B')?ROBOTS[0]:ROBOTS[1];
			L = max(abs(robot.first - P) + 1 + robot.second, L+1);
			robot.first = P; robot.second = L;
			if (R=='B') ROBOTS[0]=robot; else ROBOTS[1]=robot;
		}
		printf("Case #%d: %d\n", t+1, L);
	}
	return 0;
}