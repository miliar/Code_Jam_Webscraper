#include<stdio.h>
#include<algorithm>

using namespace std;

#define lg 100000

int teste, tst, p, q, i, v[lg], poz[lg], d[lg], cost, vf, pt[100], j, k;

int main()
{
	freopen("ab.in", "rt", stdin);
	freopen("ab.out", "wt", stdout);

	pt[1] = 1;
	for (i = 2; i <= 10; i ++)
		pt[i] = 2*pt[i-1];

	scanf("%d", &teste);
	for (tst = 1; tst <= teste; tst ++){
		memset(poz, 0, sizeof(poz));

		scanf("%d%d", &p, &q);
		for (i = 1; i <= q; i ++){
			scanf("%d", &v[i]);
			poz[ v[i] ] = i;
		}

		memset(d, 0x3f, sizeof(d));
		d[0] = 0;

		for (i = 0; i < (1 << q) - 1; i ++){
			for (j = 1; j <= q; j ++)
				if (!(i & pt[j])){
					vf = v[j]; cost = 0;

					for (k = vf+1; k <= p; k ++)
						if (poz[k] > 0){
							if ((pt[ poz[k] ] & i) > 0)
								break;
							else
								cost ++;
						}
						else
							cost ++;
					for (k = vf-1; k; k --)
						if (poz[k] > 0)
							if ((pt[ poz[k] ] & i) > 0)
								break;
							else
								cost ++;
						else
							cost ++;
		

					d[i | pt[j]] = min(d[i | pt[j]], d[i] + cost);
				}
		}

		printf("Case #%d: %d\n", tst, d[(1 << q) - 1]);
	}

	return 0;
}

