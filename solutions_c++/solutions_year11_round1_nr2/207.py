#include <cstdio>
#include <cstring>

int n, m;
char words[10000][15];
bool letterUsed[30];
bool known[15];
bool bad[10000];


int simulate(char ordering[], int wordUsed) {
	for (int i = 0; i < strlen(words[wordUsed]); i++) {
		known[i] = false;
	}

	for (int i = 0; i < 26; i++) {
		letterUsed[i] = false;
	}

	for (int i = 0; i < n; i++) {
		if (strlen(words[i]) != strlen(words[wordUsed])) {
			bad[i] = true;
		} else {
			bad[i] = false;
		}
	}

	int ret = 0;
	for (int i = 0; i < 26; i++) {
		bool willUse = false;
		for (int j = 0; j < n; j++) {
			if (bad[j]) {
				continue;
			}
			bool mightUse = false;
			for (int k = 0; k < strlen(words[j]) && !bad[j]; k++) {
				if (known[k] && words[j][k] != words[wordUsed][k]) {
					bad[j] = true;
				} else if (letterUsed[words[j][k] - 'a'] && words[wordUsed][k] != words[j][k]) {
					bad[j] = true;
				} else if (words[j][k] == ordering[i]) {
					mightUse = true;
				}
			}
			if (!bad[j] && mightUse) {
				willUse = true;
			}
		}
		letterUsed[ordering[i] - 'a'] = true;
		for (int j = 0; j < strlen(words[wordUsed]); j++) {
			if (words[wordUsed][j] == ordering[i]) {
				known[j] = true;
			}
		}
		if (willUse) {
			ret++;
			for (int j = 0; j < strlen(words[wordUsed]); j++) {
				if (words[wordUsed][j] == ordering[i]) {
					ret--;
					break;
				}
			}
		}
	}
	return ret;
}

int cost[10000];

void proc() {
	scanf("%d %d ", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%s ", words[i]);
	}
	for (int i = 0; i < m; i++) {
		char ordering[30];
		scanf("%s ", ordering);
		int highest = 0;
		for (int j = 0; j < n; j++) {
			cost[j] = simulate(ordering, j);
			if (cost[highest] < cost[j]) {
				highest = j;
			}
		}
		for (int j = 0; j < n; j++) {
		//	printf("%s %d\n", words[j], cost[j]);
		}
		printf(" %s", words[highest]);
	}
}

int main() {
	int c;
	scanf("%d ", &c);
	for (int i = 1; i <= c; i++) {
		printf("Case #%d:", i);
		proc();
		printf("\n");
	}

	return 0;
}
