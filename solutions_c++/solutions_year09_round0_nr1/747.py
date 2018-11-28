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
#define cl(array,value) memset(array, value, sizeof(array))

char in[] = "A-large.in";
char out[] = "A_large.out";

int zero;
char s[1000];
vs b;
int main()
{
	int i, j;
	freopen(in, "rt", stdin); freopen(out, "wt", stdout);

	int T, test;

	int L, D, N;
	scanf("%d%d%d", &L, &D, &N);

	rep(i, D)
		scanf("%s", s), b.pb(s);

	rep(test, N)
	{
		int res = 0;
	
		scanf("%s", s);

		vs w;
		int n = strlen(s), st = 0, p = 0;
		for (i = 0; i < n; ++i)
		{
			if (s[i] == '(') ++st;
			else if (s[i] == ')') --st, ++p;
			else
			{
				if (w.size() <= p)
					w.resize(p + 1);
				w[p] += s[i];
				if (!st) ++p;
			}
		}
		for (i = 0; i < b.size(); ++i)
		{
			int ok = true;
			if (b[i].size() != w.size())
				ok /= zero;
			else for (j = 0; j < w.size(); ++j)
				if (w[j].find( b[i][j] ) == string::npos)
					ok = false;

			if (ok)
				++res;
		}

		printf ("Case #%d: %d\n", test + 1, res);
	}

	return 0;
}