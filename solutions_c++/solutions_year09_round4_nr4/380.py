#include<stdio.h>
#include<math.h>

int n,p[3][3];

double process()
{
	double min=2100000000,a,b,dx,dy;

	if(n==1) return p[0][2];
	if(n==2)
	{
		min=p[0][2];
		if(p[1][2]>min) min=p[1][2];
		return min;
	}

	dx=p[1][0]-p[2][0]; dy=p[1][1]-p[2][1];
	a=p[0][2]; b=sqrt(dx*dx+dy*dy)+double(p[1][2]+p[2][2]); b=b/2.;
	if(a<b) a=b;
	if(a<min) min=a;

	dx=p[0][0]-p[2][0]; dy=p[0][1]-p[2][1];
	a=p[1][2]; b=sqrt(dx*dx+dy*dy)+double(p[0][2]+p[2][2]); b=b/2.;
	if(a<b) a=b;
	if(a<min) min=a;

	dx=p[1][0]-p[0][0]; dy=p[1][1]-p[0][1];
	a=p[2][2]; b=sqrt(dx*dx+dy*dy)+double(p[1][2]+p[0][2]); b=b/2.;
	if(a<b) a=b;
	if(a<min) min=a;

	return min;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,t;
	double res;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&n);
		for(j=0;j<n;j++)
		{
			scanf("%d%d%d",&p[j][0],&p[j][1],&p[j][2]);
		}
		res=process();
		printf("Case #%d: %lf\n",i,res);
	}
	return 0;
}