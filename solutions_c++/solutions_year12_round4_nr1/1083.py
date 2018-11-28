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
typedef unsigned long long ULL;
typedef pair<int,int> PII;
double PI = acos(-1.0);
template <class T> inline void checkmin(T &a, T b) {if (b<a) a=b;}
template <class T> inline void checkmax(T &a, T b) {if (b>a) a=b;}
template <class T> inline T gcd(T a, T b) {if (!b) return a; return gcd(b,a%b);}
const int MAX = 10000 + 10;
int test,I;
int i,n,d[MAX], l[MAX],D,now;
int start[MAX];
int main()
{
//	freopen("A-small-attempt0.in","r",stdin); freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin); freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin); freopen("A-small-attempt2.out","w",stdout);
//	freopen("A-small-attempt3.in","r",stdin); freopen("A-small-attempt3.out","w",stdout);
//	freopen("A-small-attempt4.in","r",stdin); freopen("A-small-attempt4.out","w",stdout);
	freopen("A-large.in","r",stdin); 		  freopen("A-large.out","w",stdout);
//	freopen("A.in","r",stdin);
	scanf("%d",&test);
	for (I=1; I<=test; ++I)
	{
		scanf("%d",&n);
		memset(start, 0 , sizeof start);
		REP(i,n)
		{
			scanf("%d%d",d+i,l+i);
		}
		scanf("%d",&D);
		start[0] = d[0];
		int f = 0;
		now = 0;
		REP(i,n)
		{
			if (start[i] ==0) break;
			if (d[i]+start[i]>=D)
			{
				printf("Case #%d: YES\n",I);
				f = 1;
			}
			int j = now+1;
			while (j<n)
			{
				if (d[j]>d[i]+start[i]) break;
				start[j] = d[j]-d[i];
				checkmin(start[j], l[j]);
				++j;
			}
			now = j-1;
		}
		if (!f)
		printf("Case #%d: NO\n",I);
	}
}













