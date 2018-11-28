#include <stdio.h>
int ans[2000000][7];
int f(int x,int y)
{
	int i=0,j=0,t,k,l,c=y;
	int xx[20],yy[20];
	while(x>0)
	{
		xx[i++]=x%10;
		x=x/10;
	}
	while(y>0)
	{
		yy[j++]=y%10;
		y=y/10;
	}
	if(i==j)
	{
		k=i+j;l=j;
		i=0;--j;
		while(i<j)
		{
			t=xx[j];
			xx[j]=xx[i];
			xx[i]=t;
			i++;j--;
		}
		for(i=l;i<k;i++)
			xx[i]=xx[i-l];
		for(i=0;i<l;i++)
		{
			for(j=i,t=0;j<i+l;j++)
				t=t*10+xx[j];
			if(t==c)
				return 1;
		}
	}
	else
		return 0;
	return 0;
}
int main()
{
	int i,j,k,l=0,m,n,a,b;
	scanf("%d",&n);
	while(n--)
	{
		k=0;
		scanf("%d%d",&a,&b);
		for(i=a;i<b;i++)
			for(j=i+1;j<=b;j++)
				if(f(i,j))
					k++;
		printf("Case #%d: %d\n",++l,k);
	}
}
