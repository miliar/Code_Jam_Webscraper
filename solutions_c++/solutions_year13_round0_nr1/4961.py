#include <cstdio>

char mp[10][10];

int judge(char a, char b, char c, char d) {
    int x = (a == 'X') + (b == 'X') + (c == 'X') + (d == 'X');
    int o = (a == 'O') + (b == 'O') + (c == 'O') + (d == 'O');
    int t = (a == 'T') + (b == 'T') + (c == 'T') + (d == 'T');
    if ((x == 3 && t == 1) || (x == 4)) return 1;
    else if ((o == 3 && t == 1) || (o == 4)) return -1;
    else return 0;
}

int solve() {
    int ans;
    for (int i = 0; i < 4; i++) {
        if ((ans = judge(mp[i][0], mp[i][1], mp[i][2], mp[i][3])) != 0)
            return ans;
        if ((ans = judge(mp[0][i], mp[1][i], mp[2][i], mp[3][i])) != 0)
            return ans;
    }
    if ((ans = judge(mp[0][0], mp[1][1], mp[2][2], mp[3][3])) != 0)
        return ans;
    if ((ans = judge(mp[0][3], mp[1][2], mp[2][1], mp[3][0])) != 0)
        return ans;
    return 0;
}

int main() {
    freopen("in.txt", "r", stdin);
   freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        for (int i = 0; i < 4; i++)
            scanf(" %s", mp[i]);

        int ans = solve();
        if (ans == 1) printf("Case #%d: X won\n", cas);
        else if (ans == -1) printf("Case #%d: O won\n", cas);
        else {
            int cnt = 0;
            for (int i = 0; i < 4; i++)
                for (int j = 0; j < 4; j++)
                    cnt += mp[i][j] == '.';
            if (cnt == 0) printf("Case #%d: Draw\n", cas);
            else printf("Case #%d: Game has not completed\n", cas);
        }
    }
}