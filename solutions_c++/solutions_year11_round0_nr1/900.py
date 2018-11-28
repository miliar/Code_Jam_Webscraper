#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char p[100][10];
int r[100];
int main()
{
	int t,tt,n,x,y,s,i,j,nx,ny,temp;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
	{
		s=0;
		x=y=1;
		scanf("%d",&n);
		for (i=0;i<n;i++)
			scanf("%s %d",p[i],r+i);
		for (i=0;i<n;i++)
		{
			nx=ny=-1;
			for (j=n-1;j>=i;j--)
			{
				if (p[j][0]=='O')
					nx=r[j];
				else
					ny=r[j];
			}
			if (p[i][0]=='O')
			{
				temp=abs(nx-x)+1;
				if (ny==-1)
				{
					s+=temp;
					x=nx;
				}
				else if (abs(ny-y)<=temp)
				{
					s+=temp;
					x=nx;
					y=ny;
				}
				else if (ny<y)
				{
					s+=temp;
					x=nx;
					y=y-temp;
				}
				else
				{
					s+=temp;
					x=nx;
					y=y+temp;
				}
			}
			else
			{
				temp=abs(ny-y)+1;
				if (nx==-1)
				{
					s+=temp;
					y=ny;
				}
				else if (abs(nx-x)<=temp)
				{
					s+=temp;
					y=ny;
					x=nx;
				}
				else if (nx<x)
				{
					s+=temp;
					y=ny;
					x=x-temp;
				}
				else
				{
					s+=temp;
					y=ny;
					x=x+temp;
				}
			}
		}
		printf("Case #%d: %d\n",tt,s);
	}
	return 0;
}