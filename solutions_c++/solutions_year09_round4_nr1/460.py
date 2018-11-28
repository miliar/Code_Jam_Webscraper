#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int V[50];

int main() {
	int T;
	scanf(" %d", &T);
	for (int _42=1; _42 <= T; _42++) {
		int ans=0;
		int N;
		scanf(" %d", &N);
		for (int i=0; i < N; i++) {
			char buf[1000];
			scanf(" %s", buf);
			int rightmost=0;
			for (int j=strlen(buf)-1; j >= 0; j--) {
				if (buf[j] == '1') {
					rightmost = j;
					break;
				}
			}
			V[i] = rightmost;
//			printf("-> %d\n", rightmost);
		}

		for (int i=0; i < N; i++) {
//			for (int ii=0; ii < N; ii++) printf("%d ", V[ii]); printf("\n");
			if (V[i] <= i) continue;

			for (int j=i; j < N; j++) {
				if (V[j] <= i) {
					for (int k=j-1; k >= i; k--) {
						swap(V[k], V[k+1]);
						ans++;
					}
					break;
				}
			}
		}
		printf("Case #%d: %d\n", _42, ans);
	}


	return 0;
}
