#include <iostream>
#include <cmath>
using namespace std;

#define sqr(x) ((x)*(x))
int i,j,k,m,n,p,t;
int x[45],y[45],r[45];
double cb,wb;

double ccb(int u,int v)
{
	return (sqrt(1.0*(sqr(x[u]-x[v])+sqr(y[u]-y[v])))+r[u]+r[v])/2.0;

}

int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small-attempt1.out","w",stdout);
	scanf("%d",&t);
	for (p=1; p<=t; p++)
	{
		scanf("%d",&n);
		for (i=1; i<=n; i++)
			scanf("%d%d%d",&x[i],&y[i],&r[i]);
		printf("Case #%d: ",p);
		if (n==1) printf("%.8lf\n",(double)r[1]);
		if (n==2) printf("%.8lf\n",(double)max(r[1],r[2]));
		if (n==3)
		{
			cb=max(ccb(1,2),(double)r[3]);
			cb=min(cb,max(ccb(1,3),(double)r[2]));
			cb=min(cb,max(ccb(2,3),(double)r[1]));
			printf("%.8lf\n",cb);
		}
	}

//	system("pause");
	return 0;
}
