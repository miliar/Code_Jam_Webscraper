#include<cstdio>

int main(void)
{
	int T;
	scanf("%d",&T);

	for(int t=1; t<=T; t++) {

		int n, k;
		scanf("%d %d",&n, &k);
		int m = (1 << n) - 1;

		bool result = (k % (1 << n)) == m;


		printf("Case #%d: %s\n", t, result ? "ON" : "OFF");

	}
	return 0;

}

