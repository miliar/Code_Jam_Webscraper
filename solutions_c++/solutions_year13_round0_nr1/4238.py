/*
PROG: zzz
LANG: C++
ID: 2012agura1
*/

/*
* The following code is based off of a shell written before the contest.
*/

#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <ctime>

using namespace std;
FILE *fin  = fopen("a.in",  "r");
FILE *fout = fopen("gcj-a.out", "w");
/*
* Keep arrays small.  Smaller than 4,000,000 integers or 2,000,000 long longs/doubles
*/

int main () {
	//clock_t time0 = clock();
	int T;
    char arr[4][4];
    char s[10];
	fscanf(fin, "%d", &T);

    for(int t = 1; t <= T; t++) {
        for(int r = 0; r < 4; r++) {
            fscanf(fin, "%s", s);
            for(int c = 0; c < 4; c++) {
                arr[r][c] = s[c];
            }
        }
        bool cont = false;
        // Highest precidence = X or O win?
        // rows
        for(int r = 0; r < 4; r++) {
            int nx=0,no=0,nt=0;
            for(int c = 0; c < 4; c++) {
                if(arr[r][c] == 'O') no++;
                if(arr[r][c] == 'X') nx++;
                if(arr[r][c] == 'T') nt++;
            }
            if(nx == 3 && nt == 1 || nx == 4) {
                fprintf(fout, "%s%d%s\n", "Case #", t, ": X won");
                cont = true;
                break;
            }
            if(no == 3 && nt == 1 || no == 4) {
                fprintf(fout, "%s%d%s\n", "Case #", t, ": O won");
                cont = true;
                break;
            }
        }
        if(cont) continue;
        //cols
        for(int c = 0; c < 4; c++) {
            int nx = 0, no = 0, nt = 0;
            for(int r = 0; r < 4; r++) {
                if(arr[r][c] == 'O') no++;
                if(arr[r][c] == 'X') nx++;
                if(arr[r][c] == 'T') nt++;
            }
            if(nx == 3 && nt == 1 || nx == 4) {
                fprintf(fout, "%s%d%s\n", "Case #", t, ": X won");
                cont = true;
                break;
            }
            if(no == 3 && nt == 1 || no == 4) {
                fprintf(fout, "%s%d%s\n", "Case #", t, ": O won");
                cont = true;
                break;
            }
        }
        if(cont) continue;
        // main diag
        int nx=0,no=0,nt=0;
        for(int i = 0; i < 4; i++) {
            if(arr[i][i] == 'O') no++;
            if(arr[i][i] == 'X') nx++;
            if(arr[i][i] == 'T') nt++;
        }
        if(nx == 3 && nt == 1 || nx == 4) {
            fprintf(fout, "%s%d%s\n", "Case #",t,": X won");
            continue;
        }
        if(no == 3 && nt == 1 || no == 4) {
            fprintf(fout, "%s%d%s\n", "Case #",t,": O won");
            continue;
        }
        // anti diag
        nx=0,no=0,nt=0;
        for(int i = 0; i < 4; i++) {
            if(arr[i][3-i] == 'O') no++;
            if(arr[i][3-i] == 'X') nx++;
            if(arr[i][3-i] == 'T') nt++;
        }
        if(nx == 3 && nt == 1 || nx == 4) {
            fprintf(fout, "%s%d%s\n", "Case #",t,": X won");
            continue;
        }
        if(no == 3 && nt == 1 || no == 4) {
            fprintf(fout, "%s%d%s\n", "Case #",t,": O won");
            continue;
        }
        // draw or game not complete
        int ndot = 0;
        for(int r = 0; r < 4; r++)
            for(int c = 0; c < 4; c++)
                if(arr[r][c] == '.') ndot++;
        if(ndot == 0)
            fprintf(fout, "%s%d%s\n", "Case #",t,": Draw");
        else
            fprintf(fout, "%s%d%s\n", "Case #",t,": Game has not completed");
    }

	return 0;
}


