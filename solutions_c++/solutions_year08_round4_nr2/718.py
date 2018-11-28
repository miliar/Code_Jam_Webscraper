#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int nTC;
	scanf("%d", &nTC);
	for (int kasus=1; kasus<=nTC; kasus++) {
		int hasil;
		int nrows, ncols;
		int A;
		scanf("%d %d %d", &ncols, &nrows, &A);
		bool finish=false;
		for (int j=0; j<=nrows; j++) {
			for (int k=0; k<=ncols; k++) {
				for (int l=0; l<=nrows; l++) {
					for (int m=0; m<=ncols; m++) {
						if (abs(j*m-k*l)==A) {
							printf("Case #%d: 0 0 %d %d %d %d\n", kasus, k, j, m, l);
							finish=true;
							break;
						}
					}
					if (finish) break;
				}
				if (finish) break;
			}
			if (finish) break;
		}
		if (!finish)
		printf("Case #%d: IMPOSSIBLE\n", kasus);
	}
	return 0;
}
