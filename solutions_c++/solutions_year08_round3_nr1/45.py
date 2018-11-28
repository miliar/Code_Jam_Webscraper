#include <cstdio>
#include <cstdlib>
#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;

int P, K, L;
long long res;
vector<int> let;

void init() {
    int temp;
    res = 0;
    let.clear();
    scanf("%d %d %d", &P, &K, &L);
    for(int i=0; i<L; ++i) {
        scanf("%d", &temp);
        let.push_back(temp);
    }
}

bool cmp(const int &a, const int &b) {
    return a > b;
}

void solve() {
    sort(let.begin(), let.end(), cmp);
    for(int i=0; i<L; ++i) {
        res += (1 + i / K) * let[i];
    }
}

int main(void) {
	int n;

	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);

	cin >> n;
	for(int i=1; i<=n; ++i) {
		init();
		solve();
		cout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}
