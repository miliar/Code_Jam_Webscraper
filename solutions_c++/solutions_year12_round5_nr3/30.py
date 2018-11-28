#include <iostream>
#include <cstdio>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;

typedef pair<long long, long long> pii;

void solve() {
	long long M, F, N;
	cin >> M >> F >> N;
	vector<pii> a(N);
	
	for (int i = 0; i < N; i++)
		cin >> a[i].first >> a[i].second;

    sort(a.begin(), a.end());

	long long ans = 0;
	
	for (int d = 1; d * F <= M; d++) {
		long long R = M - d * F;
		
		long long days = 0;
        for (int i = 0; i < N; i++) if ((a[i].second + 1) * d > days) {
            long long buy = min(R / a[i].first, (a[i].second + 1) * d - days);
            days += buy;
            R -= a[i].first * buy;
        }
		
        ans = max(ans, days);
	}
	
    static int test;
    cout << "Case #" << ++test << ": ";
    cout << ans << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--)
        solve();
    return 0;
}
