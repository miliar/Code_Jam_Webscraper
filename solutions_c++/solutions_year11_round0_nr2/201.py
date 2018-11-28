/* 
 * File:   main.cpp
 * Author: Prowindy
 *
 * Created on 2011年5月7日, 上午11:49
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
char str[1000], ans[1000];
char U[300][300], D[300][300];

int main(int argc, char** argv) {
    int tt, tcas = 1;
    int i, j, a, N;
    int Un,Dn;
    freopen("B-large.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d", &tt);
    while (tt--) {
        memset(U, 0, sizeof (U));
        memset(D, 0, sizeof (D));
        
        scanf("%d", &Un);
        for (i = 0; i < Un; i++) {
            scanf("%s", str);
            U[str[0]][str[1]] =U[str[1]][str[0]]= str[2];
        }
        scanf("%d", &Dn);
        for (i = 0; i < Dn; i++) {
            scanf("%s", str);
            D[str[0]][str[1]] = D[str[1]][str[0]] = 1;
        }
        scanf("%d%s", &N, str);
        int len = -1;
        for (i = 0; i < N; i++) {
            ans[++len] = str[i];
            while (len - 1 >= 0) {
                if (U[ans[len]][ans[len - 1]] != 0) {
                    ans[len - 1] = U[ans[len]][ans[len - 1]];
                    len--;
                }else break;
            }
            for (j = 0; j < len; j++)
                if (D[ans[len]][ans[j]] == 1) {
                    len = -1;
                }
        }

        printf("Case #%d: [", tcas++);
        for (i = 0; i <= len; i++)
            if (i != len) printf("%c, ", ans[i]);
            else printf("%c", ans[i]);
        printf("]\n");
    }
}


