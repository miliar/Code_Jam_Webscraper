#include <iostream>

using namespace std;

typedef long long Int64;

const int maxn = 1000;

int seq1[maxn], seq2[maxn];
int n;

void Solve() {
    cin >> n;
    int i;
    for (i = 0; i < n; i++)
	cin >> seq1[i];
    for (i = 0; i < n; i++)
	cin >> seq2[i];
    sort(seq1, seq1 + n);
    sort(seq2, seq2 + n);
    Int64 ans = 0;
    for (i = 0; i < n; i++)
	ans += (Int64)seq1[i] * seq2[n - 1 - i];
    cout << ans << endl;
}

int main() {
    int t, i;
    cin >> t;
    for (i = 0; i < t; i++) {
	cout << "Case #" << i + 1 << ": ";
	Solve();
    }
    return 0;
}
