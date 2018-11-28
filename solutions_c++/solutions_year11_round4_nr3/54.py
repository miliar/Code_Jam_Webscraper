#include <stdio.h>
#include <memory.h>
#include <algorithm>
#define MX 1000001
#define ll long long
using namespace std;
ll n, i, j, k;
int r;
int npr[MX];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tt, T;

	memset(npr,0,sizeof(npr));
	for (i = 2; i < MX; i++) {
		if (!npr[i]) {
			for (j = i*2; j < MX; j += i)
				npr[j] = 1;
		}
	}
	scanf("%d",&T);
	for (tt = 1; tt <= T; tt++) {
		printf("Case #%d: ",tt);
		scanf("%lld",&n);
		if (n == 1) {
			printf("0\n");
			continue;
		}
		r = 1;
		for (i = 2; i*i <= n; i++) {
			if (npr[i]) continue;
			for (k = i; k <= n; k *= i)
				r++;
			r--;
		}
		printf("%d\n",r);
	}
	return 0;
}