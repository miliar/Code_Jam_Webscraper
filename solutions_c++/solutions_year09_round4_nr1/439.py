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

int table[50][50];
int tt[50];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	scanf("%d\n", &T);
	FOR(tc, 1, T) {
		printf("Case #%d: ", tc);

		int n;
		scanf("%d", &n);
		REP(i, n) REP(j, n) {
			scanf("%1d", &table[i][j]);
		}
		REP(i, n) {
			int cnt = 0;
			FORD(j, n-1, 0) {
				if(table[i][j]!=0)	break;
				cnt++;
			}
			tt[i] = n-cnt-1;
		}
		
		int sol = 0;
		REP(i, n) {
			if(tt[i] > i) {
				int mem = 0;
				FOR(j, i+1, n-1) {
					if(tt[j] <= i) {
						mem = j;
						break;
					}
				}
				FORD(j, mem, i+1) {
					swap(tt[j], tt[j-1]);
					sol++;
				}
			}
		}

		printf("%d\n", sol);
		fprintf(stderr, "Case #%d Finished!\n", tc);
	}

	return 0;
}