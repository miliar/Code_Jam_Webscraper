#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

template <class T> T sqr (T x) {return x * x;}

int n, m;
int a[2000], b[2000];
vector <int> A[2000];
int ans[2000];
bool u[3000];

bool check (vector <int> tmp, int C) {
	int l = -1;
	int r = -1;
	int ds = inf;
	forn (i, tmp.size())
		forn (j, A[tmp[i]].size()) {
			vector <int> :: iterator it = lower_bound (all (tmp), A[tmp[i]][j]);
			if (it != tmp.end())
				if ((*it) == A[tmp[i]][j]) {
					l = i;
					r = it - tmp.begin();
					if (l+1 < r)
						ds = min (ds, r-l);
				}
		}
	l = r = -1;
	forn (i, tmp.size())
		if (l != -1) 
			break;
		else
			forn (j, A[tmp[i]].size()) {
				vector <int> :: iterator it = lower_bound (all (tmp), A[tmp[i]][j]);
				if (it != tmp.end())
					if ((*it) == A[tmp[i]][j]) {
						l = i;
						r = it - tmp.begin();
						if (l+1 >= r || (ds < r-l)) {
							l = -1;
							r = -1;
							continue;
						}
						break;
					}
			}
	if (l == -1) {
		if (I tmp.size() < C)
			return 0;
		int cur = 0;
		forn (i, tmp.size()) {
			if (cur < C)
				ans[tmp[i]] = cur ++;
			else {
				int c1 = ans[tmp[i-1]];
				int c2 = ans[tmp[(i+1)%tmp.size()]];
				if (c1 > c2)
					swap (c1, c2);
				if (c1 == 0 && c2 == 1)
					c1 = 2;
				else
				if (c1 == 0 || c2 == 0)
					c1 = 1;
				else
					c1 = 0;
				ans[tmp[i]] = c1;
			}
		}
		return 1;
	}
	if (r - l + 1 < C)
		return 0;
	vector <int> tmp1;
	forn (i, tmp.size())
		if (!(l < i && i < r))
			tmp1.pb (tmp[i]);
	if (!check (tmp1, C))
		return 0;
	seta (u, 0);
	for (int i = l; i <= r; i ++)
		if (ans[tmp[i]] != -1)
			u[ans[tmp[i]]] = 1;
	int cur = 0;
	for (int i = l; i <= r; i ++) {
		while (u[cur])
			cur ++;
		if (ans[tmp[i]] != -1)
			continue;
		if (cur < C)
			ans[tmp[i]] = cur ++;
		else {
			int c1 = ans[tmp[(i-1+tmp.size())%tmp.size()]];
			int c2 = ans[tmp[(i+1)%tmp.size()]];
			if (c1 > c2)
				swap (c1, c2);
			if (c1 == 0 && c2 == 1)
				c1 = 2;
			else
			if (c1 == 0 || c2 == 0)
				c1 = 1;
			else
				c1 = 0;
			ans[tmp[i]] = c1;
		}
	}
	return 1;			
}

void calccalc () {
	cin >> n >> m;
	forn (i, n)
		A[i].clear ();
	forn (i, m)
		cin >> a[i];
	forn (i, m)
		cin >> b[i];
	forn (i, m) {
		a[i] --;
		b[i] --;
	}
	forn (i, m) {
		A[a[i]].pb (b[i]);
		A[b[i]].pb (a[i]);
	}
	forn (i, n)
		sort (all (A[i]));
	int l = 3;
	int r = n;
	while (l < r) {
		int mid = (l + r + 1) / 2;
		vector <int> tmp;
		seta (ans, 255);
		forn (j, n)
			tmp.pb (j);
		if (check (tmp, mid))
			l = mid;
		else
			r = mid-1;
	}
	seta (ans, 255);
	vector <int> tmp;
	forn (j, n)
		tmp.pb (j);
	check (tmp, l);
	cout << l << endl;
	forn (i, n)
		cout << ans[i]+1 << " ";
	cout << endl;
}

int main ()
{
//	freopen ("input.txt", "r", stdin);
//	freopen ("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	forn (ii, tt) {
		printf ("Case #%d: ", ii+1);
		calccalc ();
	}	
	return 0;
}
