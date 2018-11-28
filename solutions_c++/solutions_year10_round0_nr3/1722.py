#include<cstdio>

const int maxn=1000+10;
int next[maxn];
int s[maxn*2];
int n,m,limit;
int t,cases;

int main()
{
	for (scanf("%d",&t);t--;)
	{
		scanf("%d%d%d",&m,&limit,&n);
		for (int i=1;i<=n;i++) scanf("%d",&s[i]),s[i+n]=s[i];
		for (int i=1;i<=n+n;i++) s[i]+=s[i-1];

		for (int i=1;i<=n;i++)
		for (int j=i;j<=n*2;j++)
		if (s[j+1]-s[i-1]>limit || j-i+1==n)
		{
			next[i]=j;
			break;
		}

		long long res=0;
		for (int i=0,k=1;i<m;i++)
		{
			int j=next[k];
			res+=s[j]-s[k-1];
			k=next[k]+1;
			while (k>n) k-=n;
		}
		printf("Case #%d: %lld\n",++cases,res);
	}
}
