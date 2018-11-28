#include <iostream> 
#include <vector> 
#include <cstdio> 
#include <cstring> 
#include <algorithm> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <string> 
#include <sstream> 
#include <ctime> 
#include <cmath> 

using namespace std; 

int T, C, D, N, cur;
char carr[40][5], darr[33][5], narr[105], ans[105];

void remove() {
	if (cur < 2) return;
	for (int i = 1; i <= C; i++) {
        int yes = 0;
        if (carr[i][0] == ans[cur-1] && carr[i][1] == ans[cur-2]) yes = 1;
        if (carr[i][1] == ans[cur-1] && carr[i][0] == ans[cur-2]) yes = 1;
		if (yes) {
            //printf("%d %c\n", cur, carr[i][2]);
			ans[cur-2] = carr[i][2]; cur -= 1;
			return;
		}
	}
}

void clear() {
	if (cur < 2) return;
	for (int i = 1; i <= D; i++) {
		for (int j = 0; j < cur; j++) {
			for (int k = j+1; k < cur; k++) {
				int yes = 0;
				if (darr[i][0] == ans[j] && darr[i][1] == ans[k]) yes = 1;
				if (darr[i][0] == ans[k] && darr[i][1] == ans[j]) yes = 1;
				if (yes) {
					cur = 0; return;
				}
			}
		}
	}
}

int main() { 
	FILE *fin = fopen("P2.txt", "r");
	FILE *fout = fopen("P2ans.txt", "w");
	fscanf(fin, "%d", &T);
	for (int z = 1; z <= T; z++) {
		fscanf(fin, "%d", &C);
		for (int i = 1; i <= C; i++) {
			fscanf(fin, "%s", &carr[i]);
		}
		fscanf(fin, "%d", &D);
		for (int i = 1; i <= D; i++) {
			fscanf(fin, "%s", &darr[i]);
		}
		fscanf(fin, "%d %s", &N, &narr);
		cur = 0;
		for (int i = 1; i <= N; i++) {
			ans[cur++] = narr[i-1];
			remove();
			clear();
		}
		fprintf(fout, "Case #%d: [", z);
		if (!cur) fprintf(fout, "]\n");
		for (int i = 0; i < cur; i++) {
			if (i != cur-1) {
				fprintf(fout, "%c, ", ans[i]);
			}
			else {
				fprintf(fout, "%c]\n", ans[i]);
			}
		}
	}
	
	//cin.get();
	
    return 0;
}

