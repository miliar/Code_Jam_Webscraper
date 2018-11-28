#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>
#include <climits>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <string>
#include <utility>
#include <map>
#include <set>
#include <algorithm>
#define REP(i,n)      for (i=0; i<(n); ++i)
#define FOR(i,l,r)    for (i=(l); i<=(r); ++i)
#define FOReach(it,c) for (__typeof(c.begin()) it=c.begin(); it!=c.end(); ++it)
#define foreach(c)    for (__typeof(c.begin()) it=c.begin(); it!=c.end(); ++it)
using namespace std;
typedef long long LL;
template <class T> inline void checkmin(T &a, T b) {if (b<a) a=b;}
template <class T> inline void checkmax(T &a, T b) {if (b>a) a=b;}
template <class T> inline T gcd(T a, T b) {if (!b) return a; return gcd(b,a%b);}

int test,i,j,l;
char s[200];
char a[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d ",&test);
	for (i = 1; i<=test; ++i)
	{
		gets(s);
		printf("Case #%d: ",i);
		l = strlen(s);
		for (j=0; j<l; ++j)
		{
			if (s[j] == ' ')
			{
				printf(" ");
			}
			else
			{
				printf("%c",a[s[j]-97]);
			}
		}
		printf("\n");
	}
}












