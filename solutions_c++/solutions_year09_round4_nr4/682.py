#include <iostream>
#include <cmath>
using namespace std;

int n;
struct point
{
	double x,y;
	double r;
}a[100];

void init()
{
	cin>>n;
	int i;
	for (i=1;i<=n;i++)
		cin>>a[i].x>>a[i].y>>a[i].r;
}
void make()
{
	double r,m;
	int i,j;
	r=1e50;

	if (n>=3)
	{
		for (i=1;i<n;i++)
		{
			for (j=i+1;j<=n;j++)
			{
				m=sqrt((a[i].x-a[j].x)*(a[i].x-a[j].x)+(a[i].y-a[j].y)*(a[i].y-a[j].y));
				m=m+a[i].r+a[j].r;
				m=m/2;
				if (m<r) r=m;
			}
		}
	}
	else if (n==2)
	{
		if (a[1].r>a[2].r) r=a[1].r;
		else r=a[2].r;

	}
	else r=a[1].r;
	printf("%.6lf\n",r);
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cs;
	cin>>cs;
	int i;
	for (i=1;i<=cs;i++)
	{
		init();
		cout<<"Case #"<<i<<": ";
		make();

	}
	return 0;
}