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

int T, R, C, D;
char arr[505][505];
double pos[505][505][2];
double mass[505][505][2];
double sumpos[505][505][2];
double summass[505][505][2];

int main() { 
	FILE *fin = fopen("test.txt", "r");  
	FILE *fout = fopen("testans.txt", "w");
	
	fscanf(fin, "%d", &T);
	
	for (int z = 1; z <= T; z++) {
		for (int i = 0; i <= 504; i++) {
			for (int j = 0; j <= 504; j++) {
				sumpos[i][j][0] = 0.0; sumpos[i][j][1] = 0.0;
				summass[i][j][0] = 0.0; summass[i][j][1] = 0.0;
			}
		}
		fscanf(fin, "%d %d %d", &R, &C, &D);
		for (int i = 1; i <= R; i++) {
			fscanf(fin, "%s", &arr[i][1]);
		}
		for (int i = 1; i <= R; i++) {
			for (int j = 1; j <= C; j++) {
				pos[i][j][0] = (double)((arr[i][j]-'0')+1)*i;
				pos[i][j][1] = (double)((arr[i][j]-'0')+1)*j;
				mass[i][j][0] = (double)(arr[i][j]-'0')+1;
			}
		}
		for (int i = 1; i <= R; i++) {
			for (int j = 1; j <= C; j++) {
				for (int k = 0; k < 2; k++) {
					sumpos[i][j][k] = sumpos[i][j-1][k] + sumpos[i-1][j][k] - sumpos[i-1][j-1][k] +pos[i][j][k];
				}
				summass[i][j][0] = summass[i][j-1][0] + summass[i-1][j][0] - summass[i-1][j-1][0]+mass[i][j][0];
			}
		}
		
		
		//for (int i = 1; i <= R; i++) for (int j = 1; j <= C; j++) printf("%d\n", arr[i][j]-'0');
		int done = 0, ans = -1;
		for (int y = min(R, C); y >= 3; y--) {
			int maxa = R-y+1, maxb = C-y+1;
			for (int i = 1; i <= maxa; i++) {
				for (int j = 1; j <= maxb; j++) {
                    //printf("check %d %d %d\n", i, j, y);
					double cursum[2], curmass;
					for (int k = 0; k < 2; k++) {
						cursum[k] = sumpos[i+y-1][j+y-1][k] + sumpos[i-1][j-1][k] - sumpos[i+y-1][j-1][k] - sumpos[i-1][j+y-1][k];
						cursum[k] -= (pos[i][j][k] + pos[i+y-1][j][k] + pos[i][j+y-1][k] + pos[i+y-1][j+y-1][k]);
					}
					curmass = summass[i+y-1][j+y-1][0] + summass[i-1][j-1][0] - summass[i+y-1][j-1][0] - summass[i-1][j+y-1][0];
					curmass -= (mass[i][j][0] + mass[i+y-1][j][0] + mass[i][j+y-1][0] + mass[i+y-1][j+y-1][0]);
					//printf("curmass %f\n", curmass);
					double p = i + (y-1)/2.0 - cursum[0]/curmass, q = j + (y-1)/2.0 - cursum[1]/curmass;
					//printf("%.6f %.6f\n", p, q);
					if (abs(p) < 1e-6 && abs(q) < 1e-6) {
						done = 1; ans = y;
					}
					if (done) break;
				}
				if (done) break;
			}
			if (done) break;
		}
		if (done) {
			//printf("Case #%d: %d\n", z, ans);
			fprintf(fout, "Case #%d: %d\n", z, ans);
		}
		else {
            //printf("Case #%d: IMPOSSIBLE\n", z, ans);
            fprintf(fout, "Case #%d: IMPOSSIBLE\n", z, ans);
        }
	}
	
	
	
	
	//cin.get();
	
    return 0;
}

