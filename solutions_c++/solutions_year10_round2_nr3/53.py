#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int mod = 100003;
int C[600][600];
int D[600][600];

int main() {
	C[0][0]=1;
	for(int i=1; i<600; i++) {
		C[i][0] = 1;
		for(int j=1; j<600; j++) {
			C[i][j] = (C[i-1][j-1] + C[i-1][j]) % mod;
		}
	}
	//for(int i=0; i<20; i++) {for(int j=0; j<20; j++) printf(" %d", C[i][j]); puts(""); }

	for(int i=0; i<600; i++) D[i][1] = 1;
	for(int n=2; n<600; n++) {
		for(int k=2; k<n; k++) {
			for(int x=1; x<k; x++) {
				D[n][k] += (D[k][x] * (1LL * C[n-k-1][k-x-1])) % mod;
				D[n][k] %= mod;
			}
		}
	}

	int tcase;
	scanf("%d", &tcase);
	for(int ttt=1; ttt<=tcase; ttt++) {
		int n;
		scanf("%d", &n);
		int ret = 0;
		for(int k=1; k<n; k++) ret = (ret + D[n][k]) % mod;
		printf("Case #%d: %d\n", ttt, ret);
	}
}

