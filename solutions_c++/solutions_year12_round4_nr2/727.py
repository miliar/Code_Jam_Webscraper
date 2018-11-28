#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<iostream>
#define swap(a, b)  ((a) == (b) || (a) ^= (b), (b) ^= (a), (a) ^= (b))
using namespace std;
typedef int TT;
typedef __int64 ll;
TT abs(TT x)
{
	return x>0?x:-x;
}
TT min(TT x,TT y)
{
	return x<y?x:y;
}
TT max(TT x,TT y)
{
	return x>y?x:y;
}
const int INF = 1000000000;
#define mp(x,y) make_pair(x,y)
typedef pair<int,int>per;
const int N = 15;
double rx[N],ry[N];
struct P
{
	double r;
	int id;
}data[N];
bool cmp(P x,P y)
{
	return x.r>y.r;
}
int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n,ca=1,T,i,j;
	double W,L;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",ca++);
		scanf("%d%lf%lf",&n,&W,&L);
		double dx=W/1000,dy=L/1000;
		for(i=0;i<n;i++)scanf("%lf",&data[i].r),data[i].id=i;
		sort(data,data+n,cmp);
		int k=0,h;
		while(k<n)
		{
		//	printf("k:%d \n",k);
			for(i=0;i<=1000&&k<n;i++)
			{
				for(j=0;j<=1000&&k<n;j++)
				{
					double nx=dx*i,ny=dy*j;
					for(h=0;h<k;h++)
					{
						if((data[h].r+data[k].r)*(data[h].r+data[k].r)<(nx-rx[data[h].id])*(nx-rx[data[h].id])+(ny-ry[data[h].id])*(ny-ry[data[h].id]))
							continue;
						break;
					}
					if(h==k)
					{
						rx[data[k].id]=nx;
						ry[data[k].id]=ny;
						k++;
					}
				}
			}
		//	printf("22 k:%d \n",k);
		}
		for(i=0;i<n;i++)printf("%.9lf %.9lf ",rx[i],ry[i]);
		puts("");
	}
	return 0;
}