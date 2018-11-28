#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
using namespace std;
#define eps 1e-7
#define M 5
class pnt_type
{
public:
	double x,y,r;
};

pnt_type pnt[M];
int n;

void read_data()
{
	cin >> n;
	int i;
	for (i=1;i<=n;i++) cin >> pnt[i].x >> pnt[i].y >> pnt[i].r;
}

double dist(pnt_type a,pnt_type b)
{
	return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

double work_ans()
{
	if (n == 1) return pnt[1].r;
	else if (n == 2) return max(pnt[1].r,pnt[2].r);
	double ans1,ans2,ans3;
	ans1 = max((dist(pnt[1],pnt[2]) + pnt[1].r + pnt[2].r) / 2,pnt[3].r);
	ans2 = max((dist(pnt[1],pnt[3]) + pnt[1].r + pnt[3].r) / 2,pnt[2].r);
	ans3 = max((dist(pnt[2],pnt[3]) + pnt[2].r + pnt[3].r) / 2,pnt[1].r);

	return min(ans1,min(ans2,ans3));
}

int main()
{
	freopen("D-small-attempt2.in","r",stdin);
	freopen("D.out","w",stdout);
	double ans;
	int t,i;
	cin >> t;
	for (i=1;i<=t;i++)
	{
		read_data();
		ans = work_ans();
		printf("Case #%d: %.6lf\n",i,ans);
	}
	return 0;
}
