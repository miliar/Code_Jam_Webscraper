#include<cstdio>
#include<algorithm>
using namespace std;

struct p_tag {
	int name;
	int r;
} A[1010];
int n;
int W,L;
pair<int,int> ans[1010];

bool cmp( p_tag a , p_tag b )
{
	return a.r > b.r;
}

void prog()
{
	scanf("%d%d%d",&n,&L,&W);
	for(int c=1;c<=n;c++)
	{
		scanf("%d",&A[c].r);
		A[c].name = c;
	}
	sort( A+1 , A+n+1 , cmp );
	int nowy = -A[1].r;
	for(int c=1;c<=n;c++)
	{
		nowy += A[c].r;
		int nowx = -A[c].r;
		int ny = nowy + A[c].r;
		for(;c<=n and nowx+A[c].r <= W;c++)
		{
			nowx += A[c].r;
			ans[A[c].name] = pair<int,int>( nowy , nowx );
			nowx += A[c].r;
		}
		c --;
		nowy = ny;
	}
	for(int c=1;c<=n;c++) printf("%d %d ",ans[c].first,ans[c].second);
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
		prog();
		printf("\n");
	}
}
