#include <stdio.h>
#include <string>
#include <map>
#include <vector>
#define maxn 52
using namespace std;

struct chick{
	int xi;
	int vi;
	bool canArr;
}chicks[maxn];

int C, c = 1;
int n, k, b, t;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	for(scanf("%d", &C); C; --C)
	{
		scanf("%d%d%d%d", &n, &k, &b, &t);

		for(int i = 0; i < n; ++i)
		{
			scanf("%d", &chicks[i].xi);
		}
		for(int i = 0; i < n; ++i)
		{
			scanf("%d", &chicks[i].vi);
		}

		int ans = 0, cannotNum = 0;

		for(int i = n - 1; i >= 0 && k; --i)
		{
			if(chicks[i].vi * t + chicks[i].xi >= b)
			{
				chicks[i].canArr = true;
				--k;
				ans += cannotNum;
			}else
			{
				chicks[i].canArr = false;
				++cannotNum;
			}
		}
		
		if(k)
			printf("Case #%d: IMPOSSIBLE\n", c++);
		else
			printf("Case #%d: %d\n", c++, ans);
			
	}
}