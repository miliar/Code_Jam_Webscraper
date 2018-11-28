#include <cstdio>
#include <cstring>

const int MAXN=2000000;
int deg[8]={1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};
bool was[MAXN+1]={0};
int main()
{
	int T, t, A, B, n, m, len, i;
	int q, r;
	int seq[7];
	int ans;
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for(t=1; t<=T; ++t)
	{
		scanf("%d%d", &A, &B);
		ans=0;
		for(n=A; n<B; ++n)
		{
			for(len=1; deg[len]<=n; ++len);
			for(i=1; i<len; ++i)
			{
				q=n/deg[i], r=n-q*deg[i];
				m=r*deg[len-i]+q;	
				if(r>=deg[i-1] && n<m && m<=B)
				{
					ans+=(!was[m]);
					was[m]=true;
				}
				seq[i]=m;
			}
			for(i=1; i<len; ++i)
				if(0<=seq[i] && seq[i]<=MAXN)
					was[seq[i]]=false;
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
