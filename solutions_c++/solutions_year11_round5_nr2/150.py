#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

const int INF=2100000000;
int T,n;
int a[1005];
vector<int> V[1005];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		int ans=INF;
		int cnt=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%d",&a[i]);
		sort(a,a+n);
		for(int j=0;j<n;j++)
		{
			int MIN=INF;
			for(int i=0;i<cnt;i++)
				if(V[i].back()==a[j]-1)
					if(MIN==INF||V[i].size()<V[MIN].size())
						MIN=i;
			if(MIN==INF)
				V[cnt++].push_back(a[j]);
			else
				V[MIN].push_back(a[j]);
		}
		for(int i=0;i<cnt;i++)
			ans=min(ans,(int)V[i].size());
		printf("Case #%d: %d\n",test,n==0?n:ans);
		for(int i=0;i<cnt;i++)
			V[i].clear();
	}
	return 0;
}

