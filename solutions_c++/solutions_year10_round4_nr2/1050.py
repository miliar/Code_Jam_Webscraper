#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>

using namespace std;

#define MAX 1030

int T;
int P;
int M[ MAX ];
int tic[ 11 ][ MAX ];
int prices[11][MAX];

int main(int argc, char** argv) {
    freopen("B-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int pp = 1; pp <= T; pp++){
        scanf("%d",&P);
        for (int i = 0; i < (1<<P); i++)
            scanf("%d",&M[i]);
        for (int i = 0; i < P; i++)
            for (int j = 0; j < (1<<(P-i-1)); j++){
                scanf("%d",&prices[i][j]);
            }
        memset(tic,0,sizeof(tic));
        int res = 0;
        for (int i = 0; i < (1<<P); i++){
            int nTics = P - M[i];            
            for (int r = P-1; r >= 0 && nTics > 0; r--,nTics--){
                int match = (i / (1 << (r+1)));

                if (tic[r][match] == 0) tic[r][match] = 1, res+= prices[r][match];
            }
        }
        printf("Case #%d: %d\n",pp,res);
    }
    return (EXIT_SUCCESS);
}