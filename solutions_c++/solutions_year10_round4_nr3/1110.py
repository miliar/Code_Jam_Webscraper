#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
using namespace std;

#define CLR(a, x) memset(a, x, sizeof(a)) // x = 0|-1, true|false.
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<=(b); i++)
#define FORD(i, b, a) for(int i=(b); i>=(a); i--)
#define FORE(ty, it, data) for(ty::iterator it=data.begin(); it!=data.end(); it++)
#define ALL(x) (x).begin(),(x).end()
#define TWO(X) (1<<(X))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define EPS 1e-10
const double PI = acos(-1.0);

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef map<string, int> MSI;

template<typename T> string toString(const T &n) { ostringstream O; O<<n; return O.str(); }

////////////////////////////////////////////////////////////////////////////////////////////////////////

bool table[111][111];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d\n", &T);
	FOR(tc, 1, T) {
		printf("Case #%d: ", tc);

		CLR(table, false);
		int R, cnt(0);
		scanf("%d", &R);
		while(R--) {
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			FOR(x, x1, x2) FOR(y, y1, y2) {
				table[x][y] = true;
				cnt++;
			}
		}

		int work(0);
		while(true) {
			FORD(i, 110, 1) FORD(j, 110, 1) {
				if(table[i-1][j]&&table[i][j-1]) {
					if(table[i][j]==false) {
						table[i][j] = true;
						cnt++;
					}
				}
				if(!table[i-1][j]&&!table[i][j-1]) {
					if(table[i][j]==true) {
						table[i][j] = false;
						cnt--;
					}
				}
			}
			work++;
			int ccnt(0);
			FORD(i, 110, 1) FORD(j, 110, 1) {
				if(table[i][j]==true)	ccnt++;
			}
			if(ccnt==0)	break;
		}

		printf("%d\n", work);



		fprintf(stderr, "Case #%d Finished!\n", tc);
	}

	return 0;
}