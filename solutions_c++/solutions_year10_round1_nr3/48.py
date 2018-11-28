#include<stdio.h>

bool check(int x,int y)
{
	int z;
	if (x<y)
	{
		z=x;
		x=y;
		y=z;
	}
	if (x%y==0)
	{
		if (x==y) return false;
		else return true;
	}
	if (x/y>1) return true;
	else return !check(y,x%y);
}

int main()
{
	int t,p;
	int a1,a2;
	int b1,b2;
	int i,j;
	long long k;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	for (p=1;p<=t;p++)
	{
		scanf("%d%d",&a1,&a2);
		scanf("%d%d",&b1,&b2);
		k=0;
		for (i=a1;i<=a2;i++)
		{
			int x1,x2,y1,y2;
			x1=1;
			x2=2;
			y1=1;
			y2=1;
			while (y1*i/y2-x1*i/x2>=3)
			{
				y1=x2;
				y2=x1+x2;
				x1=y2;
				x2=y1+y2;
			}
			if (b1<=x1*i/x2)
			{
				if (x1*i/x2<=b2) k=k+x1*i/x2-b1+1;
				else k=k+b2-b1+1;
				j=x1*i/x2+1;
			}
			else j=b1;
			for (;j<=b2&&j<=y1*i/y2+1&&j<i;j++)
				if (check(i,j)) k++;
		}
		for (i=b1;i<=b2;i++)
		{
			int x1,x2,y1,y2;
			x1=1;
			x2=2;
			y1=1;
			y2=1;
			while (y1*i/y2-x1*i/x2>=3)
			{
				y1=x2;
				y2=x1+x2;
				x1=y2;
				x2=y1+y2;
			}
			if (a1<=x1*i/x2)
			{
				if (x1*i/x2<=a2) k=k+x1*i/x2-a1+1;
				else k=k+a2-a1+1;
				j=x1*i/x2+1;
			}
			else j=a1;
			for (;j<=a2&&j<=y1*i/y2+1&&j<i;j++)
				if (check(i,j)) k++;
		}
		printf("Case #%d: %lld\n",p,k);
	}
	return 0;
}

