
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define MAX 1024

int mrc[MAX];
int g[MAX];

long long sum[MAX];

int main(void)
{
	int nc;
	int r, k, n;
	int i, j, p;
	long long at, res;
	int tot;

	scanf("%d", &nc);
	for(int ca=1; ca<=nc; ca++)
	{
		printf("Case #%d: ", ca);

		scanf("%d %d %d", &r, &k, &n);

		tot = 0;
		for(i=0; i<n; i++)
		{
			scanf("%d", &g[i]);
			tot += g[i];
		}
		if(tot <= k)
		{
			printf("%d\n", (long long)(r)*tot);
			continue;
		}

		memset(mrc, -1, sizeof(mrc));
		memset(sum, 0, sizeof(sum));

		p = 0;
		for(i=0; i<r; i++)
		{
			if(mrc[p] != -1) break;
			mrc[p] = i;

			at = 0;
			while(at+g[p] <= k)
			{
//				printf("  sobe %d\n", g[p]);

				at += g[p];
				p = (p+1) % n;
			}
			sum[i+1] = sum[i] + at;

//			printf("i=%d somei %d\n", i, at);
		}

		int com = mrc[p];
		int passos = i - com;
		int pulos = (r-i)/passos;

//		printf("i=%d, %d passos vezes %d = %d\n", i, passos, pulos, passos*pulos);

		res = sum[i] + (sum[i]-sum[com])*pulos;

		for(i += passos*pulos; i<r; i++)
		{
			at = 0;
			while(at+g[p] <= k)
			{
//				printf("  sobe %d\n", g[p]);

				at += g[p];
				p = (p+1) % n;
			}
			res += at;

//			printf("i=%d somei %d\n", i, at);
		}

		printf("%d\n", res);
	}

	return 0;
}
