#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define sz size()

typedef long long i64;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int Max = 128;

int N;
int data[Max][Max];

inline int sgn(int x) { if (x == 0) return 0; if (x < 0) return -1; else return +1; }

bitset<Max> is_confl[Max], new_confl[Max];
int max_clique;
int iter;

void clique(int first, bitset<Max> adj, int cnt = 0)
{
	if (max_clique < cnt)
		max_clique = cnt;

	iter++;
	if (iter > 100000)
		return;

	FOR(i, first, N)
		if (adj[i])
			clique(i+1, adj & is_confl[i], cnt+1);			
}

int solve()
{
	int K;
	scanf("%d %d", &N, &K);
	REP(i, N) REP(j, K)
		scanf("%d", &data[i][j]);

	REP(i, N) {
		is_confl[i].reset();
		REP(j, N) {
			int exp_sgn = sgn(data[i][0]-data[j][0]);
			if (exp_sgn != 0) {
				REP(k, K)
					if (exp_sgn != sgn(data[i][k]-data[j][k]))
						is_confl[i].set(j);	
			} else
				is_confl[i].set(j);				
		}
	}

	max_clique = 0;
	REP(i, 50) {
		vector<int> vvv(N);
		REP(k, N)
			vvv[k] = k;
		random_shuffle(ALL(vvv));

		REP(x,N) REP(y,N)
			new_confl[vvv[x]].set(vvv[y], is_confl[x][y]);

		REP(k, N)
			is_confl[k] = new_confl[k];

		iter = 0;
		clique(0, bitset<Max>().set());
	}
	return max_clique;
}

int main()
{
	//freopen("C-large.in", "r", stdin);

	int n_test;
	scanf("%d\n", &n_test);
	REP(i_test, n_test)
		printf("Case #%d: %d\n", i_test+1, solve());

	return 0;
}
