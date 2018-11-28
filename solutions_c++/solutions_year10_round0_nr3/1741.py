#include <stdio.h>
#include <memory.h>
#include <string.h>

#define big __int64

big g[1000+100];

struct NODE
{
	int ind;
	big val;
	big sum;
} flag[1001];


int main()
{
	int T;
	big tot;
	int first,second;
	int ind;
	int i;
	int loop;
	big loopval;

	freopen("C-large.in","r",stdin);
	freopen("c.out","w",stdout);

	scanf("%d",&T);
	for (int tcase = 1; tcase <= T; tcase ++) {
		printf("Case #%d: ",tcase);
		int r,k,n;
		tot = 0;
		scanf("%d%d%d",&r,&k,&n);
		for (i = 0; i < n; i ++) {
			scanf("%I64d",&g[i]);
		}
		memset(flag,-1,sizeof(flag));
		
		i = 0;
		tot = 0;
		ind = 0;
		
		while (1) {
			big sum = 0;
			int j = i;
			if (flag[i].val == -1) {
				while (sum + g[i] <= k) {
					sum += g[i];
					i ++;
					i = i % n;
					if (i == j) break;
				}
				tot = tot + sum;
				flag[j].val = tot;
				flag[j].ind = ind;
				flag[j].sum = sum;
			} else {
				loop = ind - flag[i].ind;
				loopval = tot - flag[i].val + flag[i].sum;
				break;
			}
			ind ++;
		}

	//	printf("ans %I64d\n",ans);


		int start = flag[i].ind;
		int starti = i;

	//	printf("st %d\n",start);


		int lef = (r - start) % loop;
		big ans = (big)loopval * (big)( (r - start) / loop);
	//	printf("ans %I64d\n",ans);
		int times = 0;
		i = 0;
		while (times < start) {
			big sum = 0;
			int j = i;
			while (sum + g[i] <= k) {
				sum += g[i];
				i ++;
				i = i % n;
				if (i == j) break;
				
			}ans += sum;
			times ++;
		}
	//	printf("ans %I64d\n",ans);

	//	printf("lef %d\n",lef);


		i = starti;
		times = 0;

		while (times < lef) {
			big sum = 0;
			int j = i;
			while (sum + g[i] <= k) {
				sum += g[i];
				i ++;
				i = i % n;
			//	printf("sum : %d %d\n",sum);
				if (i == j) break;
				
			}ans += sum;
			times ++;
		}
	//	printf("loop : %d %d\n",loop,loopval);
		printf("%I64d\n",ans);

	}





	return 0;
}
