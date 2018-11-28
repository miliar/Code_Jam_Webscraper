#define _CRT_SECURE_NO_DEPRECATE
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <set>
#include <cmath>
#include <queue>
#include <sstream>
#include <iostream>
using namespace std;
#define inf      2147483647
#define inf64    9223372036854775807
#define eps      1e-10
#define pi      3.14159265358
#define sqr(a) (a)*(a)
#define rall(a) a.rbegin(),a.rend()
#define all(a) a.begin(),a.end()
#define sz(a) (a).size()
#define mset(a,v) memset(a, v, sizeof(a))
#define pb push_back 
#define updateMIN(a, x) if(a > x)a = x 
#define updateMAX(a, x) if(a < x)a = x 
typedef long long ll;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;

string s;
ll res;

bool isUgly()
{
	ll temp = 0, cur = 0;
	int i; char last = '+';
	for(i = 0 ; i < sz(s) ; ++i)
	{
        if(s[i] == '-' || s[i] == '+')
		{
			if(last == '-')
				temp -= cur;
			else temp += cur;
			last = s[i];
			cur = 0;
		}
		else
		{
			cur *= 10;
			cur += (s[i] - '0');
		}
	}
    if(last == '-') temp -= cur;
    else temp += cur;
	return (temp % 2 == 0 || temp % 3 == 0 || temp % 5 == 0 || temp % 7 == 0 || temp == 0);
}

void dfs(int pos)
{
	if(pos == sz(s))
	{
		if(isUgly())res++;
	}
	else
	{
       s.insert(pos, 1, '-');
	   dfs(pos + 2);
	   s[pos] = '+';
	   dfs(pos + 2);
	   s.erase(pos, 1);
	   dfs(pos + 1);
	}
}

int main()
{
	int k, T, i;
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
	scanf("%d", &T);
	for(k = 1 ; k <= T ; ++k)
	{
		cin >> s;
        res = 0;
        dfs(1);
		printf("Case #%d: %lld\n", k, res);
	}
	return 0;
}
