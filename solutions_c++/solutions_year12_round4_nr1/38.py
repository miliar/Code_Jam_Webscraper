#include<cstdio>
#include<algorithm>
using namespace std;

int n,k;
pair<int,int> A[10010];
int ans[10010];

bool prog()
{
	for(int c=0;c<10010;c++) ans[c] = -1;
	scanf("%d",&n);
	for(int c=1;c<=n;c++) scanf("%d%d",&A[c].first,&A[c].second);
	scanf("%d",&k);
	ans[1] = 2*A[1].first;
	int p = false, mm = ans[1];
	for(int c=2;c<=n;c++)
	{
		int z = -1;
		for(int d=1;d<c;d++) if( ans[d] >= A[c].first )
		{
			z = max( z , A[c].first + min( A[c].second , A[c].first - A[d].first ) );
		}
		ans[c] = z;
		mm = max( mm , ans[c] );
	}
	//for(int c=1;c<=n;c++) printf("%d ",ans[c]); printf("\n");
	return mm >= k;
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("sol1.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		printf("Case #%d: ",c);
		if( prog() ) printf("YES\n");
		else printf("NO\n");
	}
}
