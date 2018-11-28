#include<cstdio>
#include<algorithm>
#include<queue>
#include<set>
#include<utility>
#include<list>
#include<vector>
using namespace std;
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
typedef pair<int,int> PII;
int n,m,a;
bool dbg=0;
PII find(int xs,int ys,int xa,int ya,int xb,int yb)
{
	if(dbg)printf("find(%d,%d,%d,%d,%d,%d)\n",xs,ys,xa,ya,xb,yb);
	if(xa>n||xb>n||ya>m||yb>m)return MP(-1,-1);
	if(abs(xa*ys-ya*xs)==a)return MP(xa,ya);
	if(abs(xb*ys-yb*xs)==a)return MP(xb,yb);
	if(xa*ys>ya*ys)
	{
		return find(xs,ys,xa+xb,ya+yb,xb,yb);
	}
	else
		return find(xs,ys,xa,ya,xb+xa,yb+ya);
}
inline bool check(int x1,int y1,int x2,int y2)
{
	return (abs(x1*y2-x2*y1)==a);
}

void computeCase(int cas)
{
	scanf("%d%d%d",&n,&m,&a);
	for(int x=0;x<=n;x++)
		for(int y=0;y<=m;y++)
		{
			for(int x1=0;x1<=n;x1++)
				for(int y1=0;y1<=m;y1++)
					if(check(x,y,x1,y1))
					{
						printf("Case #%d: 0 0 %d %d %d %d\n",cas,x,y,x1,y1);
						return;
					}
			/*PII res=find(x,y,0,1,1,0);
			if(res.ST>=0)
			{
				printf("Case #%d: 0 0 %d %d %d %d\n",cas,x,y,res.ST,res.ND);
				return;
			}*/
		}
	printf("Case #%d: IMPOSSIBLE\n",cas);
}


int main()
{
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		computeCase(i+1);
	}
	return 0;
}
