#include <cstdio>
using namespace std;

int main()
{
	freopen("data.in", "r", stdin);
	freopen("result.out", "w", stdout);

	int curt, tn;
	scanf("%d", &tn);
	for(curt = 1; curt <= tn; ++curt) {
		int n, k;
		printf("Case #%d: ", curt);
		scanf("%d %d", &n, &k);
		int base = 1 << n;

		k = k % base;
		if(k == (base-1)) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}