#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

const int MAXN=1005;

int N;
int rank[MAXN];
int a[MAXN];
pair<int,int> b[MAXN];
bool used[MAXN];

int find(int i)
{
	int ans=0;
	do
	{
		used[i]=true;
		ans++;
		i=rank[i];
	}while(!used[i]);
	return ans;
}

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int kk=1;kk<=T;kk++)
	{
		scanf("%d",&N);
		for(int i=0;i<N;i++)
		{
			scanf("%d",&a[i]);
			b[i].first=a[i],b[i].second=i;
		}
		sort(b,b+N);
		for(int i=0;i<N;i++)
			rank[b[i].second]=i;
		double re=0;
		memset(used,false,sizeof(used));
		for(int i=0;i<N;i++)
			if (rank[i]!=i && !used[i])
				re+=find(i);
		printf("Case #%d: %.6lf\n",kk,re);
	}
	return 0;
}
