#include <stdio.h>
#include <math.h>

int main()
{
//	freopen("A-small.in","r",stdin);

	freopen("A-large.in","r",stdin);
	freopen("A-small.out","w",stdout);

	int T;
	scanf("%d",&T);
	for (int tcase = 1; tcase <= T; tcase ++) {
		int n,k;
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",tcase);
		if ( (k+1) % (int)pow(2,n) == 0) {
			printf("ON\n");
		} else {
			printf("OFF\n");
		}
	}
	return 0;
}

