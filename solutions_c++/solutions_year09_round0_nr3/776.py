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

char in[] = "C-large.in";
char out[] = "C-large.out";

char s[505];
char t[] = "welcome to code jam";
int dp[25][505];
int mod = 10000;
int main()
{
	int i, j, k;
	freopen(in, "rt", stdin); freopen(out, "wt", stdout);

	int T, test;
	gets(s);
	sscanf(s, "%d", &T);

	rep(test, T)
	{
		int res = 0;

		gets(s);

		int len = strlen(t);
		int n = strlen(s);

		cl(dp, 0);

		rep(i, n)
			if (s[i] == 'w')
				dp[0][i] = 1;

		for (i = 1; i < len; ++i)
		{ 
			for (j = i; j < n; ++j)
				if (s[j] == t[i])
					for (k = 0; k < j; ++k)
						if (s[k] == t[i-1])
							dp[i][j] = (dp[i][j] + dp[i-1][k]) % mod;
		}
		for (i = 0; i < n; ++i)
			res = (res + dp[len-1][i]) % mod;



		printf ("Case #%d: %04d\n", test+1, res);
	}

	return 0;
}