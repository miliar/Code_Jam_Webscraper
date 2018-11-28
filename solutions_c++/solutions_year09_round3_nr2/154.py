#include<stdio.h>
#include<math.h>

int n,sp[501][3],v[501][3];
double dmin,tmin;

void process()
{
	int i,p1=0,p2=0,p3=0,q1=0,q2=0,q3=0;
	double a,b,c,x;
	for(i=0;i<n;i++)
	{
		p1+=v[i][0]; p2+=v[i][1]; p3+=v[i][2];
		q1+=sp[i][0]; q2+=sp[i][1]; q3+=sp[i][2];
	}
	a=p1*p1+p2*p2+p3*p3; b=2*p1*q1+2*p2*q2+2*p3*q3; c=q1*q1+q2*q2+q3*q3;
	if(a==0)
	{
		tmin=0; dmin=sqrt(c)/double(n);
	}
	else
	{
		tmin=-b/(a+a);
		if(tmin<0) tmin=0;
		x=a*tmin*tmin+b*tmin+c;
		if(x<0) x=0;
		dmin=sqrt(x)/double(n);
	}
}

int main()
{
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	int i,j,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&n);
		for(j=0;j<n;j++)
		{
			scanf("%d%d%d%d%d%d",&sp[j][0],&sp[j][1],&sp[j][2],&v[j][0],&v[j][1],&v[j][2]);
		}
		process();
		printf("Case #%d: %.8f %.8f\n",i,dmin,tmin);
	}
	return 0;
}