#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
using namespace std;

const int MAXN=2000;

struct Go
{
	int total_groups;
	long long money;
} g[MAXN];
int a[MAXN];
int N,R,K,T;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for (int test=1;test<=T;++test)
	{
		scanf("%d%d%d",&R,&K,&N);
		for (int i=0;i<N;i++)
			scanf("%d",&a[i]);

		for (int i=0;i<N;i++)
		{
			g[i].total_groups=0;
			g[i].money=0;
			while (true)
			{
				if (a[(i+g[i].total_groups)%N]+g[i].money <= K)
				{
					g[i].money+=a[(i+g[i].total_groups)%N];
					++g[i].total_groups;
					if (g[i].total_groups==N)
						break;
				} else
					break;
			}
		}

		long long res=0;
		int cur=0;
		for (int i=0;i<R;i++)
		{
			res=res+g[cur].money;
			cur=cur+g[cur].total_groups;
			if (cur>=N)
				cur-=N;
		}

		printf("Case #%d: %lld\n",test,res);
	}
	return 0;
}