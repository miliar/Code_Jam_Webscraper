// powered by xpd1
// on 2011-03-
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <ctime>
#include <cstring>
#include <ctype.h>
#include <memory>
#include <fstream>
#include <string>

#include <map>
#include <queue>
#include <stack>
#include <iomanip>
#include <vector>
#include <list>
#include <deque>
#include <set>
//#include <conio.h>
#define oo 2000000000
#define ol 200000000000000000ll
#define ooo 1E14
#define EPS 1E-10
/*#define dis(x1,y1,x2,y2)\
 (double)(sqrt( ((x1)-(x2))*((x1)-(x2)) + ((y1)-(y2))*((y1)-(y2)) ) )
#define disx(x,y) (double)(sqrt((x)*(x)+(y)*(y)))
#define dianji(x1,y1,x2,y2) (double)((x1)*(x2)+(y1)*(y2))
#define chaji(x1,y1,x2,y2) (double)((x1)*(y2)-(y1)*(x2))*/
using namespace std;
const double PI=acos((double)-1);
typedef long long LL;
int ts,ts2;
int n,m;
LL gcd(LL x,LL y){LL t;for(;y!=0;){t=x%y;x=y;y=t;}return x;}
LL d[10005],len[10005],D,f[100005];
int main()
{
  int i,j,k,t1,t2,t3,t4,t5,t,T,T2;
  double u1,u2,u3,u4,u5;
  char c1,c2,c3;
  srand((unsigned)time(0));//srand(72888306);
  #ifndef ONLINE_JUDGE
  freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
  #endif
  cin >>T;T2=T;
  for(;T--;)
  {
			
			printf("Case #%d: ",T2-T);
			scanf("%d",&n);
			for(i=1;i<=n;i++)
			{
				cin >>d[i]>>len[i];
			}
			cin >>D;
			fill(f,f+n+15,0);
			for(i=1;i<=n;i++)
			{
				if (i==1){f[i]=d[1];}
				for(j=1;j<i;j++)
				 if (f[j]+d[j]>=d[i])
				  f[i]=max(f[i],d[i]-d[j]);
				f[i]=min(f[i],len[i]);
				if (f[i]+d[i]>=D)break;
			}
			if (i>n)printf("NO\n");
			else printf("YES\n");
		}
  return 0;
}
