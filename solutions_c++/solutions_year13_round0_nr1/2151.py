#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int main()
{
    int n;
    int ans[4] = {0};
    scanf("%d", &n);
    getchar();

    ans[0] = (int)(4 *'X');
    ans[1] = (int)(3 *'X' + 'T');
    ans[2] = (int)(4 *'O');
    ans[3] = (int)(3 *'O' + 'T');

    for(int k = 1; k <= n ; k++) {
        int flag = 0;
        int ctr = 0;
        char tac[4][4];
        char a;
        int b[10] = {0};

        for(int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%c", &tac[i][j]);
                b[i] = b[i] + (int)tac[i][j];
                if(i == j) b[4] = b[4] + (int)tac[i][j];
                else if (j == 3-i) b[5] = b[5] + (int)tac[i][j];

                if(tac[i][j] == '.') ctr++;
            }

            getchar();
        }

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                b[6+i] = b[6+i] + (int)tac[j][i];
            }
        }

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 4; j++) {
                if (b[i] == ans[j]) {
                    if (j == 0 || j == 1) {
                        printf("Case #%d: X won\n", k);
                        flag = 1;
                        break;
                    }

                    else if (j == 2 || j == 3) {
                         printf("Case #%d: O won\n", k);
                         flag = 1;
                         break;
                    }

                }
            }

            if(flag == 1) {
                break;
            }
        }

        if (flag == 0) {
            if (ctr == 0) {
                printf("Case #%d: Draw\n",k);
            } else {
                printf("Case #%d: Game has not completed\n", k);
            }
        }

        getchar();
    }

    return 0;
}
