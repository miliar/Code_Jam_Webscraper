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


FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");

int di[4] = {-1, 0, 0, 1};
int dj[4] = {0, -1, 1, 0};
int rev[4] = {3, 2, 1, 0};

int table[100][100], dir[100][100];
char sol[100][100];

inline bool bound(int i, int j, int m, int n)
{
	return i>=0 && i<m && j>=0 && j<n;
}

int main()
{
	int T;
	fscanf(in, "%d\n", &T);
	FOR(tc, 1, T) {
		fprintf(out, "Case #%d:\n", tc);

		int m, n;
		fscanf(in, "%d %d", &m, &n);
		REP(i, m) REP(j, n) {
			fscanf(in, "%d", &table[i][j]);
		}
		
		REP(i, m) REP(j, n) {
			int cur = table[i][j], mem = 4;
			REP(k, 4) {
				int ii = i + di[k];
				int jj = j + dj[k];
				if(!bound(ii, jj, m, n))	continue;
				if(table[ii][jj] < cur) {
					cur = table[ii][jj];
					mem = k;
				}
			}
			dir[i][j] = mem;
		}

		char chr = 'a';
		CLR(sol, 0);
		REP(i, m) REP(j, n) {
			if(sol[i][j] != 0)	continue;
			//find sink
			int ii=i, jj=j;
			while(dir[ii][jj]!=4) {
				int dd = dir[ii][jj];
				ii += di[dd], jj += dj[dd];
			}

			//bfs
			queue<PII> Q;
			Q.push(mp(ii, jj));
			sol[ii][jj] = chr;
			while(!Q.empty()) {
				int ni = Q.front().X, nj = Q.front().Y;
				Q.pop();
				REP(k, 4) {
					int nni = ni+di[k], nnj = nj+dj[k];
					if(!bound(nni, nnj, m, n))	continue;
					if(sol[nni][nnj] != 0)	continue;
					if(dir[nni][nnj] == rev[k])	{
						sol[nni][nnj] = chr;	
						Q.push(mp(nni,nnj));
					}
				}
			}

			chr++;
		}

		REP(i, m) {
			REP(j, n) {
				fprintf(out, "%c%c", sol[i][j], (j!=n-1)?' ':'\n');
			}
		}
	}

	return 0;
}