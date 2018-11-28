#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<list>
#include<algorithm>
using namespace std;

int csK, csN, N, last[64], ans;

int main()
{
	int i, j, k, m, t;
	char str[64];
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d", &N);
		for(i = 1; i <= N; ++i)
		{
			scanf("%s", str+1);
			for(j = N; j >= 1; --j)
				if(str[j] == '1') break;
			last[i] = j;
		}
		ans = 0;
		for(i = 1; i <= N; ++i)
		{
			for(j = i; j <= N; ++j)
				if(last[j] <= i) break;
			for(; j > i; --j, ++ans)
			{
				t = last[j];
				last[j] = last[j-1];
				last[j-1] = t;
			}
		}
		printf("Case #%d: %d\n", csK, ans);
	}
}
