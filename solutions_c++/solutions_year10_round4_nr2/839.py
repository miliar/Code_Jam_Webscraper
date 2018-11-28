//{{{
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
//}}}

typedef long long LL;

const int MAX=3000;
int M[MAX];
int G[MAX][2];
vector<int> teams[MAX];

const LL INF = 1LL<<55;
LL dp[2055][1055][11];
int leaves;

LL go(int at, int t, int rem) {
	if (rem < 0) return INF;
	if (at < leaves) return 0;

	LL& ref = dp[at][t][rem];
	if (ref != -1) return ref;
	ref = 0;

	int lc = G[at][0];
	int rc = G[at][1];

	//printf("\tAT: %d LC: %d RC: %d\n", at, lc, rc);

	// In left subtree
	if (find(teams[lc].begin(),teams[lc].end(),t) != teams[lc].end()) {
		for (int j=0;j<teams[rc].size();++j) {
			const int opp = teams[rc][j];
			assert(opp != t);
			LL cur = INF;
			if (rem > 0 && M[opp] > 0) {
				cur = min(cur, go(lc, t, rem-1) + go(rc, opp, M[opp]-1));
			}

			cur = min(cur, M[at] + go(lc, t, rem) + go(rc, opp, M[opp]));

			ref = max(ref, cur);
		}
	}
	else {
		for (int j=0;j<teams[lc].size();++j) {
			const int opp = teams[lc][j];
			assert(opp != t);
			LL cur = INF;
			if (rem > 0 && M[opp] > 0) {
				cur = min(cur, go(rc, t, rem-1) + go(lc, opp, M[opp]-1));
			}

			cur = min(cur, M[at] + go(rc, t, rem) + go(lc, opp, M[opp]));

			ref = max(ref, cur);
		}
	}
	return ref;
}


int main() {
	int NCASES;
	cin >> NCASES;
	for (int z=1;z<=NCASES;++z) {
		int P;
		cin >> P;
		leaves = 1<<P;

		for (int i=0;i<2*leaves + 5;++i) {
			G[i][0] = G[i][1] = -1;
			teams[i].clear();
		}

		queue<int> q;
		for (int i=0;i<leaves;++i) {
			q.push(i);
			teams[i].push_back(i);
		}
		int cnt = leaves;
		for (int i=0;i<P+1;++i) {
			//printf("NEXT LEVEL %d\n", i);
			queue<int> nq;
			int prev = -1;
			while (!q.empty()) {
				int t = q.front(); q.pop();
				//printf("\tREAD FOR NODE %d WITH CH %d %d\n", t, G[t][0], G[t][1]);
				cin >> M[t];
				if (prev != -1) {
					nq.push(cnt);
					G[cnt][0] = t-1;
					G[cnt][1] = t;
					teams[cnt].clear();
					teams[cnt].insert(teams[cnt].end(), teams[t].begin(), teams[t].end());
					teams[cnt].insert(teams[cnt].end(), teams[t-1].begin(), teams[t-1].end());
					++cnt;
					prev = -1;
				}
				else {
					prev = t;
				}
			}
			q = nq;
		}


		for (int j=0;j<cnt;++j)
			for (int k=0;k<leaves;++k)
				for (int h=0;h<=P;++h)
					dp[j][k][h] = -1;

		const int root = cnt-1;
		LL ans = -1;
		for (int i=0;i<leaves;++i) {
			LL cur = go(root,i,M[i]);
			ans = max(ans, cur);
			//printf("IF TEAM %d WINS ==> %lld\n", i, cur);
		}
		assert(ans != -1);
		printf("Case #%d: %lld\n", z, ans);
	}
}
