#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
using namespace std; 

#define REP(i,n) for(int i=0;i<(n);++i) 
#define FOR(i,a,b) for(int i=(a);i<=(b);++i) 
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i) 
#define FOREACH(it,c) for(typeof((c).begin())it=(c).begin();it!=(c).end();++it) 
#define CLR(x) memset((x),0,sizeof((x))) 
typedef long long LL; 
typedef vector<int> VI; 
typedef vector<string> VS; 

#define INF 2000000000

char mat[10][10];
int height, width;
LL mm[10][1 << 10];

LL dp(int row, int state) {
	if (row == -1) return 0;

	if (row == 9) {
		int adai = 0;
	}
	
	LL& res = mm[row][state];
	if (res != -1) return res;

	if (row == height) return res = 0;

	res = 0;
	int total = (1 << width);
	REP(s,total) {
		bool flag = true;
		REP(i,width) {
			if ((s & (1 << i)) && ((state & (1 << i)) || (mat[row][i] == 'x'))) {
				flag = false;
				break;
			}
		}
		REP(i,width-1) {
			if ((s & (1 << i)) && (s & (1 << (i + 1)))) {
				flag = false;
				break;
			}
		}
		if (!flag) continue;

		int ss = 0;
		int now = 0;
		REP(i,width) {
			if (s & (1 << i)) {
				++now;
				int a1 = i - 1, a2 = i + 1;
				if (a1 >= 0) {
					ss |= (1 << a1);
				}
				if (a2 < width) {
					ss |= (1 << a2);
				}
			}
		}
		LL t = dp(row - 1, ss);
		res = max(res, now + t);
	}
	return res;
}

void run() {
	cin >> height >> width;
	REP(i,height) {
		REP(j,width) {
			cin >> mat[i][j];
		}
	}

	memset(mm, -1, sizeof(mm));
	LL res = dp(height - 1, 0);
	cout << res << endl;
}

int main() {
	int kase;
	cin >> kase;
	REP(k,kase) {
		cout << "Case #" << k + 1 << ": ";
		run();
	}
	return 0;
}
