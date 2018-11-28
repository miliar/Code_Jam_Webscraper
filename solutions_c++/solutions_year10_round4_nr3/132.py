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

const int fx[2] = {-1, 0};
const int fy[2] = {0, -1};
int tt, n, now, ax, ay, bx, by;
bool f[2][110][110];
int main()
    {
        freopen("C-small-attempt0.in", "r", stdin);
        freopen("C-small-attempt0.out", "w", stdout);
        cin >> tt;
        for (int ca = 1; ca <= tt; ca++)
            {
                cin >> n;
                now = 0;
                for (int i = 0; i < n; i++)
                    {
                        scanf("%d%d%d%d", &ax, &ay, &bx, &by);
                        if (ax > bx)
                            swap(ax, bx);
                        if (ay > by)
                            swap(ay, by);
                        for (int x = ax; x <= bx; x++)
                            for (int y = ay; y <= by; y++)
                                f[0][x][y] = 1;
                    }
                bool flag = 1;
                int nn = 0;
                while (flag)
                    {
                        flag = 0;
                        now ^= 1;
                        memset(f[now], 0, sizeof(f[now]));
                        for (int x = 1; x <= 100; x++)
                            for (int y = 1; y <= 100; y++)
                                if (f[now ^ 1][x][y] == 1)
                                    {
                                        bool can = 0;
                                        for (int k = 0; k < 2; k++)
                                            {
                                                int tx = x + fx[k];
                                                int ty = y + fy[k];
                                                if (1 <= tx && 1 <= ty)
                                                    {
                                                        if (f[now ^ 1][tx][ty] == 1)
                                                            can = 1;
                                                    }
                                            }
                                        if (can)
                                            {
                                                f[now][x][y] = 1;
                                                flag = 1;
                                            }
                                    }
                        for (int x = 1; x <= 100; x++)
                            for (int y = 1; y <= 100; y++)
                                if (f[now ^ 1][x][y] == 0)
                                    {
                                        bool can = 1;
                                        for (int k = 0; k < 2; k++)
                                            {
                                                int tx = x + fx[k];
                                                int ty = y + fy[k];
                                                if (1 <= tx && 1 <= ty)
                                                    {
                                                        if (f[now ^ 1][tx][ty] != 1)
                                                            can = 0;
                                                    }
                                                else
                                                    can = 0;
                                            }
                                        if (can)
                                            {
                                                f[now][x][y] = 1;
                                                flag = 1;
                                            }
                                    }
                        nn++;
                    }
                printf("Case #%d: ", ca);
                printf("%d\n", nn);
            }
    }
