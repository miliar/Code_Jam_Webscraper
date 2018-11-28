#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

struct gao
{
	int x1,y1,x2,y2;
}a[100001];


int n,m;

int main()
{
	freopen("in2.txt","r",stdin);
	freopen("out3.txt","w",stdout);
	int nn;
	scanf("%d",&nn);
	char s[20];
	int i,j,ii,k;
	for(ii=1;ii<=nn;ii++)
	{
		int x,y,tt,z,t,xx,yy;
		x=y=0;
		int p=0;
		memset(a,0,sizeof(a));
		printf("Case #%d: ",ii);
		scanf("%d",&tt);
		n=x=y=xx=yy=m=0;
		m++;
		while(tt--)
		{
			scanf("%s%d",s,&z);
			int l=strlen(s);
			while(z--)
			{
				for(i=0;i<l;i++)
				{
					if(s[i]=='R')
					{
						if(xx!=x||yy!=y)
						{
							a[n].x1=x;
							a[n].y1=y;
							a[n].x2=xx;
							a[n].y2=yy;
							n++;
							x=xx;
							y=yy;
						}
						p=(p+1)%4;
					}
					else if(s[i]=='L')
					{
						if(xx!=x||yy!=y)
						{
							a[n].x1=x;
							a[n].y1=y;
							a[n].x2=xx;
							a[n].y2=yy;
							n++;
							x=xx;
							y=yy;
						}
						p=(p+3)%4;
					}
					else
					{
						if(p==0)
							xx++;
						if(p==1)
							yy++;
						if(p==2)
							xx--;
						if(p==3)
							yy--;
					}
				}
			}
		}
		a[n].x1=x;
		a[n].y1=y;
		a[n].x2=a[n].y2=0;
		n++;
		for(i=0;i<n;i++)
		{
			if(a[i].x1>a[i].x2)
			{
				int c=a[i].x1;
				a[i].x1=a[i].x2;
				a[i].x2=c;
			}
			if(a[i].y1>a[i].y2)
			{
				int c=a[i].y1;
				a[i].y1=a[i].y2;
				a[i].y2=c;
			}
		}
		t=0;
		for(i=0;i<400;i++)
		{
			for(j=0;j<400;j++)
			{
				x=i-200;
				y=j-200;
				int x1,x2,y1,y2;
				x1=x2=y1=y2=0;
				for(k=0;k<n;k++)
				{
					if(a[k].y1==a[k].y2)
					{
						if(a[k].x1<x+0.5&&a[k].x2>x+0.5)
						{
							if(a[k].y1<y+0.5)
								y1++;
							if(a[k].y1>y+0.5)
								y2++;
						}
					}
					else if(a[k].x1==a[k].x2)
					{
						if(a[k].y1<y+0.5&&a[k].y2>y+0.5)
						{
							if(a[k].x1<x+0.5)
								x1++;
							if(a[k].x1>x+0.5)
								x2++;
						}
					}
				}
				if(x1&&x2&&x1%2==0&&x2%2==0)
					t++;
				else if(y1&&y2&&y1%2==0&&y2%2==0)
					t++;
			}
		}
		printf("%d\n",t);
	}
	return 0;
}