/* 
 * File:   main.cpp
 * Author: Prowindy
 *
 * Created on 2011年5月7日, 上午10:35
 */
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <set>
#include <math.h>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

/*
 * 
 */
int order[200][2],Q[101*101*101][3],step[101][101][101];
int main(int argc, char** argv) {
    int tt, tcas = 1;
    int i,j,a,N;
    char str[10];
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d", &tt);
    while (tt--) {
        printf("Case #%d: ", tcas++);
        scanf("%d", &N);
        for (i = 0; i < N; i++) {
            scanf("%s%d", str, &a);
            order[i][0] = (str[0] == 'O' ? 0 : 1);
            order[i][1] = a;
        }
        int L = 0, R = 1;
        Q[0][0] = 1, Q[0][1] = 1, Q[0][2] = 0;
        memset(step, -1, sizeof (step));
        int ans = 1000000000;
        step[1][1][0] = 0;
        while (L < R) {
            int a = Q[L][0], b = Q[L][1], t = Q[L][2];
            L++;
            if (t == N) {
                ans = min(ans, step[a][b][t]);
                continue;
            }
            for (i = -1; i <= 1; i++)
                for (j = -1; j <= 1; j++) {
                    int aa = a, bb = b;
                    aa += i, bb += j;
                    if (aa >= 1 && aa <= 100 && bb >= 1 && bb <= 100) {
                        if (step[aa][bb][t] < 0) {
                            step[aa][bb][t] = step[a][b][t] + 1;
                            Q[R][0] = aa, Q[R][1] = bb, Q[R][2] = t;
                            R++;
                        }
                        if (order[t][0] == 0) {
                            if (i == 0 && aa == order[t][1]) {
                                if (step[aa][bb][t + 1] < 0) {
                                    step[aa][bb][t + 1] = step[a][b][t] + 1;
                                    Q[R][0] = aa, Q[R][1] = bb, Q[R][2] = t + 1;
                                    R++;
                                }
                            }
                        } else {
                            if (j == 0 && bb == order[t][1]) {
                                if (step[aa][bb][t + 1] < 0) {
                                    step[aa][bb][t + 1] = step[a][b][t] + 1;
                                    Q[R][0] = aa, Q[R][1] = bb, Q[R][2] = t + 1;
                                    R++;
                                }
                            }
                        }
                    }
                }

        }
        printf("%d\n", ans);
    }
    return (EXIT_SUCCESS);
}

