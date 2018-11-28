#include <cstdio>
#include <algorithm>
using namespace std;

int T, N;
int dis[10000], len[10000];
int most[10000];
int end;
bool ans;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);

	scanf("%d", &T);
	for(int cnt=1; cnt<=T; ++cnt)
	{
		scanf("%d", &N);
		for(int i=0; i<N; ++i) scanf("%d %d", &dis[i], &len[i]);
		scanf("%d", &end);

		for(int i=1; i<N; ++i) most[i] = 0;
		most[0] = min(dis[0], len[0]);
		ans = 0;
		for(int i=0; i<N; ++i)
		{
			if(dis[i]+most[i]>=end)
			{
				ans = 1;
				break;
			}
			for(int j=i+1; j<N; ++j)
			{
				if(dis[j]-dis[i]>most[i]) break;
				most[j] = max(most[j], min(len[j], dis[j]-dis[i]));
			}
		}
		printf("Case #%d: %s\n", cnt, (ans?"YES":"NO"));
	}
	return 0;
}
