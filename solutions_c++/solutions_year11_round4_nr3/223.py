#ifndef LOCAL_BOBER
#pragma comment(linker, "/STACK:134217728")
#endif

#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <stack>
#include <sstream>
#include <cstring>
#include <numeric>
#include <ctime>

#define re return
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int) (x).size())
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rrep(i, n) for (int i = (n) - 1; i >= 0; i--)
#define y0 y32479
#define y1 y95874
#define fill(x, y) memset(x, y, sizeof(x))
#define sqr(x) ((x) * (x))
#define prev prev239
#define next next239
#define hash hash239
#define rank rank239
#define sqrt(x) sqrt(abs(x))

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef long long ll;
typedef double D;
typedef long double LD;

template<class T> T abs(T x) {return x > 0 ? x : -x;}

int n;
int m;

int d[2100001];
ll pr[2100001];
int pcol = 0;

void calc(int n) {
	for (int i = 2; i * i <= n; i++)
		if (d[i] == 0)
			for (int j = i * i; j <= n; j += i)
				d[j] = 1;
	for (int i = 2; i <= n; i++)
		if (d[i] == 0)
			pr[pcol++] = i;
}

int main() {
#ifdef LOCAL_BOBER
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	calc(1100000);
	int tc;
	cin >> tc;
	rep(tt, tc) {
		printf("Case #%d: ", tt + 1);

		ll n;
		cin >> n;

		if (n == 1) {
			cout << 0 << endl;
			continue;
		}

		ll ans = 0;
		rep(i, pcol) {
			if (n < pr[i] * pr[i])
				break;
			ans--;
			ll t = pr[i];
			while (t <= n) {
				ans++;
				t *= pr[i];
			}
		}

		cout << ans + 1 << endl;
	}

	re 0;
}

