#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <queue>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

char str[500];
char combine[300][300];
char oppose[300][300];
char final[200];
int process() {
	int C,D,N;
	memset(combine, 0, sizeof(combine));
	memset(oppose, 0, sizeof(oppose));
	
	scanf("%d", &C);
	for (int i = 0; i < C; ++i) {
		scanf("%s", str);
		combine[str[0]][str[1]] = combine[str[1]][str[0]] = str[2];
	}
	
	scanf("%d", &D);
	for (int i = 0; i < D; ++i) {
		scanf("%s", str);
		oppose[str[0]][str[1]] = oppose[str[1]][str[0]] = 1;
	}
	
	scanf("%d %s", &N, str);
	int end = 0;
	
	char c;
	bool cleared;
	for (int i = 0; i < N; i++) {
		c = str[i];
		while (end > 0 && combine[c][final[end-1]] > 0) {
			c = combine[c][final[end-1]];
			--end;
		}
		cleared = false;
		for (int j = 0; j < end; j++) {
			if (oppose[c][final[j]]) {
				cleared = true;
				end = 0;
			}
		}
		if (!cleared) {
			final[end] = c;
			end++;
		}
	}
	
	printf("[");
	for (int i = 0; i < end; i++) {
		if (i) printf(", ");
		printf("%c", final[i]);
	}
	printf("]");
}

int main() {
	
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int i = 0 ; i < T ; i++) {
		printf("Case #%d: ", i+1);
		process();
		printf("\n");
	}
	
	return 0;
}
