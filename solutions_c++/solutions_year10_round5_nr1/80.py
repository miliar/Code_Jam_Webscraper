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
int p[100000], pr[1000001], x[20];

int power (int a, int b, int p) {
	int c = 1;
	while (b) {
		if (b & 1) c = ((long long)c * a) % p;
		b /= 2;
		a = ((long long)a * a) % p;
	}
	return c;
}

int main() {
	memset (pr, 0, sizeof (pr));
	int r = 0;
	for (int i = 2; i <= 1000000; i++)
		if (!pr[i]) {
			p[r++] = i;
			if (i <= 1000000 / i) for (int j = i * i; j <= 1000000; j += i) pr[j] = 1;
		}
//	printf ("%d\n", r);
	int tt;
	scanf ("%d\n", &tt);
	for (int it = 0; it < tt; it++) {
		scanf ("%d%d", &n, &m);
		int base = 1;
		for (int i = 0; i < n; i++) base *= 10;
		for (int i = 0; i < m; i++) scanf ("%d", &x[i]);
		int mp = 0;
		for (int i = 0; i < m; i++) mp = max (mp, x[i]);
		if (m == 1) {
			printf ("Case #%d: I don't know.\n", it + 1);
		} else 
		if (m == 2) {
			set<int> all; all.clear ();
			for (int i = 0; i < r && all.size () < 2; i++)
				if (p[i] < base && p[i] > mp)
					for (int a = 0; a < p[i] && all.size () < 2; a++) {
						int b = ((long long)x[0] * a) % p[i];
						int ok = 1;
						for (int j = 0; j + 1 < m; j++)
							if (((long long)x[j] * a + b) % p[i] != x[j + 1]) {
								ok = 0;
								break;
							}	
						if (ok) all.insert (((long long)x[m - 1] * a + b) % p[i]);
					}
			if (all.size () == 1) printf ("Case #%d: %d\n", it + 1, *all.begin ()); else printf ("Case #%d: I don't know.\n", it + 1);
		} else {
			set<int> all; all.clear ();
			for (int i = 0; i < r; i++)
				if (p[i] > mp && p[i] < base) {
					int a = ((long long)((x[1] - x[2] + p[i]) % p[i]) * power ((x[0] - x[1] + p[i]) % p[i], p[i] - 2, p[i])) % p[i];
					int b = ((long long)x[0] * a) % p[i];
					b = (x[1] - b + p[i]) % p[i];
					int ok = 1;
					for (int j = 0; j + 1 < m; j++)
						if (((long long)x[j] * a + b) % p[i] != x[j + 1]) {
							ok = 0;
							break;
						}	
					if (ok) all.insert (((long long)x[m - 1] * a + b) % p[i]);
				}
			if (all.size () == 1) printf ("Case #%d: %d\n", it + 1, *all.begin ()); else printf ("Case #%d: I don't know.\n", it + 1);
		}
		cerr << it + 1 << " done" << endl;
	}
	return 0;
}