#pragma comment (linker, "/STACK:64000000")
#include <algorithm>  
#include <iostream>  
#include <cstdio>  
#include <sstream>  
#include <ctype.h>  
#include <cstring>  
#include <string>  
#include <cmath>  
#include <queue>  
#include <vector>  
#include <map>  
#include <set>  

using namespace std;  

typedef long long i64;
typedef unsigned long long u64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef istringstream iss;
typedef ostringstream oss;   

const int inf = 1<<30;
const int N = 107;

#define pb push_back
#define mp make_pair
#define all(a) (a).begin(),(a).end()   
#define forr(it,b,lim) for (it = (b); it < (lim); ++it)
#define forn(it,b,lim) for (it = (b); it >= (lim); --it)
#define rep(it,lim) for (it = 0; it < (lim); ++it)
#define cl(array,value) memset(array, value, sizeof(array))

char in[] = "B-large.in";
char out[] = "B-large.out";

int di[] = {-1, 0, 0, 1};
int dj[] = {0, -1, 1, 0};

int a[N][N], used[N][N];
char s[N][N], color[N];

struct S
{
	int alt, i, j;
	S() {}
	S(int aa, int ii, int jj)
	{
		alt = aa, i = ii, j = jj;
	}
	bool operator < (const S &b) const
	{
		if (alt != b.alt)	return alt > b.alt;
		if (i != b.i)	return i < b.i;
		return j < b.j;
	}
};
vector<S> v;
int n, m, ok;
void dfs (int i, int j)
{
	if (used[i][j] == 0)
		used[i][j] = -2;
	int k, ind = -1, best = inf, ni, nj;
	for (k = 0; k < 4; ++k)
	{
		ni = i + di[k], nj = j + dj[k];
		if (ni < 0 || ni >= n || nj < 0 || nj >= m)	continue;
		if (best > a[ni][nj])	best = a[ni][nj], ind = k;
	}
	if (ind == -1) return;

	ni = i + di[ind], nj = j + dj[ind];
	if (a[ni][nj] >= a[i][j]) return;
	if (used[ni][nj] == 0)	dfs(ni, nj);
	if (used[ni][nj] > 0)	used[i][j] = used[ni][nj];
}
int main()
{
	int i, j, k;
	freopen(in, "rt", stdin); freopen(out, "wt", stdout);

	int T, test;
	scanf("%d", &T);

	rep(test, T)
	{
		int res = 0;
		v.clear();
		scanf("%d%d", &n, &m);
		rep(i, n)
			rep(j, m)
		{
			scanf("%d", &a[i][j]);
			v.pb( S(a[i][j], i, j) );
		}
		sort(all(v));
		cl(used, 0);	cl(s, 0);	cl(color, -1);
		int ncomp = 0;
		for (i = 0; i < v.size(); ++i)
		{
			int iii = v[i].i, jj = v[i].j, alt = v[i].alt;
			if (used[iii][jj] != 0)
				continue;
			ok = 0;
			dfs (iii, jj);
			int hasnew = 0;
			rep(j, n)
				rep(k, m)
					if (used[j][k] == -2)
						used[j][k] = ncomp+1, hasnew = 1;
			if (hasnew)
				++ncomp;
		}
		char ptt = 'a';
		color[ used[0][0] ] = 'a';
		rep(i, n)
			rep(j, m)
				if (color[ used[i][j] ] == -1) color[ used[i][j] ] = ++ptt;

		printf ("Case #%d:\n", test + 1);
		rep(i, n)
		{
			printf ("%c", color[ used[i][0] ]);
			for (j = 1; j < m; ++j)
				printf (" %c", color[ used[i][j] ]);
			printf ("\n");
		}
	}

	return 0;
}