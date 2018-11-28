#include<stdio.h>
#include<string.h>
#define MAX 101
char c[MAX][MAX];
double a[MAX],b[MAX],p[MAX],p2[MAX],p3[MAX];
int main()
{
	int cs,n,i,j,x;
	double y;
	scanf("%d",&cs);
	for(int dd=1;dd<=cs;dd++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%s",c[i]);
		for(i=0;i<n;i++)
		{
			for(a[i]=b[i]=j=0;j<n;j++)
				if(c[i][j]=='1')
				{
					a[i]+=1;
					b[i]+=1;
				}
				else if(c[i][j]=='0')
					b[i]+=1;
		}
		for(i=0;i<n;i++)
		{
			for(y=x=j=0;j<n;j++)
				if(c[i][j]!='.')
				{
					y+=(a[j]-c[j][i]+'0')/(b[j]-1);
					x++;
				}
			p2[i]=y/x;
		}
		for(i=0;i<n;i++)
		{
			for(y=x=j=0;j<n;j++)
				if(c[i][j]!='.')
				{
					y+=p2[j];
					x++;
				}
			p3[i]=y/x;
		}
		printf("Case #%d:\n",dd);
		for(i=0;i<n;i++)
		{
			printf("%.8f\n",0.25*a[i]/b[i]+0.5*p2[i]+0.25*p3[i]);
		}
	}
}
