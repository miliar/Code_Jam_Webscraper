#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>

#define INFILE "A-large.in"
#define OUTFILE "A-large.out"

using namespace std;

int wire[1004][2];

int main() {
	FILE *fpIn = freopen(INFILE, "r", stdin);
	if (fpIn == NULL) {
		printf("[main] Fail to call freopen()");
		return -1;
	}
	FILE *fpOut = fopen(OUTFILE, "w");
	if (fpOut == NULL) {
		printf("[main] Fail to call fopen()");
		return -1;
	}

	int T;
	scanf("%d", &T);

	for (int cntCase = 0; cntCase < T; cntCase++) {
		int N;
		scanf("%d", &N);

		for (int i = 0; i < N; i++) 
			scanf("%d %d", &wire[i][0], &wire[i][1]);

		unsigned long long ans = 0;
		for (int i = 0; i < N; i++) {
			for (int j = i+1; j < N; j++) {
				if (wire[i][0] > wire[j][0] && wire[i][1] < wire[j][1])
					ans++;
				else if (wire[i][0] < wire[j][0] && wire[i][1] > wire[j][1])
					ans++;
			}
		}

		fprintf(fpOut, "Case #%d: %llu\n", cntCase+1, ans);
	}

}