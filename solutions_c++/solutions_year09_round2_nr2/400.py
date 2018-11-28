#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char line[100];
char list[10000][100];
int pos[10000];
int size;

bool cmp(int a, int b) {
	return strcmp(list[a], list[b]) < 0;
}

int main() {
	int caseSize;
	scanf("%d", &caseSize);
	for (int T = 1; T <= caseSize; T++) {
		scanf("%s", line);
		int len = strlen(line);
		size = 0;
		for (int i = 0; i < len; i++) {
			for (int j = i + 1; j < len; j++) {
				if (line[j] > line[i]) {
					list[size][len] = 0;
					for (int k = 0; k < len; k++) {
						list[size][k] = line[k];
					}
					list[size][i] = line[j];
					list[size][j] = line[i];
					sort(list[size] + i + 1, list[size] + len);
					size++;
				}
			}
		}
		if (size == 0) {
			int temp = 0;
			for (int i = 0; i < len; i++) {
				if (line[i] != '0' && line[i] < line[temp]) temp = i;
			}
			list[size][len + 1] = 0;
			for (int k = 1; k <= len; k++)
				list[size][k] = line[k - 1];
			list[size][0] = line[temp];
			list[size][temp + 1] = '0';
			sort(list[size] + 1, list[size] + len + 1);
			size++;
		}
		for (int i = 0; i < size; i++) pos[i] = i;
		sort(pos, pos + size, cmp);
		printf("Case #%d: %s\n", T, list[pos[0]]);
	}
	return 0;
}
