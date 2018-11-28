#include <cstdio>
#include <vector>
#define fi first
#define se second
#define pb push_back
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pi;
int t[5003];
int d[5003];
int main()
{
	int N;
	scanf("%d",&N);
	for (int u=1; u<=N; u++)
	{
		int n,m;
		scanf("%d %d",&n,&m);
		for (int i=0; i<n; i++)
		{
			t[i]=0;
			d[i]=(i+1)%n;
		}
		t[0]=1;
		d[n-1]=1;
		int k=0,l=0;
		for (int i=2; i<=n; i++)
		{
			for (int j=0; j<i; j++)
			{
				l=k;
				k=d[k];
			}
			t[k]=i;
			d[l]=d[k];
		}
		printf("Case #%d:",u);
		for (int i=0; i<m; i++)
		{
			int a;
			scanf("%d",&a);
			printf(" %d",t[a-1]);
		}
		printf("\n");
	}
}
