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

int test,n,surp,p,a[100],i,j,med,highyes,highno,lowyes,lowno,ans;

int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&test);
	for (i = 1; i<=test; ++i)
	{
		scanf("%d%d%d",&n,&surp,&p);
		for (j = 0; j<n; ++j)
			scanf("%d",a+j);
		med = highyes = highno = lowyes = lowno = 0;
		REP(j,n)
		{
			if (a[j]%3==0)
			{
				if (a[j]/3>=p)
					if (a[j]==0 || a[j]==30) highno++;
					else		 highyes++;
				else if (a[j]/3+1==p && a[j]!=0) med++;
				else
				{
					if (a[j]==0) lowno++;
					else  		 lowyes++;
				}
			}
			else if (a[j]%3==1)
			{
				if (a[j]/3+1>=p)
					if (a[j]==1) highno++;
					else		 highyes++;
				else
					if (a[j]==1) lowno++;
					else		 lowyes++;
			}
			else
			{
				if (a[j]/3+1>=p)
					if (a[j]==29) highno++;
					else 		  highyes++;
				else if (a[j]/3+2==p) med++;
				else lowyes++;
			}
		}
		ans = highyes+highno;
		ans += min(med, surp);
		printf("Case #%d: %d\n",i,ans);
	}
}














