#include<cstdio>
using namespace std;

int main() {
	int i, T;
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	scanf("%d\n", &T);

	for (i = 0; i < T; i++) {
		int sum = 0;
		int min = 1000001;
		int n, x, j;
		int xor = 0;
		scanf("%d\n", &n);
		for (j = 0; j < n; j++)	{
			scanf("%d", &x);
			sum+=x;
			xor ^= x;
			if (min > x) min = x;
		}
		if (xor == 0) printf("Case #%d: %d\n",i+1, sum-min );
		else printf("Case #%d: NO\n",i+1);
	}
	return 0;
}