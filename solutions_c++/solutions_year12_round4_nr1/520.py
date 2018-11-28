// tuan anh 
// hanoi tower

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <queue>

using namespace std;

#define PI acos(-1)
#define MP make_pair
#define PB push_back
#define VI vector <int>
#define PII pair <int, int>
#define LL long long
#define SET(v,i) memset(v, i, sizeef(v))
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)
#define FORN(i,a,b) for (int i = (a); i < (b); i++)
#define DOWN(i,a,b) for (int i = (a); i > (b); i--)
#define FIT(it,v) for (typeof((v.begin()))::iterator it = v.begin(); it != v.end(); it++)
#define FITD(it,v) for (typeof(v)::iterator it = v.rbegin(); it != v.rend(); it++)
#define FREOPEN freopen("hanoi.inp", "r", stdin); freopen("hanoi.out", "w", stdout)

#define maxn 10010

int n, D, d[maxn], l[maxn];
int f[maxn];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int ntest;
	cin >> ntest;
	FOR (test, 1, ntest) {
		cin >> n;
		FOR (i, 1, n) cin >> d[i] >> l[i];
		cin >> D;
		d[0] = 0;
		d[n + 1] = D;
		FOR (i, 1, n + 1) f[i] = n + 1;
		f[1] = 0;
		
		FOR (i, 1, n) {
			if (f[i] == n + 1) break;
			int L = min(d[i] - d[f[i]], l[i]);
			//cerr << L << endl;
			FOR (j, i + 1, n + 1)
				if (d[j] - d[i] > L ) break;
					else if (f[j] == n + 1) f[j] = i;
			if (f[n + 1] <= n) break;
			//cerr << f[i] << endl;
		}
		
		string res = "YES";
		if (f[n + 1] > n) res = "NO";
		cout << "Case #" << test << ": "<< res << endl;
	}
}
