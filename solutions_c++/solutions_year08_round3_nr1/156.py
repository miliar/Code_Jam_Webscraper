#include <stdio.h>
#include <algorithm>
using namespace std;
int main()
{
	int nt, np, nk, nl, freq, kleft;
	long long ans;
	int array[1005];
	scanf("%d", &nt);
	for (int it = 1; it <= nt; it++) {
		scanf("%d %d %d", &np, &nk, &nl);
		for (int i = 0; i < nl; i++) {
			scanf("%d", &array[i]);
		}
		if (np * nk < nl) {
			printf("Case #%d: Impossible\n", it);
			continue;
		}		
		sort(array, array + nl);
		kleft = nk;
		freq = 1;
		ans = 0;
		for (int i = nl - 1; i >= 0; i--) {
			ans += freq * array[i];
			kleft--;
			if (kleft == 0) {
				kleft = nk;
				freq++;
			}
		}
		printf("Case #%d: %lld\n", it, ans);
	}
	return 0;
}
