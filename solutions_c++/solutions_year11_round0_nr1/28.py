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

int T, N, opos, bpos, cur, move, nexto, nextb;
char carr[110][5]; 
int narr[110];

int main() { 
	FILE *fin = fopen("P1.txt", "r");
	FILE *fout = fopen("P1ans.txt", "w");
	fscanf(fin, "%d", &T);
	for (int z = 1; z <= T; z++) {
		fscanf(fin, "%d", &N);
		for (int i = 1; i <= N; i++) {
			fscanf(fin, "%s %d", &carr[i], &narr[i]);
		}
		carr[N+1][0] = 'B'; carr[N+2][0] = 'O'; narr[N+1] = 1, narr[N+2] = 1;
		opos = 1, bpos = 1, cur = 1, move = 0, nexto = 1, nextb = 1;
		while (carr[nexto][0] != 'O') nexto++; while (carr[nextb][0] != 'B') nextb++;
		while (true) {
			if (cur > N) break;
			if (carr[cur][0] == 'B') {
				move++;
				if (opos < narr[nexto]) opos++;
				else if (opos > narr[nexto]) opos--;
				if (bpos == narr[cur]) {
					cur++; nextb++;
					while (carr[nextb][0] != 'B') nextb++;
					continue;
				}
				if (bpos < narr[nextb]) bpos++;
				else if (bpos > narr[nextb]) bpos--;
			}
			else {
				move++;
				if (bpos < narr[nextb]) bpos++;
				else if (bpos > narr[nextb]) bpos--;
				if (opos == narr[cur]) {
					cur++; nexto++;
					while (carr[nexto][0] != 'O') nexto++;
					continue;
				}
				if (opos < narr[nexto]) opos++;
				else if (opos > narr[nexto]) opos--;
			}
		}
		fprintf(fout, "Case #%d: %d\n", z, move);
	}
	
	//cin.get();
	
    return 0;
}

