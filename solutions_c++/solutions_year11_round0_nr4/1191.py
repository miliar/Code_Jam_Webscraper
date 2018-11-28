
#include "cstdio"
#include "cmath"


int main(int argc, char *argv[]) {
  freopen(argv[1], "r", stdin);

	int tn;
	scanf("%d", &tn);

	for (int ti = 1; ti <= tn; ti++) {

		//read
		int n;
		scanf("%d", &n);

		int data[2000];
		int bad = 0;
		for (int i = 1; i <= n; i++) {
			scanf("%d", &data[i]);
			if (i != data[i]) bad++;
		}


		printf("Case #%d: %d.000000\n", ti, bad);

	}


	return 0;
}






