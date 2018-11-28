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

int tt, p, now, f[2][1100][13], nn, pri[1100], m[1100];
int main()
    {
        freopen("B-large(1).in", "r", stdin);
        freopen("B-large(1).out", "w", stdout);
        cin >> tt;
        for (int ca = 1; ca <= tt; ca++)
            {
                cin >> p;
                nn = (1 << p);
                memset(f, -1, sizeof(f));
                for (int i = 0; i < nn; i++)
                    {
                        scanf("%d", &m[i]);
                        m[i] = p - m[i];
                    }
                now = 0;
                for (int i = 0; i < nn; i++)
                    f[0][i][m[i]] = 0;
                nn /= 2;
                while (nn)
                    {
                        now ^= 1;
                        memset(f[now], -1, sizeof(f[now]));
                        for (int i = 0; i < nn; i++)
                            scanf("%d", &pri[i]);
                        for (int i = 0; i < nn; i++)
                            for (int k1 = 0; k1 <= 10; k1++)
                                for (int k2 = 0; k2 <= 10; k2++)
                                    if (f[now ^ 1][i * 2][k1] != -1
                                    && f[now ^ 1][i * 2 + 1][k2] != -1)
                                        if (f[now][i][max(k1, k2)] == -1 ||
                                        f[now][i][max(k1, k2)] > f[now ^ 1][i * 2][k1] + f[now ^ 1][i * 2 + 1][k2])
                                            {
                                                f[now][i][max(k1, k2)] = f[now ^ 1][i * 2][k1] + f[now ^ 1][i * 2 + 1][k2];
                                            }
                        for (int i = 0; i < nn; i++)
                            for (int k1 = 0; k1 <= 10; k1++)
                                for (int k2 = 0; k2 <= 10; k2++)
                                    if (f[now ^ 1][i * 2][k1] != -1
                                    && f[now ^ 1][i * 2 + 1][k2] != -1)
                                        if (f[now][i][max(max(k1, k2) - 1, 0)] == -1 ||
                                        f[now][i][max(max(k1, k2) - 1, 0)] > f[now ^ 1][i * 2][k1] + f[now ^ 1][i * 2 + 1][k2] + pri[i])
                                            {
                                                f[now][i][max(max(k1, k2) - 1, 0)] = f[now ^ 1][i * 2][k1] + f[now ^ 1][i * 2 + 1][k2] + pri[i];
                                            }
                        nn /= 2;
                    }
                printf("Case #%d: ", ca);
                printf("%d\n", f[now][0][0]);
            }
    }
