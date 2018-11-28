#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <assert.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <functional>
#include <vector>
#include <deque>
#include <utility>
#include <bitset>

using namespace std;
typedef long long ll;
const int INF = 987654321;
const ll LINF = 1e15;

int TC, TCC;
char Map[5][5];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int i, j, k;

    scanf("%d", &TC);
    while(++TCC <= TC) {
        printf("Case #%d: ", TCC);

        bool left = false;
        for(i = 0; i < 4; i++) {
            scanf("%s", Map[i]);
            for(j = 0; j < 4; j++) if(Map[i][j] == '.') left = true;
        }

        bool OW = false, XW = false;

        for(i = 0; i < 4; i++) {
            int count[2] = {0,0};
            for(j = 0; j < 4; j++) {
                if(Map[i][j] == 'O') ++count[0];
                else if(Map[i][j] == 'X') ++count[1];
                else if(Map[i][j] == 'T') ++count[0], ++count[1];
            }
            if(count[0] == 4) OW = true;
            if(count[1] == 4) XW = true;
        }

        for(i = 0; i < 4; i++) {
            int count[2] = {0,0};
            for(j = 0; j < 4; j++) {
                if(Map[j][i] == 'O') ++count[0];
                else if(Map[j][i] == 'X') ++count[1];
                else if(Map[i][j] == 'T') ++count[0], ++count[1];
            }
            if(count[0] == 4) OW = true;
            if(count[1] == 4) XW = true;
        }

        {
            int count[2] = {0, 0};
            for(i = 0; i < 4; i++) {
                if(Map[i][i] == 'O') ++count[0];
                else if(Map[i][i] == 'X') ++count[1];
                else if(Map[i][i] == 'T') ++count[0], ++count[1];
            }
            if(count[0] == 4) OW = true;
            if(count[1] == 4) XW = true;
        }

        {
            int count[2] = {0, 0};
            for(i = 0; i < 4; i++) {
                if(Map[i][3-i] == 'O') ++count[0];
                else if(Map[i][3-i] == 'X') ++count[1];
                else if(Map[i][3-i] == 'T') ++count[0], ++count[1];
            }
            if(count[0] == 4) OW = true;
            if(count[1] == 4) XW = true;
        }

        if(OW && XW) puts("Draw");
        else if(OW) puts("O won");
        else if(XW) puts("X won");
        else puts(left ? "Game has not completed" : "Draw");
    }
    return 0;
}
