#include<stdio.h>
#include<string.h>
#include<math.h>
#include<string>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
#include<string>

using namespace std;

const int inf = 2147483647;
const double eps = 1e-8;
const double pi = acos(-1.0);

const int maxn = 120;
const int maxq = 100005;

long long L;
int N,a[maxn],mod,begin,end;
int dist[maxq],Q[maxq];
bool inQ[maxq];

void spfa()
{
	for(int i=0;i<mod;i++) dist[i] = -1;
	dist[0] = 0; begin = end = 0; Q[end++] = 0; inQ[0] = true;
	while(begin!=end)
	{
		int x = Q[begin++]; if(begin==maxq) begin = 0;
		inQ[x] = false;
		for(int i=0;i<N-1;i++)
		{
			int y = x + a[i];
			if(y>=mod)
			{
				if(dist[y-mod]==-1 || dist[y-mod]>dist[x])
				{
					dist[y-mod] = dist[x];
					if(!inQ[y-mod])
					{
						inQ[y-mod] = true;
						Q[end++] = y-mod;
						if(end==maxq) end = 0;
					}
				}
			}
			else
			{
				if(dist[y]==-1 || dist[y]>dist[x]+1)
				{
					dist[y] = dist[x] + 1;
					if(!inQ[y])
					{
						inQ[y] = true;
						Q[end++] = y;
						if(end==maxq) end = 0;
					}
				}
			}
		}
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int ntest;
	scanf("%d",&ntest);
	for(int test=1;test<=ntest;test++)
	{
		fprintf(stderr,"%d\n",test);
		scanf("%I64d%d",&L,&N);
		for(int i=0;i<N;i++)
		{
			scanf("%d",&a[i]);
		}
		sort(a,a+N); mod = a[N-1];
		spfa();
		printf("Case #%d: ",test);
		if(dist[L%mod]==-1) printf("IMPOSSIBLE\n");
		else printf("%I64d\n",dist[L%mod] + L/mod);
	}
	return 0;
}
