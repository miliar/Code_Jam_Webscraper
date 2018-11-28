#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

const char str[] = "welcome to code jam";

char word[1000];

int dp[510][30];

int dfs(int x, int y)
{
    if (y < 0) return 1;
    if (x < 0) return 0;
    int &res = dp[x][y];
    if (res > -1) return res;
    res = 0;
    res += dfs(x - 1, y);
    if (word[x] == str[y]) {
        res += dfs(x - 1, y - 1);
    }
    res %= 10000;
    return res;
}
int main()
{
    //freopen("C-large.in", "r", stdin);
    //freopen("C-large.out", "w", stdout);
    int len = strlen(str);
    int N;
    scanf("%d", &N);
    fgets(word, 1000, stdin);
    for (int t = 1; t <= N; ++t) {
        fgets(word, 1000, stdin);
        int n = strlen(word);
        while (n > 0 && (word[n - 1] == '\r' || word[n - 1] == '\n')) n--;
        word[n] = 0;
        memset(dp, -1, sizeof(dp));
        int ans = dfs(n - 1, len - 1);
        printf("Case #%d: %.4d\n", t, ans);
    }
    return 0;
}
