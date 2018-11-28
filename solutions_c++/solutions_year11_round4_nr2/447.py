#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

#define MAXN 510

int n,m;
int d;
unsigned w[MAXN][MAXN];

unsigned sum[MAXN][MAXN];
pair<unsigned,unsigned> wctr[MAXN][MAXN];

pair<unsigned,unsigned> operator +(pair<unsigned,unsigned> a,pair<unsigned,unsigned> b)
{
	return make_pair(a.first+b.first,a.second+b.second);
}

pair<unsigned,unsigned> operator -(pair<unsigned,unsigned> a,pair<unsigned,unsigned> b)
{
	return make_pair(a.first-b.first,a.second-b.second);
}

int ans;

pair<unsigned,unsigned> cell_center(unsigned i,unsigned j)
{
	return make_pair((i*2+1)*w[i][j],(j*2+1)*w[i][j]);
}

bool solve(unsigned len)
{
	for (int i=0;i+len<=n;i++)
		for (int j=0;j+len<=m;j++)
		{
			pair<unsigned,unsigned> cur=wctr[i+len][j+len]-wctr[i][j+len]-wctr[i+len][j]+wctr[i][j];
			cur=cur-cell_center(i,j);
			cur=cur-cell_center(i+len-1,j);
			cur=cur-cell_center(i,j+len-1);
			cur=cur-cell_center(i+len-1,j+len-1);
			unsigned weight=sum[i+len][j+len]-sum[i][j+len]-sum[i+len][j]+sum[i][j];
			weight-=w[i][j]+w[i+len-1][j]+w[i][j+len-1]+w[i+len-1][j+len-1];
			if (cur.first==weight*(i*2+len) && cur.second==weight*(j*2+len))
			{
//				cerr<<i<<' '<<j<<' '<<len<<endl;
				return true;
			}
		}
	return false;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int caseN;
	scanf("%d",&caseN);
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		scanf("%d%d%d",&n,&m,&d);
		memset(sum,0,sizeof(sum));
		memset(wctr,0,sizeof(wctr));
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
			{
				scanf("%1u",&w[i][j]);
				sum[i+1][j+1]=sum[i][j+1]+sum[i+1][j]-sum[i][j]+w[i][j];
				wctr[i+1][j+1]=wctr[i][j+1]+wctr[i+1][j]-wctr[i][j]+cell_center(i,j);
			}
		ans=0;
		for (int k=min(n,m);k>=3;k--)
			if (solve(k))
			{
				ans=k;
				break;
			}
		printf("Case #%d: ",caseI);
		if (ans)
			printf("%d\n",ans);
		else
			printf("IMPOSSIBLE\n");
	}
}
