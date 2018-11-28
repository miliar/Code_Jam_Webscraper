#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int dp[6][6][4][3];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int cases, i, j, winner;
    bool not_finished;
    char c;
    string ans;

    memset(dp, 0, sizeof(dp));

    scanf("%d\n", &cases);
    for (int test_case = 1; test_case <= cases; test_case++) {

        not_finished = false;
        winner = 0;

        for (j = 1; j <= 4; j++) {
            for (i = 1; i <= 4; i++) {
                scanf("%c", &c);
                if (c == '.') not_finished = true;
                dp[i][j][0][1] = (c == 'X' || c == 'T') ? dp[i-1][j][0][1] + 1 : 0;
                dp[i][j][0][2] = (c == 'O' || c == 'T') ? dp[i-1][j][0][2] + 1 : 0;
                dp[i][j][1][1] = (c == 'X' || c == 'T') ? dp[i][j-1][1][1] + 1 : 0;
                dp[i][j][1][2] = (c == 'O' || c == 'T') ? dp[i][j-1][1][2] + 1 : 0;
                dp[i][j][2][1] = (c == 'X' || c == 'T') ? dp[i-1][j-1][2][1] + 1 : 0;
                dp[i][j][2][2] = (c == 'O' || c == 'T') ? dp[i-1][j-1][2][2] + 1 : 0;
                dp[i][j][3][1] = (c == 'X' || c == 'T') ? dp[i+1][j-1][3][1] + 1 : 0;
                dp[i][j][3][2] = (c == 'O' || c == 'T') ? dp[i+1][j-1][3][2] + 1 : 0;
            }
            scanf("%c", &c);
        }

        scanf("%c", &c);

        for (int player = 1; player <= 2; player++)
            for (int direction = 0; direction <= 3; direction++)
                for (i = 1; i <= 4; i++)
                    for (j = 1; j <= 4; j++)
                        if (dp[i][j][direction][player] == 4)
                            winner = player;

    ans.clear();
    if (winner == 0) {
        if (not_finished)
            ans = "Game has not completed";
        else
            ans = "Draw";
    } else {
        ans = ans + ((winner == 1) ? 'X' : 'O') + " won";
    }
    printf("Case #%d: %s\n", test_case, ans.c_str());

    }
}
