#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int T,statue1,statue2,statue3,statue4,win;
char a[5][5],ch;
bool flag;
int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>T; scanf("%c",&ch);
    for (int kase = 1;kase <= T; kase++) {
        flag = true; win = 0;
        for (int i = 1;i <= 4; i++){
            for (int j = 1;j <= 4; j++){
                scanf("%c",&a[i][j]);
                if (a[i][j] == '.') flag = false;
            }
            scanf("%c",&ch);
        }
        scanf("%c",&ch);
        for (int i = 1;i <= 4; i++){
            statue1 = 0; statue2 = 0; statue3 = 0; statue4 = 0;
            for (int j = 1;j <= 4; j++) {
                if (a[i][j] == 'X' || a[i][j] == 'T') statue1++;
                if (a[i][j] == 'O' || a[i][j] == 'T') statue2++;
                if (a[j][i] == 'X' || a[j][i] == 'T') statue3++;
                if (a[j][i] == 'O' || a[j][i] == 'T') statue4++;
            }
            if (statue1 == 4 || statue3 == 4) win = 1; else if (statue2 == 4 || statue4 == 4) win = 2;
            if (win) break;
        }
        if (!win) {
           statue1 = 0; statue2 = 0; statue3 = 0; statue4 = 0;
           for (int i = 1;i <= 4; i++){
               if (a[i][i] == 'X' || a[i][i] == 'T') statue1++;
                if (a[i][i] == 'O' || a[i][i] == 'T') statue2++;
                if (a[i][5-i] == 'X' || a[i][5-i] == 'T') statue3++;
                if (a[i][5-i] == 'O' || a[i][5-i] == 'T') statue4++;
           }
            if (statue1 == 4 || statue3 == 4) win = 1; else if (statue2 == 4 || statue4 == 4) win = 2;
        }
        printf("Case #%d: ",kase);
        if (win == 1) printf("X won\n");
        else if (win == 2) printf("O won\n");
        else if (flag) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
