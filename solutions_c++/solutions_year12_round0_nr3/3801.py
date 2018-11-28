#include <cstdio>
#include <cstdlib>
#include <cstring>

int T,id,a,b,i,j,f[10];
int ans;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&T);
	for (id=1;id<=T;id++)
	{
		ans=0;
		scanf("%d%d",&a,&b);
		for (i=a;i<b;i++)
		{
			if (i>999999)
			{
				j=i/10+i%10*1000000;
				f[0]=j;
				if (j>i && j<=b)ans++;
				j=i/100+i%100*100000;
				f[1]=j;
				if (j!=f[0] && j>i && j<=b)ans++;
				j=i/1000+i%1000*10000;
				f[2]=j;
				if (j!=f[0] && j!=f[1] && j>i && j<=b)ans++;
				j=i/10000+i%10000*1000;
				f[3]=j;
				if (j!=f[0] && j!=f[1] && j!=f[2] && j>i && j<=b)ans++;
				j=i/100000+i%100000*100;
				f[4]=j;
				if (j!=f[0] && j!=f[1] && j!=f[2] && j!=f[3] && j>i && j<=b)ans++;
				j=i/1000000+i%1000000*10;
				f[5]=j;
				if (j!=f[0] && j!=f[1] && j!=f[2] && j!=f[3] && j!=f[4] && j>i && j<=b)ans++;
			}
			else if (i>99999)
			{
				j=i/10+i%10*100000;
				f[0]=j;
				if (j>i && j<=b)ans++;
				j=i/100+i%100*10000;
				f[1]=j;
				if (j!=f[0] && j>i && j<=b)ans++;
				j=i/1000+i%1000*1000;
				f[2]=j;
				if (j!=f[0] && j!=f[1] && j>i && j<=b)ans++;
				j=i/10000+i%10000*100;
				f[3]=j;
				if (j!=f[0] && j!=f[1] && j!=f[2] && j>i && j<=b)ans++;
				j=i/100000+i%100000*10;
				f[4]=j;
				if (j!=f[0] && j!=f[1] && j!=f[2] && j!=f[3] && j>i && j<=b)ans++;
			}
			else if (i>9999)
			{
				j=i/10+i%10*10000;
				f[0]=j;
				if (j>i && j<=b)ans++;
				j=i/100+i%100*1000;
				f[1]=j;
				if (j!=f[0] && j>i && j<=b)ans++;
				j=i/1000+i%1000*100;
				f[2]=j;
				if (j!=f[0] && j!=f[1] && j>i && j<=b)ans++;
				j=i/10000+i%10000*10;
				f[3]=j;
				if (j!=f[0] && j!=f[1] && j!=f[2] && j>i && j<=b)ans++;
			}
			else if (i>999)
			{
				j=i/10+i%10*1000;
				f[0]=j;
				if (j>i && j<=b)ans++;
				j=i/100+i%100*100;
				f[1]=j;
				if (j!=f[0] && j>i && j<=b)ans++;
				j=i/1000+i%1000*10;
				f[2]=j;
				if (j!=f[0] && j!=f[1] && j>i && j<=b)ans++;
			}
			else if (i>99)
			{
				j=i/10+i%10*100;
				f[0]=j;
				if (j>i && j<=b)ans++;
				j=i/100+i%100*10;
				f[1]=j;
				if (j!=f[0] && j>i && j<=b)ans++;
			}
			else if (i>9)
			{
				j=i/10+i%10*10;
				if (j>i && j<=b)ans++;
			}
		}
		printf("Case #%d: %d\n",id,ans);
	}
	return 0;
}