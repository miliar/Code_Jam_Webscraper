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

#define pb push_back
#define mp make_pair
#define all(a) (a).begin(),(a).end()   
#define forr(it,b,lim) for (it = (b); it < (lim); ++it)
#define forn(it,b,lim) for (it = (b); it >= (lim); --it)
#define rep(it,lim) for (it = 0; it < (lim); ++it)
#define mset(array,value) memset(array, value, sizeof(array))

#define PATH "A-small-attempt0"

struct T
{
	vs v;
	int t;
};
set<vs> si;
int main()
{
	int i, j;
	freopen(PATH ".in", "rt", stdin); 
	//freopen(PATH ".out", "wt", stdout);

	int Tt, test;
	scanf("%d", &Tt);

	rep(test, Tt)
	{
		int res = inf;
		si.clear();

		int n;
		scanf("%d", &n);

		vs v(n);
		char s[100];
		rep(i, n)
			scanf("%s", &s), v[i] = s;

		queue <T> q;
		T c;
		c.v = v, c.t = 0;
		si.insert(v);
		q.push(c);
		while (!q.empty())
		{
			T c = q.front(); q.pop();

			int ii, jj, ok = 1;
			rep(ii, n)
				for (jj = ii + 1; jj < n; ++jj)
					if (c.v[ii][jj] == '1')
						ok = 0;
			if (ok == 1)
				res = min(res, c.t);

			rep(i, n-1)
				{
					vs w = c.v;
					swap(w[i], w[i+1]);
					if (si.find(w) == si.end())
					{
						si.insert(w);
						T nc;
						nc.v = w, nc.t = c.t + 1;
						q.push(nc);

					}
				}
		}
		printf ("Case #%d: %d\n", test + 1, res);
	}

	return 0;
}