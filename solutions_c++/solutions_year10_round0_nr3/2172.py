#include <stdio.h>
#include <string.h>
int main()
{
	int g[2002];
	int b[1001];
	int sum[1001];
	int  f[1001];
	int a,r;
	int T,R,K,N;
	int i,j;
	int s,t;
	int h,w,x;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&T);
	for (int ii=1;ii<=T;ii++)
	{
		scanf("%d%d%d",&R,&K,&N);
		for (i=0;i<N;i++)
		{
			scanf("%d",&g[i]);
			g[i+N]=g[i];
			if (i==0)
			{
				sum[i]=g[i];
			}
			else 
			{
				sum[i]=sum[i-1]+g[i];
			}
		}
		
		a=1;
		i=0;
		memset(f,0,sizeof(f));
		while (f[i]==0)
		{
			j=i;
			s=0;
			while (j<i+N&&s+g[j]<=K)
			{
				s+=g[j];
				j++;
			}
			b[i]=j-i;
			f[i]=a++;
			i=j%N;
		}
		r=a-f[i];
		a=f[i]-1;
		t=i;
		h=0;
		if (R<=a)
		{
			j=0;
			for (i=0;i<R;i++)
			{
				h+=b[j];
				j+=b[j];
				j%=N;
			}
			w=h/N*sum[N-1]+sum[h%N];
		}
		else
		{
			h=0;
			j=0;
			for (i=0;i<a;i++)
			{
				h+=b[j];
				j+=b[j];
				j%=N;
			}
			x=0;
			j=t;
			for (i=0;i<r;i++)
			{
				x+=b[j];
				j+=b[j];
				j%=N;
			}
			h+=(R-a)/r*x;
			j=t;
			for (i=0;i<(R-a)%r;i++)
			{
				h+=b[j];
				j+=b[j];
				j%=N;
			}
			if (h%N==0)
			{
				w=h/N*sum[N-1];
			}
			else
			{
				w=h/N*sum[N-1]+sum[h%N-1];
			}	
		}
		printf("Case #%d: %d\n",ii,w);
	}
}