#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define eps 1e-9
#define FOR(x, s, e) for(int x = (s); x < (e); ++x)
#define FORc(x, s, e, c) for(int x = (s); x < (e) && (c); ++x)
#define STEP(x, s, e, d) for(int x = (s); x < (e); x+=(d))
#define ROF(x, s, e) for(int x = (s); x >= (e); --x)
#define ROFc(x, s, e, c) for(int x = (s); x >= (e) && (c); --x)
#define vb vector<bool>
#define vi vector<int>
#define vii vector<pair<int, int> >
#define vs vector<string>
#define pb push_back
#define mp make_pair
#define ALL(X) X.begin(), X.end()
#define LL long long
#define pii pair<int, int>
#define x first
#define y second
#define gcd(x, y) __gcd((x), (y))
#define countbit(x) __builtin_popcount(x)

using namespace std;

bool adj[10][10], sol;
int val[10], N, C, ans[10];
vector<vi > shape;

void col(int v){
	if (v == N){
		int S = shape.size();
		sol = 1;
		FORc(i, 0, S, sol){
			bool seen[10] = {0};
			int cnt = 0;
			FOR(j, 0, shape[i].size()) {
				cnt += !seen[val[shape[i][j]]];
				seen[val[shape[i][j]]] = 1;
			}
			sol = cnt == C;
		}
		if (sol){
			FOR(i, 0, N) ans[i] = val[i];
		}
	}else FORc(i, 0, C, !sol) val[v] = i, col(v+1);
}

int main(int argc, char **argv){
	int T;
	cin >> T;
	FOR(Ca, 1, T+1){
		shape.clear();
		printf("Case #%d: ", Ca);
		int M;
		cin >> N >> M;
		memset(adj, 0, sizeof(adj));
		FOR(i, 0, N) adj[i][(i+1)%N] = adj[i][(i+N-1)%N] = 1;
		int U[M], V[M];
		FOR(i, 0, M) cin >> U[i], --U[i];
		FOR(i, 0, M) cin >> V[i], --V[i];
		FOR(i, 0, M) adj[U[i]][V[i]] = 1, adj[V[i]][U[i]] = 1;
		vi comp;
		FOR(i, 0, N) comp.pb(i);
		map<vi, bool> seen;
		do{
			vi seq;
			seq.pb(comp[0]);
			FOR(i, 1, N){
				if (!adj[seq[i-1]][comp[i]]) break;
				seq.pb(comp[i]);
				if (adj[comp[i]][seq[0]] && seq.size() > 2) break;
			}
			if (seq.size() < 3) continue;
			bool ok = 1;
			int Q = seq.size();
			FORc(i, 0, Q, ok)
				ok = adj[seq[i]][seq[(i+1)%Q]];
			FORc(i, 0, Q, ok)
				FORc(j, 0, Q, ok){
					if ((i+1)%Q != j && ((i+Q-1)%Q!= j))
						ok = !adj[seq[i]][seq[j]];
				}
			vi sseq = seq;
			sort(ALL(sseq));
			if (!ok || seen[sseq]) continue;
			seen[sseq] = 1;
			shape.pb(seq);
			//FOR(i, 0, Q) printf("%d-", seq[i]+1); puts("");
		}while (next_permutation(ALL(comp)));
		int res = 1;
		sol = 0;
		ROFc(i, N, 1, !sol){
			C = i;
			col(0);
			if (sol) res = i;
		}
		printf("%d\n", res);
		FOR(i, 0, N)printf("%d ", ans[i]+1); puts("");
	}
	return 0;
}
