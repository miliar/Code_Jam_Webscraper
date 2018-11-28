#include <stdio.h>
#include <algorithm>
using namespace std;


int main(void)
{
	int T;
	scanf("%d", &T);
	int tc = 0;
	while (T--) {
		tc++;
		int n, k;
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", tc);
		if ((k & ((1 << n)-1)) == ((1 << n) - 1)) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
