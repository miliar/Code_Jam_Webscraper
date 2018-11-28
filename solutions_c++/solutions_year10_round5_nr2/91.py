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

int n;
int m;
int res[1000000];
int x[100];

int main() {
	int tt;
	scanf ("%d\n", &tt);
	for (int it = 0; it < tt; it++) {
		long long l;
	        scanf ("%I64d%d", &l, &n);
	        for (int i = 0; i < n; i++) scanf ("%d", &x[i]);
	        sort (x, x + n);
	        reverse (x, x + n);
	        long long s = 0;
	        for (int i = 1; i < n; i++) s += (long long)x[i] * (x[i - 1] - 1);
		memset (res, 0, sizeof (res));
		for (int i = 1; i <= s; i++) {
			res[i] = -1;
			for (int j = 1; j < n; j++)
				if (i - x[j] >= 0 && res[i - x[j]] != -1 && (res[i] == -1 || res[i] > res[i - x[j]] + 1))
					res[i] = res[i - x[j]] + 1;
		}
		long long ans = -1;
		long long cans = (l - s) / x[0];
		for (long long cur = l - cans * x[0]; cur >= 0; cur -= x[0], cans++)
			if (cur <= s && res[cur] != -1 && (ans == -1 || ans > cans + res[cur])) ans = cans + res[cur];
		if (ans == -1) printf ("Case #%d: IMPOSSIBLE\n", it + 1); else
		printf ("Case #%d: %I64d\n", it + 1, ans);
		cerr << it + 1 << " done" << endl;
	}
	return 0;
}