#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <algorithm>
#include <string>

#define rep(i,x,y) for (int i = x; i < y; i++)

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int main()
{
   freopen("in", "r", stdin);
   freopen("out", "w", stdout);
   int tt;
   scanf("%d\n", &tt);
   rep(z,0,tt)
   {
	printf("Case #%d: ", z + 1);
   string s;
   getline(cin, s);
   int len = s.length();
   map<char, int> m;
   for (int i = 0; i < len; i++)
   {
	   m[s[i]] = -1;
	}
   int k = 0;
   m[s[0]] = 1;
   string res = "1";
   for (int i = 1; i < len; i++)
   {
	   if (m[s[i]] == -1)
	   {
	   	m[s[i]] = k;
		if (k != 0)
		{
			k++;
		}
		else
		{
			k = 2;
		}
		}
	   res += (m[s[i]] + '0');
   }
   ll ans = 0;
   int base = k ? k : 2;
   int lens = res.length();
   cerr << "test is " << z + 1 << " and res = " << res << endl;
   for (int i = 0; i < lens; i++)
   {
	   cerr << base << endl;
	   ans += (res[i] - '0') * pow(base, lens - i - 1);
   }
   printf("%lld\n", ans);
	}

   return 0;
}
