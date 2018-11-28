#include <stdio.h>
#include <string.h>

char str1[100], str2[100];

int getTime(char str[]) {
	int i, j;
	sscanf(str, "%d:%d", &i, &j);
	return i * 60 + j;
}

void swap(int &a, int &b) {
	int c = a;
	a = b;
	b = c;
}

int nTrain, time[1000], dt[1000], ns, nn;
int start[1000], end[1000], dir[1000];

int main() {
	freopen("B.in","r",stdin);
	freopen("B.out", "w", stdout);

	int i, j, t, turn, n, m, testcases;

	scanf("%d", &testcases);
	for (t = 0; t < testcases; t++) {
		scanf("%d", &turn);
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; i++) {
			scanf("%s%s", str1, str2);
			start[i] = getTime(str1);
			end[i] = getTime(str2);
			dir[i] = 0;
		}
		for (i = 0; i < m; i++) {
			scanf("%s%s", str1, str2);
			start[i + n] = getTime(str1);
			end[i + n] = getTime(str2);
			dir[i + n] = 1;
		}
		for (i = 0; i < n + m; i++) {
			for (j = i + 1; j < n + m; j++) {
				if (start[i] > start[j]) {
					swap(start[i], start[j]);
					swap(end[i], end[j]);
					swap(dir[i], dir[j]);
				}
			}
		}
		ns = nn = nTrain = 0;
		for (i = 0; i < n + m; i++) {
			for (j = 0; j < nTrain; j++) {
				if (time[j] + turn <= start[i] && dt[j] != dir[i]) {
					time[j] = end[i];
					dt[j] = dir[i];
					break;
				}
			}
			if (j == nTrain) {
				time[nTrain] = end[i];
				dt[nTrain] = dir[i];
				nTrain++;
				if (dir[i] == 0) ns++;
				else nn++;
			}
		}
		printf("Case #%d: %d %d\n", t + 1, ns, nn);
	}

	return 0;
}
