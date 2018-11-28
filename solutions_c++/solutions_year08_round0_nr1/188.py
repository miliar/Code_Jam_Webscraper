#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

FILE *fp, *fp_w;
int t, n, m;
int i, j, k, l;
char engine[110][110], query[1010][110];
int dp[1000][100], q[1000];
int next, val;

int main() {

	//fp = fopen("A-small.txt", "r");
	fp = fopen("A-large.in", "r");

	fp_w = fopen("out", "w");

	fscanf(fp, "%d", &t);
	for(i = 0; i < t; i++) {
		fscanf(fp, "%d", &n);
		fgets(engine[0], 110, fp);
		for(j = 0; j < n; j++) {
			memset(engine[j], 0, 110);
			fgets(engine[j], 110, fp);
		}

		fscanf(fp, "%d", &m);
		fgets(query[0], 110, fp);
		for(j = 0; j < m; j++) {
			memset(query[j], 0, 110);
			fgets(query[j], 110, fp);			
			for(k = 0; k < n; k++) {
				if (strncmp(query[j], engine[k], strlen(query[j])) == 0) {
					q[j] = k;
					break;
				}
			}
		}

		for(j = 0; j < m; j++)
			for(k = 0; k < n; k++)
				dp[j][k] = -1;

		for(j = 0; j < n; j++) {
			if (q[0] == j) continue;
			dp[0][j] = 0;
		}

		for(j = 1; j < m; j++) {
			for(k = 0; k < n; k++) {
				if (q[j] == k) continue;
				for(l = 0; l < n; l++) {
					if (dp[j-1][l] == -1) continue;

					next = dp[j-1][l] + (l == k ? 0 : 1);
					if (dp[j][k] == -1 || dp[j][k] > next)
						dp[j][k] = next;
				}
			}
		}

		val = 987654321;
		for(j = 0; j < n; j++) {
			if (dp[m-1][j] == -1) continue;
			val = min(val, dp[m-1][j]);
		}
				
		fprintf(fp_w, "Case #%d: %d\n", i+1, val);
	}

	fclose(fp_w);
	fclose(fp);

	return 0;
}