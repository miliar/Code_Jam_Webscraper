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
# define MAXN 100
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

int tab[MAXN][MAXN];

int main()
{
    int t, n, i, j, k, tt, aux;
    double temp, temp2;
    int p[MAXN];
    vector < PII > wp;
    vector < double > owp, oowp;
    string str;

    tt = 1;
    cin >> t;
    while(t--) {
        wp.clear();
        owp.clear();
        oowp.clear();
        cin >> n;

        FOR (i, 0, n) {
            cin >> str;
            p[i] = 0;
            FOR (j, 0, n) {
                if (str[j] == '.') {
                    tab[i][j] = -1;
                }
                else if (str[j] == '0') {
                    tab[i][j] = 0;
                    p[i]++;
                }
                else {
                    tab[i][j] = 1;
                    p[i]++;
                }
            }
        }

        // WP
        FOR (i, 0, n) {
            k = 0;
            FOR (j, 0, n) {
                if (tab[i][j] == 1) {
                    k++;
                }
            }

            wp.PB(make_pair(k, p[i]));
        }

        // OWP
        FOR (i, 0, n) {
            k = 0;
            temp = 0.0;
            FOR (j, 0, n) {
                if (tab[i][j] != -1) {
                    if (tab[i][j] == 1) {
                        if (p[j] > 1) {
                            aux = p[j] / wp[j].SN;
                            temp2 = double(wp[j].FS * aux) / double(p[j] - 1);
                            temp += temp2;
                        }
                    }
                    else {
                        if (p[j] > 1 && wp[j].FS * aux >= 1) {
                            aux = p[j] / wp[j].SN;
                            temp2 = double(wp[j].FS * aux - 1) / double(p[j] - 1);
                            temp += temp2;
                        }
                    }
                    k++;
                }
            }

            //cout << temp.FS << "  " << temp.SN << endl;
            if (k != 0) {
                owp.PB(double(temp) / double(k));
            }
        }

        // OOWP
        FOR (i, 0, n) {
            k = 0;
            temp = 0.0;
            FOR (j, 0, n) {
                if (tab[i][j] != -1) {
                    temp += owp[j];
                    k++;
                }
            }

            oowp.PB(double(temp) / double(k));
        }

        printf("Case #%d:\n", tt++);
        FOR (i, 0, n) {
            temp = 0.0;

            temp = 0.25 * double(wp[i].FS) / double(wp[i].SN);
            temp += 0.5 * owp[i];
            temp += 0.25 * oowp[i];

            printf("%.12f\n", temp);
        }
    }

    return 0;
}
