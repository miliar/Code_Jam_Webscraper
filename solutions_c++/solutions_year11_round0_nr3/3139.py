#include <stdio.h>
#include <string.h>

long long solve()
{
	int n;
	long long ret = -1;
	long long total = 0, allnot = 0,  t, min = 10000000;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		scanf("%lld", &t);
		total += t;
		allnot ^= t;
		if(min > t) min = t;
	}
	return (allnot != 0)?-1:total - min;
}

int main(int argc, char **argv)
{
	int ncase;

	freopen("C-large.in", "r", stdin);
	freopen("c_big_out.txt", "w", stdout);
	
	scanf("%d", &ncase);
	for(int icase = 0; icase < ncase; icase++)
	{
		long long ans;
		printf("Case #%d: ", icase+1);
		ans = solve();
		if(ans <= 0)
		{
			printf("NO");
		}
		else
		{
			printf("%lld", ans);
		}
		printf("\n");
	}	
		
	return 0;
}
