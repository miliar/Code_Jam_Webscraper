#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int n, k, p[120][30];
bool bcross[120][120];
int cross[120][120], ncross[120], nout[120];

int sgn(int a)
{
	if (a < 0) return -1;
	if (a > 0) return 1;
	return 0;
}

bool used[120];
int group[120][120], ngroup[120], ngroups, left;
int min;

void search()
{
	int i, j, c = -1;
	if (ngroups >= min) return;
	if (left == 0) {
		min = ngroups;
		return;
	}
	for (i = 0; i < n; i++) {
		if (used[i]) continue;
		if (c == -1 || nout[i] > nout[c]) c = i;
	}
	left--;
	for (int k = 0; k < ncross[c]; k++) nout[k]--;
	used[c] = true;
	for (i = 0; i < ngroups; i++) {
		for (j = 0; j < ngroup[i]; j++) {
			if (bcross[c][group[i][j]]) break;
		}
		if (j >= ngroup[i]) {
			group[i][ngroup[i]] = c;
			ngroup[i]++;
			search();
			ngroup[i]--;
		}
	}
	ngroups++;
	group[i][ngroup[i]] = c;
	ngroup[i]++;
	search();
	ngroup[i]--;
	used[c] = false;
	for (int k = 0; k < ncross[c]; k++) nout[k]++;
	left++;
	ngroups--;
}

int main()
{
	int cas, cases, i, j, t;
	scanf("%d", &cases);
	for (cas = 1; cas <= cases; cas++) {
		memset(ncross, 0, sizeof(ncross));
		memset(bcross, 0, sizeof(bcross));
		scanf("%d%d", &n, &k);
		for (i = 0; i < n; i++) {
			for (j = 0; j < k; j++)
				scanf("%d", &p[i][j]);
		}
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				for (t = 1; t < k; t++) {
					if (sgn(p[i][0] - p[j][0]) * sgn(p[i][t] - p[j][t]) != 1) {
						cross[i][ncross[i]++] = j;
						bcross[i][j] = true;
						break;
					}
				}
			}
		}
		memcpy(nout, ncross, sizeof(ncross));
		memset(used, 0, sizeof(used));
		memset(ngroup, 0, sizeof(ngroup));
		min = 0x7FFFFFFF;
		ngroups = 0;
		left = n;
		search();
		printf("Case #%d: %d\n", cas, min);
	}
	return 0;
}
