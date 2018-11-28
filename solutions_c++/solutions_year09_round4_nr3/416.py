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

int table[150][50];
bool bol[150][150];
int n, k;

bool comp(int p, int q)
{
	if(table[p][0]==table[q][0])	return false;
	if(table[p][0] > table[q][0]) {
		FOR(i, 1, k-1) {
			if(table[p][i] <= table[q][i])	return false;
		}
		return true;
	}
	else {
		FOR(i, 1, k-1) {
			if(table[p][i] >= table[q][i])	return false;
		}
		return true;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	scanf("%d\n", &T);
	FOR(tc, 1, T) {
		printf("Case #%d: ", tc);

		scanf("%d %d", &n, &k);
		REP(i, n) REP(j, k) {
			scanf("%d", &table[i][j]);
		}
		CLR(bol, false);
		REP(i, n) {
			FOR(j, i+1, n) {
				bol[i][j] = !comp(i,j);
				bol[j][i] = bol[i][j];
			}
		}
		/*
		REP(i, n) {
			REP(j, n) {
				fprintf(stderr, "%d ", bol[i][j]);
			}
			fprintf(stderr, "\n");
		}*/

		int sol = 0;
		REP(i, TWO(n)) {
			VI cand;
			REP(j, n) {
				if(TWO(j) & i) {
					cand.pb(j);
				}
			}
			bool flag = true;
			REP(j, cand.size()) {
				int x = cand[j];
				REP(k, cand.size()) {
					int y = cand[k];
					if(x==y)	continue;
					if(!bol[x][y]) {
						flag = false;
						break;
					}
				}
				if(!flag)	break;
			}
			if(flag) {
				int here = 0;
				REP(j, n) {
					if(TWO(j) & i) {
						here++;
					}
				}
				sol = max(sol, here);
			}
		}


		printf("%d\n", sol);
		fprintf(stderr, "Case #%d Finished!\n", tc);
	}

	return 0;
}