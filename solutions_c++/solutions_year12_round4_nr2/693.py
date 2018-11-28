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
LL W,L,r[2005],xx[2005],yy[2005];
LL gcd(LL x,LL y){LL t;for(;y!=0;){t=x%y;x=y;y=t;}return x;}
bool cmp1(int x, int y){return x>y; }
LL sqr(LL x){return x*x; }
bool legal(int x,int y,LL rad,int tt)
{
	int i;
	return (sqr(x-xx[tt])+sqr(y-yy[tt]))>=sqr(rad);
}
vector <LL> xcan,ycan;
int main()
{
  LL i,j,k,l,t1,t2,t3,t4,t5,t,T,T2;
  double u1,u2,u3,u4,u5;
  char c1,c2,c3;
  srand((unsigned)time(0));//srand(72888306);
  #ifndef ONLINE_JUDGE
  freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
  #endif
  cin >>T;T2=T;
  for(;T--;)
  {
			printf("Case #%I64d:",T2-T);  //
			cin >>n>>W>>L;
			
			for(i=1;i<=n;i++)
			{
				cin >>r[i];
			}
	//		sort(r+1,r+n+1,cmp1);
			xcan.clear();ycan.clear();
			xcan.push_back(0);ycan.push_back(0);
			for(i=1;i<=n;i++)
			{
				int haveans=0;
				for(j=0;j<xcan.size()&&!haveans;j++)
				 for(k=0;k<ycan.size()&&!haveans;k++)
				 {
						if (xcan[j]==0)t1 =0;else t1=xcan[j]+r[i];
						if (ycan[k]==0)t2 =0;else t2=ycan[k]+r[i];
					//	if (!(r[i]<=t1&&t1+r[i]<=W &&r[i]<=t2&&t2+r[i]<=L))continue;
					 if (!(0<=t1&&t1<=W && 0<=t2&&t2<=L))continue;
						for(l=1;l<i;l++)
						 if (!legal(t1,t2,r[i],l))break;
						if (l<i)continue;
						haveans=1;
						xx[i]=t1,yy[i]=t2;
						xcan.push_back(xx[i]+r[i]);ycan.push_back(yy[i]+r[i]);
					}
			 if (!haveans){printf("err %d\n",i);return 0 ;}
			}
			for(i=1;i<=n;i++)printf(" %.6lf %.6lf",(double)xx[i],(double)yy[i]);
			printf("\n");
		}
  return 0;
}
