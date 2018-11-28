/*
 * Author: NomadThanatos
 * Created Time:  2011/5/7 13:41:31
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <set>

using namespace std;

#define SZ(v) ((int)(v).size())
const int MAXINT = -1u>>1;
const int MAXN = 101;

int f[MAXN][MAXN][MAXN];
int pos[MAXN];
char color[MAXN][2];

int main() {
    freopen("A.out","w",stdout);
    int N;
    scanf("%d",&N);
    int t = 0;
    while(scanf("%d",&N) == 1) {
        for(int i = 1 ; i < N + 1 ; i++) {
            scanf("%s%d",color[i],pos + i);
        }
        memset(f,1,sizeof(f));
        f[0][1][1] = 0;
        int res;
        for(int k = 1 ; k < N + 1 ; k++) {
            int bi,bj,i,j;
            res = MAXINT;
            if (k == 1) {
                bi = 1;
                bj = 1;
                if (color[k][0] == 'O') {
                    i = pos[k];
                    for(j = 1 ;  j < MAXN ; j++) {
                        f[k][i][j] = min(f[k][i][j],f[k - 1][bi][bj] + max(abs(i - bi) + 1,abs(j - bj)));
                        res = min(res,f[k][i][j]);
                    }
                }
                else {
                    j = pos[k];
                    for(i = 1 ; i < MAXN ; i++) {
                        f[k][i][j] = min(f[k][i][j],f[k - 1][bi][bj] + max(abs(i - bi),abs(j - bj) + 1));
                        res = min(res,f[k][i][j]);
                    }
                }
            }
            else if (color[k - 1][0] == 'O') {
                bi = pos[k - 1];
                for(bj = 1 ; bj < MAXN ; bj++) {
                    if (color[k][0] == 'O') {
                        i = pos[k];
                        for(j = 1 ;  j < MAXN ; j++) {
                            f[k][i][j] = min(f[k][i][j],f[k - 1][bi][bj] + max(abs(i - bi) + 1,abs(j - bj)));
                            res = min(res,f[k][i][j]);
                        }
                    }
                    else {
                        j = pos[k];
                        for(i = 1 ; i < MAXN ; i++) {
                            f[k][i][j] = min(f[k][i][j],f[k - 1][bi][bj] + max(abs(i - bi),abs(j - bj) + 1));
                            res = min(res,f[k][i][j]);
                        }
                    }
                }
            }
            else {
                bj = pos[k - 1];
                for(bi = 1 ; bi < MAXN ; bi++) {
                    if (color[k][0] == 'O') {
                        i = pos[k];
                        for(j = 1 ;  j < MAXN ; j++) {
                            f[k][i][j] = min(f[k][i][j],f[k - 1][bi][bj] + max(abs(i - bi) + 1,abs(j - bj)));
                            res = min(res,f[k][i][j]);
                        }
                    }
                    else {
                        j = pos[k];
                        for(i = 1 ; i < MAXN ; i++) {
                            f[k][i][j] = min(f[k][i][j],f[k - 1][bi][bj] + max(abs(i - bi),abs(j - bj) + 1));
                            res = min(res,f[k][i][j]);
                        }
                    }
                }
            }
            //for(int i = 1 ; i < 5 ; i++) {
                //for(int j = 1 ; j < 5 ; j++) {
                    //printf("%d ",f[k][i][j]);
                //}
                //printf("\n");
            //}
            //printf("---------\n");
        }
        printf("Case #%d: %d\n",t + 1,res);
        t++;
    }

    return 0;
}

