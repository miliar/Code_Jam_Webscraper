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
# define MAXN 200
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

double dif(double a, double b)
{
    return fabs(a - b);
}

int main()
{
    int t, c, d, p, v, tt, i, j, len;
    PII iniPos[MAXN];
    double ini, fin, med, finPos;

    tt = 1;
    cin >> t;
    while(t--) {
        cin >> c >> d;
        len = 0;

        FOR (i, 0, c) {
            cin >> p >> v;
            iniPos[len++] = make_pair(p, v);
        }

        sort(iniPos, iniPos + len);

        ini = 0.0;
        fin = 1000000000000000.0;
        while(fabs(fin - ini) > 1e-9) {
            med = (ini + fin) / 2.0;
            //cout << ini << " " << fin << endl;

            FOR (i, 0, len) {
                FOR (j, 0, iniPos[i].SN) {
                    if (i == 0 && j == 0) {
                        finPos = double(iniPos[i].FS) - med;
                    }
                    else {
                        //cout << finPos << endl;
                        if (dif(finPos + double(d), double(iniPos[i].FS)) > med) {
                            if (finPos < double(iniPos[i].FS)) {
                                if (dif(finPos, double(iniPos[i].FS) - med) < double(d)) {
                                    break;
                                }
                                else {
                                    finPos = double(iniPos[i].FS) - med;
                                }
                            }
                            else {
                                break;
                            }
                        }
                        else {
                            finPos = finPos + double(d);
                        }
                    }
                }

                if (j < iniPos[i].SN) {
                    break;
                }
            }

            if (i == len) {
                fin = med;
            }
            else {
                ini = med;
            }
        }

        printf("Case #%d: %.6f\n", tt++, ini);
    }
    return 0;
}
