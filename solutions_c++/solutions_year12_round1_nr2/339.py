#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1000+5;

int A[MAXN];
int B[MAXN];

void solve() {
	int n;
	scanf("%d", &n);

	for(int i = 0; i < n; i++) {
		scanf("%d %d", &A[i], &B[i]);

	}

	int res = 0;
	int curr = 0;

	while(n > 0) {
		int best = -1;

		for(int i = 0; i < n; i++) {
			if(B[i] <= curr) {
				best = i;
				break;
			} else if (A[i] != -1 && A[i] <= curr) {
				if(best == -1 || B[i] > B[best]) best = i;
			}
		}

		if(best == -1) {
			printf("Too Bad");
			return;
		}

		res++;

		if(B[best] <= curr) {
			n--;
			curr+= (A[best] == -1) ? 1 : 2;
			swap(A[best], A[n]);
			swap(B[best], B[n]);
			
		} else {
			A[best] = -1;
			curr++;
		}

	}

	printf("%d", res);

}

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
		printf("\n");
	}

}