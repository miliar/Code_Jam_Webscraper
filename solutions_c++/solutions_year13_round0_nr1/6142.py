#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <cstdlib>

using namespace std;

int main()
{
    int p,flag,up1, dw2,ctr,k,di;
    scanf("%d", &p);
    getchar();
    for(int t = 1;  t <= p; t++) {
            char c[4][4];
            flag = up1 = dw2 = ctr = di = 0;
            char a;
            for(int i = 0; i < 4; i++) {
                    for(int j = 0; j  < 4; j++) {
                            scanf("%c", &c[i][j]);
                            if(c[i][j] == '.') ctr++;
                    }
                    getchar();
            }
            for(int i = 0; i < 4; i++) {
                a = c[i][0];
                int flag = 0;
                int j = 1;
                k = 1;
                if(a == 'T') {
                        a = c[i][1];
                        j = 2;
                        k = 2;
                }
                if(i == 0) {
                while(k < 4) {
                        if(c[k][k] != a && c[k][k] != 'T') di = 1;
                        k++;
                }
                }
                if(a != '.') {
                    while(j < 4) {
                        if(c[i][j] != a && c[i][j] != 'T') {
                                flag = 1;
                                break;
                        }
                        j++;
                    }
                }
                if((flag == 0 && a != '.') || (di == 0 && i == 0 && a != '.')) {
                        printf("Case #%d: %c won\n", t, a);
                        up1 = 1;
                        break;
                }
            }
        if(up1 != 1) {
                di = 0;
            for(int i = 0; i < 4; i++) {
                a = c[0][i];
                int flag = 0;
                int j = 1;
                k = 2;
                if(a == 'T') {
                        a = c[1][i];
                        j = 2;
                        k = 1;
                }
                if(i == 3) {
                while(k >= 0) {
                        if(c[3-k][k] != a && c[3-k][k] != 'T') di = 1;
                        k--;
                }
                }
                if(a != '.') {
                    while(j < 4) {
                        if(c[j][i] != a && c[j][i] != 'T') {
                                flag = 1;
                                break;
                        }
                        j++;
                    }
                }
                if((flag == 0 && a != '.') || (di == 0 && i == 3 && a != '.') ) {
                        printf("Case #%d: %c won\n", t, a);
                        dw2 = 1;
                        break;
                }
            }
        }
        if(up1 != 1 && dw2 != 1 && ctr == 0) printf("Case #%d: Draw\n", t);
        else if(up1 != 1 && dw2 != 1 && ctr != 0) printf("Case #%d: Game has not completed\n", t);
        getchar();

    }
    return 0;
}
