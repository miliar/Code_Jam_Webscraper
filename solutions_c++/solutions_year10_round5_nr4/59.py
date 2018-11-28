#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <queue>
#include <sstream>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i = 0; i < n; i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define y0 y3487465
#define y1 y8687969

typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

template<class T> T abs(T x) {
	re x > 0 ? x : -x;
}

const int mod = 1000000007;

long long n;
int m, k, q[100];
char was2[5000][71][71];
int res2[5000][71][71];
char was[71][71][71];
int res[71][71][71];
int cnk[71][71];
int fact[71];

int go2 (int sum, int i, int j) {
	if (i == 0) return (sum == 0);
	if (sum < 0 || j < 1 || i > j) return 0;
	if (was2[i][j][sum]) return res2[i][j][sum];
	was2[i][j][sum] = 1;
	res2[i][j][sum] = (go2 (sum - j, i - 1, j - 1) + go2 (sum, i, j - 1)) % mod;
	return res2[i][j][sum];
}

int go (int i, int j, int r) {
	if (j == 0) {
		if (i == k && r == 0 || i == k - 1 && r == q[i]) return 1;
		return 0;
	}	
	if (i == k) return 0;
	if (was[i][j][r]) return res[i][j][r];
	int c = q[i] - r, mr = 0;
	if (c < 0) { c += m; mr++; }
	int cur = 0;
	for (int nr = 0; nr < j; nr++)
		for (int nj = 0; nj <= j; nj++) {
			long long tmp = (((long long)go (i + 1, nj, nr + mr) * go2 (nr * m + c, j, m - 1)) % mod * cnk[j][nj]) % mod * fact[j];
			cur = (cur + tmp) % mod;
		}
	for (int nr = 0; nr < j; nr++)
		for (int nj = 1; nj <= j; nj++) {
			long long tmp = ((((long long)go (i + 1, nj, nr + mr) * go2 (nr * m + c, j - 1, m - 1)) % mod * cnk[j - 1][nj - 1]) % mod * j) % mod * fact[j - 1];
			cur = (cur + tmp) % mod;
		}
	was[i][j][r] = 1;
	res[i][j][r] = cur;
	return cur;
}

int power (int a, int b) {
	int c = 1;
	while (b) {
		if (b & 1) c = ((long long)c * a) % mod;
		b /= 2;
		a = ((long long)a * a) % mod;
	}                                    
	return c;
}

int main() {
	for (int i = 0; i <= 70; i++)
		for (int j = 0; j <= i; j++)
			if (i == 0 || j % i == 0)
				cnk[i][j] = 1;
			else
				cnk[i][j] = (cnk[i - 1][j] + cnk[i - 1][j - 1]) % mod;
	int tt;
	scanf ("%d\n", &tt);
	for (int it = 0; it < tt; it++) {
		scanf ("%I64d %d", &n, &m);
		k = 0;
		while (n) {
			q[k++] = n % m;
			n /= m;
		}
		memset (was, 0, sizeof (was));
		memset (was2, 0, sizeof (was2));
		int ans = 0, cur = 1;
		fact[0] = 1;
		for (int i = 1; i <= m; i++) {
			cur = ((long long)cur * i) % mod;
			fact[i] = cur;
			ans = (ans + (long long)go (0, i, 0) * power (cur, mod - 2)) % mod;
		}
		printf ("Case #%d: %d\n", it + 1, ans);
		cerr << it + 1 << " done" << endl;
	}
	return 0;
}