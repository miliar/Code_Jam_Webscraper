#include<stdio.h>
#include<algorithm>
using namespace std;
typedef __int64 int64;

int C, N, cas;
int64 t[1009];

int64 GCD(int64 x, int64 y)
{
	if (x > y) return GCD(y, x);
	if (x == 0) return y;
	else return GCD(y % x, x);

}

int main()
{
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-small-attempt2.out", "w", stdout);
	int i;
	int64 gcd, ans, tmp;
	scanf("%d", &C);
	for (cas = 1; cas <= C; cas ++){
		scanf("%d", &N);
		for (i=0; i<N; i++)
			scanf("%I64d", &t[i]);
		sort(t, t+N);

		gcd = t[1]-t[0];

		if (N==3){
			gcd = GCD(t[2]-t[0], gcd);
			gcd = GCD(t[2]-t[1], gcd);
		}
		//ans = gcd - t[0] % gcd;
		ans = 0;
		for (i=0; i<N; i++){
			tmp = gcd - t[i] % gcd;
//			printf("t[%d] = %I64d, tmp = %I64d, gcd = %I64d\n",i, t[i], tmp, gcd);
			if (tmp == gcd) tmp = 0;
			if (tmp > ans) ans = tmp;
		}
		printf("Case #%d: %I64d\n", cas, ans);
	}
	return 0;
}