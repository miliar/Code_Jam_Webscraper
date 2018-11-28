#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

char s[10][10], num_o, num_x, num_t;
bool h_o, h_x, h_d;

int main(){
    freopen("a.txt", "w", stdout);

    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas ++){
        //getchar();
        for (int i = 1; i <= 4; i ++){
            for (int j = 1; j <= 4; j ++)
                scanf("%c", &s[i][j]);
            //getchar();
            }

        h_o = false;
        h_x = false;
        h_d = true;
        for (int i = 1; i <= 4; i ++){
            num_o = 0;
            num_x = 0;
            num_t = 0;
            for (int j = 1; j <= 4; j ++){
                if (s[i][j] == 'O') num_o ++;
                if (s[i][j] == 'X') num_x ++;
                if (s[i][j] == 'T') num_t ++;
                if (s[i][j] == '.') h_d = false;
                }
            if (num_o >= 3 && num_t == 4 - num_o) h_o = true;
            if (num_x >= 3 && num_t == 4 - num_x) h_x = true;
            }
        for (int j = 1; j <= 4; j ++){
            num_o = 0;
            num_x = 0;
            num_t = 0;
            for (int i = 1; i <= 4; i ++){
                if (s[i][j] == 'O') num_o ++;
                if (s[i][j] == 'X') num_x ++;
                if (s[i][j] == 'T') num_t ++;
                if (s[i][j] == '.') h_d = false;
                }
            if (num_o >= 3 && num_t == 4 - num_o) h_o = true;
            if (num_x >= 3 && num_t == 4 - num_x) h_x = true;
            }
        num_o = 0;
        num_x = 0;
        num_t = 0;
        for (int i = 1; i <= 4; i ++)
            for (int j = i; j <= i; j ++){
                if (s[i][j] == 'O') num_o ++;
                if (s[i][j] == 'X') num_x ++;
                if (s[i][j] == 'T') num_t ++;
                if (s[i][j] == '.') h_d = false;
                }
        if (num_o >= 3 && num_t == 4 - num_o) h_o = true;
        if (num_x >= 3 && num_t == 4 - num_x) h_x = true;
        num_o = 0;
        num_x = 0;
        num_t = 0;
        for (int i = 1; i <= 4; i ++)
            for (int j = 5 - i; j <= 5 - i; j ++){
                if (s[i][j] == 'O') num_o ++;
                if (s[i][j] == 'X') num_x ++;
                if (s[i][j] == 'T') num_t ++;
                if (s[i][j] == '.') h_d = false;
                }
        if (num_o >= 3 && num_t == 4 - num_o) h_o = true;
        if (num_x >= 3 && num_t == 4 - num_x) h_x = true;
        if (h_o == true) printf("Case #%d: O won\n", cas);
                    else if (h_x == true) printf("Case #%d: X won\n", cas);
                                     else if (h_d == true) printf("Case #%d: Draw\n", cas);
                                                      else printf("Case #%d: Game has not completed\n", cas);
        }

    fclose(stdout);

    return 0;
}
