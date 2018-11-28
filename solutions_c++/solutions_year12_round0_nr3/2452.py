# include <iostream>
# include <cmath>
# include <cstdio>
# include <cstring>
# include <cstdlib>
# include <cctype>
# include <ctime>
# include <string>
# include <vector>
# include <queue>
# include <stack>
# include <functional>
# include <numeric>
# include <algorithm>
# include <list>
# include <map>
# include <set>
# include <iterator>
# include <utility>
# include <sstream>
# include <fstream>
# include <iomanip>
# include <exception>
# include <cassert>
# define FOR(i, n, m) for (i = (n); i < (m); i++)
# define FORR(i, n, m) for (i = (n); i >= (m); i--)
# define LLI long long int
# define ULL unsigned long long
# define PII pair < int, int >
# define MP make_pair
# define VI vector < int >
# define VS vector < string >
# define SS stringstream
# define FS first
# define SN second
# define PB push_back
# define BE begin
# define EN end
# define CL(v, val) memset(v, val, sizeof v)
# define ALL(v) v.begin(), v.end()
# define INF 0x3f3f3f3f
# define ISDIG(c) (c >= '0' && c <= '9')
using namespace std;

int read()
{
    int n;
    char c;
    bool neg;

    n = 0;
    neg = false;

    for (c = getchar(); !ISDIG(c) && c != '-'; c = getchar());

    if (c == '-') {
        neg = true;
        c = getchar();
    }

    while(ISDIG(c)) {
        n = n * 10 + c - '0';
        c = getchar();
    }

    return neg ? -n : n;
}

int main()
{
    int i, j, k, l, n, a, b, t, tt, ans, temp;
    char str[10], str2[10];
    set < int > s;

    scanf("%d", &t);
    tt = 1;
    while(t--) {
        ans = 0;

        scanf("%d%d", &a, &b);
        FOR (i, a, b + 1) {
            sprintf(str, "%d", i);
            n = strlen(str);

            if (n > 1) {
                s.clear();
                FOR (j, 0, n - 1) {
                    l = 0;
                    FOR (k, j + 1, n) {
                        str2[l++] = str[k];
                    }
                    FOR (k, 0, j + 1) {
                        str2[l++] = str[k];
                    }
                    str2[l] = '\0';

                    sscanf(str2, "%d", &temp);
                    if (s.find(temp) == s.end() && temp <= b && temp > i) {
                        ans++;
                        s.insert(temp);
                    }
                }
            }
        }

        printf("Case #%d: %d\n", tt++, ans);
    }

    return 0;
}
