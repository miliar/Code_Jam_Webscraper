#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN=10005;

struct Node
{
	int d,l;
	bool operator < (const Node &b) const
	{
		return d<b.d;
	}
}all[MAXN];

int f[MAXN],N,D;

bool solve()
{
	scanf("%d",&N);
	for(int i=0;i<N;i++)
		scanf("%d%d",&all[i].d,&all[i].l);
	sort(all,all+N);
	scanf("%d",&D);
	for(int i=0;i<N;i++)
		f[i]=0;
	f[0]=min(all[0].l,all[0].d);
	for(int i=0;i<N;i++)
	{
		int reach=all[i].d+f[i];
		if (reach>=D)
			return true;
		for(int j=i+1;j<N;j++)
			if (reach>=all[j].d)
			{
				int nf=min(all[j].l,all[j].d-all[i].d);
				if (nf>f[j])
					f[j]=nf;
				if (all[j].d+f[j]>=D)
					return true;
			}
			else
				break;
	}
	return false;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		if (solve())
			printf("Case #%d: YES\n",i);
		else
			printf("Case #%d: NO\n",i);
	}
	return 0;
}