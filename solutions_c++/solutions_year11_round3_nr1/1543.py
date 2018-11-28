# include <iostream>
# include <cstdio>
# include <cstdlib>
# include <cmath>
# include <vector>
# include <string>
# include <stack>
# include <queue>
# include <set>
# include <map>
# include <numeric>
# include <functional>
# include <cstring>
# include <algorithm>
# include <utility>
# include <list>
# include <cctype>
# include <exception>
# include <ctime>
# include <iterator>
# include <sstream>
# include <fstream>
# include <iomanip>
# define FOR(i, n, m) for (i = (n); i < (m); i++)
# define FORR(i, n, m) for (i = (n); i >= (m); i--)
# define LLI long long int
# define ULL unsigned long long
# define PII pair < int, int >
# define VI vector < int >
# define FS first
# define SN second
# define PB push_back
# define ALL(v) v.begin(), v.end()
# define INF 0x3f3f3f3f
# define ISDIG(c) (c >= '0' && c <= '9')
# define MAXN 50
using namespace std;

int read()
{
    int n;
    int mult;
    char c;

    n = 0;
    mult = 1;
    for (c = getchar(); !ISDIG(c) && c != '-'; c = getchar());

    if (c == '-') {
        mult = -1;
        c = getchar();
    }

    while(ISDIG(c)) {
        n = n * 10 + c - '0';
        c = getchar();
    }

    return mult * n;
}

int main()
{
    int t, r, c, tt, i, j;
    char v[3] = "/\\";
    string str[MAXN];
    int tab[MAXN][MAXN];

    cin >> t;
    tt = 1;
    while(t--) {
        cin >> r >> c;

        FOR (i, 0, r) {
            cin >> str[i];
        }

        memset(tab, -1, sizeof tab);
        FOR (i, 0, r) {
            FOR (j, 0, c) {
                if (str[i][j] == '#') {
                    if (i + 1 < r && j + 1 < c &&
                        tab[i][j] == -1 &&
                        tab[i][j + 1] == -1 && str[i][j + 1] == '#' &&
                        tab[i + 1][j] == -1 && str[i + 1][j] == '#' &&
                        tab[i + 1][j + 1] == -1 && str[i + 1][j + 1] == '#'
                    ) {
                        tab[i][j] = 0;
                        tab[i][j + 1] = 1;
                        tab[i + 1][j] = 1;
                        tab[i + 1][j + 1] = 0;
                    }
                }
            }
        }

        FOR (i, 0, r) {
            FOR (j, 0, c) {
                if (tab[i][j] == -1 && str[i][j] == '#') {
                    break;
                }
            }

            if (j < c) {
                break;
            }
        }

        if (i < r) {
            printf("Case #%d:\nImpossible\n", tt++);
            continue;
        }

        printf("Case #%d:\n", tt++);
        FOR (i, 0, r) {
            FOR (j, 0, c) {
                if (str[i][j] == '#') {
                    putchar(v[tab[i][j]]);
                }
                else {
                    putchar(str[i][j]);
                }
            }
            puts("");
        }
    }
    
    return 0;
}
