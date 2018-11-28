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

int T, R, C, temp[7][7];
char arr[7][7], junk[400];

int main() { 
	FILE *fin = fopen("test.txt", "r");  
	FILE *fout = fopen("testans.txt", "w");
	
	fscanf(fin, "%d", &T);
	
	for (int z = 1; z <= T; z++) {
		int ans = 0;
		fscanf(fin, "%d %d", &R, &C);
		//fgets(junk, 100, fin);
		for (int i = 0; i < R; i++) {
			fscanf(fin, "%s", &arr[i]);
		}
		//for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) printf("%c\n", arr[i][j]);
		int K = (1 << (R*C));
		for (int i = 0; i < K; i++) {
            //printf("%d\n", i);
			memset(temp, 0, sizeof temp);
			for (int j = 0; j < R*C; j++) {
				int curbit = (i >> j) & 1;
				int x = j % C, y = j / C;
				//printf("x y %d %d\n", x, y);
				if (arr[y][x] == '|') {
					if (curbit == 0) {
						y = (y+1) % R;
					} else {
						y = (y+R-1) % R;
					}
				} else if (arr[y][x] == '-') {
					if (curbit == 0) {
						x = (x+1)%C;
					} else {
						x = (x+C-1)%C;
					}
				} else if (arr[y][x] == '/') {
					if (curbit == 0) {
						x = (x+1)%C; y = (y+R-1) % R;
					} else {
						x = (x+C-1)%C; y = (y+1) % R;
					}
				} else if (arr[y][x] == '\\') {
					if (curbit == 0) {
						x = (x+1)%C; y = (y+1) % R;
					} else {
						x = (x+C-1)%C; y = (y+R-1) % R;
					}
				}
				//printf("%d %d\n", x, y);
				if (temp[x][y] != 0) break;
				temp[x][y] = 1;
				if (j == R*C-1) {
                    //printf("i is %d\n", i);
                    ans++;
                }
			}
		}
		//printf("Case #%d: %d\n", z, ans);
		fprintf(fout, "Case #%d: %d\n", z, ans);
	}
	
	
	
	
	//cin.get();
	
    return 0;
}

