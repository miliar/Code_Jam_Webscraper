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

int L, D, N;
char word[5001][20];
bool setit[20][26];
char tmp[10000];
int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    scanf("%d%d%d", &L, &D, &N);
    for (int i = 0; i < D; ++i)
        scanf("%s", word[i]);
    for (int k = 1; k <= N; ++k) {
        scanf("%s", tmp);
        memset(setit, false, sizeof(setit));
        int a = 0;
        int len = strlen(tmp);
        int c = 0;
        while (a < len) {
            if (tmp[a] == '(') {
                a++;
                while (a < len && tmp[a] != ')') {
                    setit[c][tmp[a] - 'a'] = true;
                    a++;
                }
                a++;
            } else {
                setit[c][tmp[a] - 'a'] = true;
                a++;
            }
            c++;
        }
        int ans = 0;
        bool yes;
        for (int i = 0; i < D; ++i) {
            yes = true;
            for (int j = 0; j < L; ++j) {
                if (!setit[j][word[i][j] - 'a']) {
                    yes = false;
                    break;
                }
            }
            if (yes) ans++;
        }
        printf("Case #%d: %d\n", k, ans);
    }
    return 0;
}
