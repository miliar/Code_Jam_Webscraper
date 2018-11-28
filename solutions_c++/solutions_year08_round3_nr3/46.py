#include <cstdio>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define TREE_SIZE (1<<20)
#define MAXN 500000
#define MAXM 100
#define MOD 1000000007

int tree[TREE_SIZE], h[MAXN], res;
int dp[MAXN];
int n, gen[MAXM];
vector<int> cords;

void init() {
    int m, x, y, z;
    res = 0;
    memset(tree, 0, sizeof(tree));
    cords.clear();
    scanf("%d %d %d %d %d", &n, &m, &x, &y, &z);
    for(int i=0; i<m; i++) {
        scanf("%d", &gen[i]);
    }
    for(int i=0; i<n; i++) {
        h[i] = gen[i%m];
        gen[i%m] = ((long long)x * gen[i%m] + (long long)y * (i + 1))%z;
    }
}

void update(int i, int val) {
    int cur=i+MAXN;
    while(cur>0) {
        tree[cur] += val;
        tree[cur] %= MOD;
        cur/=2;
    }
}

int calc_dp(int i) {
    int res=0, cur=i+MAXN;
    while(cur>0) {
        if(cur%2 == 1) {
            res += tree[cur-1];
            res %= MOD;
        }
        cur/=2;
    }
    return res;
}

void solve() {
    cords.resize(n);
    for(int i=0; i<n; i++) {
        cords[i] = h[i];
    }
    sort(cords.begin(), cords.end());
    cords.erase(unique(cords.begin(), cords.end()), cords.end());

    for(int i=0; i<n; i++) {
        int pos = lower_bound(cords.begin(), cords.end(), h[i]) - cords.begin();
        dp[i] = (calc_dp(pos) + 1)%MOD;
        res += dp[i];
        res %= MOD;
        update(pos, dp[i]);
    }
}

int main(void) {
	int n;

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C.out", "w", stdout);

	cin >> n;
	for(int i=1; i<=n; ++i) {
		init();
		solve();
		cout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}
