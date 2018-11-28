#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int T,N;
double x[3],y[3],r[3];

double dis(int i,int j)
{
	return sqrt((x[i] - x[j])*(x[i] - x[j]) + (y[i] - y[j])*(y[i] - y[j]));
}

double max(double a,double b)
{
	return a > b ? a : b;
}

int main()
{
	int t,i,j;
	double ans;
	freopen("D-small-attempt3.in","r",stdin);
	freopen("D.txt","w",stdout);
	scanf("%d",&T);
	for(t = 1;t <= T;t++)
	{
		scanf("%d",&N);
		for(i = 0;i < N;i++)
			scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
		if(N == 1)
			ans = r[0];
		else if(N == 2)
			ans = max(r[0],r[1]);
		else
		{
			ans = 1E9;
			if(max(r[0],max(r[1],max(r[2],(dis(1,2) + r[1] + r[2])/2.0))) < ans)
				ans = max(r[0],max(r[1],max(r[2],(dis(1,2) + r[1] + r[2])/2.0)));
			if(max(r[1],max(r[0],max(r[2],(dis(0,2) + r[0] + r[2])/2.0))) < ans)
				ans = max(r[1],max(r[0],max(r[2],(dis(0,2) + r[0] + r[2])/2.0)));
			if(max(r[2],max(r[1],max(r[0],(dis(0,1) + r[0] + r[1])/2.0))) < ans)
				ans = max(r[2],max(r[1],max(r[0],(dis(0,1) + r[0] + r[1])/2.0)));
		}
		printf("Case #%d: %.10lf\n",t,ans);
	}
	//system("PAUSE");
	return 0;
}
