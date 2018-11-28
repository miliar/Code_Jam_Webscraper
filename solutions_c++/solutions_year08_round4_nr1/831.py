#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;


#define MAXM 20000
#define INF 1000000000

int m, v;
int node[MAXM];
int gate[MAXM];
int changeable[MAXM];

bool is_leaf(int x) {
	return (x > (m-1)/2);
}

void init() {
	int g, c, l;
	scanf("%d%d", &m, &v);

	memset(gate, 0, sizeof(gate));
	memset(changeable, 0, sizeof(changeable));
	memset(node, 0, sizeof(node));

	for(int i=1; i<=(m-1)/2; ++i) { // Read the interior nodes.
		scanf("%d%d", &g, &c);
		gate[i] = g;
		changeable[i] = c;
	}

	for(int i=1; i<=(m+1)/2; ++i) { // Read the leaf nodes.
		scanf("%d", node + (m-1)/2 + i);		 
	}
}

inline int get_bool_res(int v1, int v2, int x) {
	return (gate[x]) ? (v1 && v2) : (v1 || v2);	
}

int dp[MAXM][2]; // INF -> Impossible, -1 -> Undefined.

int calc_dp(int x, int val) {
	int &res = dp[x][val];
	if(res != -1) return res;
    
	if(x > m) return res = 0;
	if(is_leaf(x)) {
		if(node[x] == val) return res = 0;
		else return res = INF;
	}
	else {
		// We want to make node[x] = val.

		res = INF;

		for(int flip = 0; flip <= 1; flip++)
		{
			if(flip == 1 && !changeable[x]) break;

			if(flip == 1) gate[x] = !gate[x];

			for(int v1=0; v1<=1; v1++)
				for(int v2=0; v2<=1; v2++)		
				{
					int curr_val = get_bool_res(v1, v2, x);
					if(curr_val != val) continue;

					int cnt1 = calc_dp(2*x, v1);
					int cnt2 = calc_dp(2*x+1, v2);
					if(cnt1 >= INF || cnt2 >= INF) continue;

					res = min(res, cnt1 + cnt2 + flip);
				}

			if(flip == 1) gate[x] = !gate[x];
		}
		
	}
	
	return res;
}

int solve() {
	memset(dp, -1, sizeof(dp));
	return calc_dp(1, v);
}

int main(void) {
	int n;
	freopen("A3-large.in", "r", stdin);
	freopen("A3-large.out", "w", stdout);

	scanf("%d", &n);
	for(int t=1; t<=n; t++) {
		init();
		int res = solve();
		if(res >= INF) printf("Case #%d: IMPOSSIBLE\n", t);
		else printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
