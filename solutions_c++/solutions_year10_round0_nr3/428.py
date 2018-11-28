#include<iostream>

using namespace std;

long long g[10000000];
long long s[10000001];
long long a[10000000];
int next[10000000];
int been[10000000];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++)
	{
		long long r,k,n;
		scanf("%I64d%I64d%I64d",&r,&k,&n);
		s[0]=0;
		for(int i=0;i<n;i++)
		{
			scanf("%I64d",&g[i]);
			s[i+1] = s[i] + g[i];
		}
		if (k>=s[n])
		{
			long long ans = s[n]*r;
			printf("Case #%d: %I64d\n",tt,ans);
			continue;
		}

		long long sum = 0;
		int i;
		for(i=0;i<n;i++)
		{
			if (sum+g[i]>k) break;
			sum+=g[i];
		}

		next[0] = i;
		sum-=g[0];
		for(int j=1;j<n;j++)
		{
			for(;sum+g[i]<=k;i=(i+1)%n)
			{
				sum+=g[i];
			}
			next[j] = i;
			sum-=g[j];
		}

		memset(been,0,sizeof(int)*(int)n);
		memset(a,0,sizeof(long long)*(int)n);

		long long ans = 0;

		int pos = 0,cnt = 0;
		
		while(r&&!been[pos])
		{
			--r;
			been[pos]=++cnt;
			int npos = next[pos];
			if (pos<npos) ans+=s[npos]-s[pos];
			else ans+=s[n]+s[npos]-s[pos];
			pos = npos;
			if (!been[pos])a[pos]=ans;
		}

		if (r==0)
		{
			printf("Case #%d: %I64d\n",tt,ans);
			continue;
		}
		
		

		ans += r/(cnt-been[pos]+1)*(ans-a[pos]);
		r%=cnt-been[pos]+1;

		while(r)
		{
			--r;
			int npos = next[pos];
			if (pos<npos) ans+=s[npos]-s[pos];
			else ans+=s[n]+s[npos]-s[pos];
			pos = npos;
		}
			
		printf("Case #%d: %I64d\n",tt,ans);
	}
	return 0;
}
