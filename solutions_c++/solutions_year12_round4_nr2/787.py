
#include <stdio.h>
#include <math.h>
#include <map>
#include <time.h>
using namespace std;

const int maxn = 10010;

double W,H;
int n;
struct point
{
	double x,y;
}pt[maxn];

double r[maxn];

double dist(point a,point b)
{
	return sqrt((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y));
}

bool ok(int id,double x,double y)
{
	int i;
	point t;
	t.x = x; t.y = y;
	for(i=0;i<id;i++)
		if(dist(t,pt[i])<r[id] + r[i])
			return false;
	return true;
}

void solve()
{
    int i;
	pt[0].x = pt[0].y = 0;
	for(i=1;i<n;i++)
	{
        while(1)
		{
			int t = rand();
			double x = (rand()%n)/1.0/n * W;
			double y = (rand()%n)/1.0/n * H;
			if(x > W || y > H) continue;
			if(ok(i,x,y))
			{
				pt[i].x = x;
				pt[i].y = y;
				break;
			}
		}
	}
	for(i=0;i<n;i++)
		printf(" %.2lf %.2lf",pt[i].x,pt[i].y);
	printf("\n");
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.txt","w",stdout);
	int ct,caset = 1;
	scanf("%d",&ct);
	while(ct--)
	{
		printf("Case #%d:",caset++);
        scanf("%d",&n);
		scanf("%lf%lf",&W,&H);
		int i;
		for(i=0;i<n;i++)
			scanf("%lf",&r[i]);
		solve();
	}
	return 0;
}