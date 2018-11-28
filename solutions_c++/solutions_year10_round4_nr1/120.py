#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

#define PB push_back
#define MP make_pair

int tt, n, ma[500][500];
char st[10000];
int edis(int ax, int ay, int bx, int by)
    {
        return abs(ax - bx) + abs(ay - by);
    }
int main()
    {
        freopen("A-large(1).in", "r", stdin);
        freopen("A-large(1).out", "w", stdout);
    //    freopen("in.txt", "r", stdin);
      //  freopen("out.txt", "w", stdout);
        cin >> tt;
        for (int ca = 1; ca <= tt; ca++)
            {
                cin >> n;
                memset(st, 0, sizeof(st));
                gets(st);
                for (int i = 1; i <= n * 2 - 1; i++)
                    {
                        gets(st);
                        for (int j = 1; j <= n * 2 - 1; j++)
                            if (st[j - 1] == ' ' || st[j - 1] == '\0')
                                ma[i][j] = -1992837465;
                            else
                                ma[i][j] = st[j - 1] - '0';
                    }
                int mi = 1992837465;
                for (int i = 1; i <= n * 2 - 1; i++)
                    for (int j = 1; j <= n * 2 - 1; j++)
                        {
                            bool flag = 0;
                            for (int X = 1; X <= n * 2 - 1; X++)
                                {
                                    int h1 = j - 1, h2 = j + 1;
                                    while (1 <= h1 && h2 <= n * 2 - 1 && (ma[X][h1] == ma[X][h2]
                                    || ma[X][h1] == -1992837465 || ma[X][h2] == -1992837465))
                                        {
                                            h1--;
                                            h2++;
                                        }
                                    if (1 <= h1 && h2 <= n * 2 - 1)
                                        {
                                            flag = 1;
                                            break;
                                        }
                                }
                            for (int Y = 1; Y <= n * 2 - 1; Y++)
                                {
                                    int h1 = i - 1, h2 = i + 1;
                                    while (1 <= h1 && h2 <= n * 2 - 1 && (ma[h1][Y] == ma[h2][Y]
                                    || ma[h1][Y] == -1992837465 || ma[h2][Y] == -1992837465))
                                        {
                                            h1--;
                                            h2++;
                                        }
                                    if (1 <= h1 && h2 <= n * 2 - 1)
                                        {
                                            flag = 1;
                                            break;
                                        }
                                }
                            if (!flag)
                                {
                                    int he = (edis(1, n, i, j) * 2 + 2) / 2;
                                    he = max(he, (edis(n * 2 - 1, n, i, j) * 2 + 2) / 2);
                                    int sh = (edis(n, 1, i, j) * 2 + 2) / 2;
                                    sh = max(sh, (edis(n, n * 2 - 1, i, j) * 2 + 2) / 2);
//                                    int he = max((i + (i - 1) + 1) / 2, (n * 2 - 1 - (i - (n * 2 - 1 - i)) + 1 + 1) / 2);
  //                                  int sh = max((j + (j - 1) + 1) / 2, (n * 2 - 1 - (j - (n * 2 - 1 - j)) + 1 + 1) / 2);
                                    mi = min(mi, max(he, sh));
//                                    cout << i << ' ' << j << ' ' << he << ' ' << sh << endl;
                                }
                        }
                printf("Case #%d: ", ca);
                printf("%d\n", mi * mi - n * n);
            }
    }

