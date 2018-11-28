#include <cstdio>

int main() {

	int t,s,n,p,x,res;

	scanf("%d",&t);

	for (int i = 0; i < t; ++i) {
		scanf("%d %d %d",&n,&s,&p);

		res = 0;

		for (int j = 0; j < n; ++j) {
			scanf("%d",&x);

			if (x-p < 0)
				continue;

			if ((x-p)/2 >= p-1)
				res++;
			else if ((x-p)/2 >= p-2 && s) {
				res++;
				s--;
			}
		}

		printf("Case #%d: %d",i+1, res);
		if (i != t-1)
			putchar('\n');

	}

	return 0;
}

