#include<cstdio>
#include<cstring>

#define maxx(a,b) ((a)>(b)?(a):(b))

const int mx=2060;

int n,p;
int m[mx];
int g[mx];

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("outB2.txt","w",stdout);
	int i,t,ca=1;
	scanf("%d",&t);
	while(t--)
	{
		memset(m,0,sizeof(m));
		memset(g,0,sizeof(g));
		scanf("%d",&p);
		n=1<<p;
		int c=n-1;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&m[c+i]);
			m[c+i]=p-m[c+i];
		}
		for(i=1;i<n;i++)
			scanf("%d",&m[mx-1]);
		for(i=n-1;i>0;i--)
			m[i]=maxx(m[i*2],m[i*2+1]);

		int cnt=0;
		for(i=1;i<2*n;i++)
		{
			g[i]=g[i/2];
			m[i]-=g[i];
			if(m[i]>0)
			{
				cnt++;
				g[i]++;
			}
		}
		printf("Case #%d: %d\n",ca++,cnt);
	}

	return 0;
}

