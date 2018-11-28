#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int teste, tst, s;
long long n, j, i, pt[100], d[100005], ind, rsp, nr;
char sir[100];

int main()
{
	freopen("ab.in", "rt", stdin);
	freopen("ab.out", "wt", stdout);

	scanf("%d\n", &teste);
	for (tst = 1; tst <= teste; tst ++){
		scanf("%s\n", sir+1);

		rsp = 1000000000000000000LL;
		for (j = 2; j <= 10; j ++){
			n = strlen(sir+1);

			pt[0] = 1;
			for (i = 1; i <= n; i ++)
				pt[i] = j * pt[i-1];

			memset(d, 0xff, sizeof(d)); ind = 0; s = 0; nr = 0;
			d[ sir[1] ] = 1;

			for (i = 1; i <= n; i ++){
				if (d[ sir[i] ] == -1){
					d[ sir[i] ] = ind;
					ind ++; if (ind == 1) ind = 2;
					if (ind > j){
						s = 1;
						break;
					}
				}
				nr = nr + d[ sir[i] ] * pt[n - i];
			}

			if (!s)
				rsp = min(rsp, nr);
		}

		printf("Case #%d: %lld\n", tst, rsp);
	}

	return 0;
}

