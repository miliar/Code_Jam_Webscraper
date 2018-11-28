#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cstdlib>

#define MOD 10007

using namespace std;

int mat[200][200];
int prob[20][2];
int h, w, r;

int main() {
    int teste, t;
    scanf("%d", &teste);
    int i, j, k;
    for (t=0; t<teste; t++) {
        scanf("%d %d %d", &h, &w, &r);
        for (i=0; i<h; i++)
        {
            for (j=0; j<w; j++){
                mat[i][j] = 0;
            }
        }
        mat[0][0] = 1;
        for (i=0; i<r; i++){
            scanf("%d %d", &prob[i][0], &prob[i][1]);
            prob[i][0]--;
            prob[i][1]--;
            mat[prob[i][0]][prob[i][1]] = 0;
        }
        for (i=1; i<h; i++)
        {
            for (j=1; j<w; j++){
                for (k=0; k<r; k++){
                    if (prob[k][0] == i && prob[k][1] == j)
                       break;
                }
                if (k<r) continue;
                if (i>=2) mat[i][j] = (mat[i][j]+mat[i-2][j-1])%MOD;
                if (j>=2) mat[i][j] = (mat[i][j]+mat[i-1][j-2])%MOD;
            }
        }
        printf("Case #%d: %d\n", t+1, mat[h-1][w-1]);   
    }
    return 0;    
}
