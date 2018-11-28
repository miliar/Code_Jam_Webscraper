#include <cstdio>
#include <algorithm>
using namespace std;

int main(int argc, char **argv) {
    int t; scanf("%d", &t);
    for(int tci = 0; tci < t; tci++) {
        int k; scanf("%d", &k);
        int tbl[10][10];
        for(int xpy = 0; xpy < k*2-1; xpy++) {
            for(int x = max(0, xpy-k+1); x <= min(xpy,k-1); x++) {
                scanf("%d", &tbl[x][xpy-x]);
            }
        }
        int c = k-1;
        int mdif0=k, mdif1=k;
        for(int i = 0; i <= c; i++) {
            bool able0=true,able1=true,able2=true,able3=true;
            for(int x = 0; x <= i; x++) {
                for(int y = 0; y <= i; y++) {
                    able0 = able0 && tbl[x][y]==tbl[i-y][i-x];
                    able1 = able1 && tbl[x][c-y]==tbl[i-y][c-i+x];
                    able2 = able2 && tbl[c-x][y]==tbl[c-i+y][i-x];
                    able3 = able3 && tbl[c-x][c-y]==tbl[c-i+y][c-i+x];
                }
            }
            if(able0 || able3)mdif0 = min(mdif0, c-i);
            if(able1 || able2)mdif1 = min(mdif1, c-i);
        }
        int mdif = mdif0+mdif1;
        printf("Case #%d: %d\n",tci+1, (k*2+mdif)*mdif);
    }
}

