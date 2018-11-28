#include <cstdio>
#include <string>

int a[5001], n, K;
bool use[5001];

void solve()
{
	int i,j=1,k;
	
	memset(a, 0, sizeof(a));
	for(i=1;i<=n;++i)
	{
		for(k=1;k<=i;++k)
		{
			while(a[j]) { ++j; if(j>n) j=1;}
			if(k==i) a[j]=k;
			++j;
			if(j>n) j=1;
		}
		
	}
	//for(i=1;i<=n;++i) printf("%d ", a[i]);
}

int main()
{

	freopen("date.in","r",stdin);
	freopen("date.out","w",stdout);
	int T,i,p;
	scanf("%d\n", &T);
	
	for(int t=1;t<=T;++t)
	{
		scanf("%d\n", &n);
	
		solve();
		
		scanf("%d ", &K);
		//printf("%d\n", K);
		printf("Case #%d: ", t);
		for(i=1;i<=K;++i)
		{
			scanf("%d ", &p);
			printf("%d ", a[p]);
		}
		printf("\n");
	}
		
	return 0;
}
