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

int tt, l[1000000], d, k, s[100], tot;
bool ss[1010000];
int main()
    {
        freopen("A-small-attempt0.in", "r", stdin);
        freopen("A-small-attempt0.out", "w", stdout);
        cin >> tt;
        for (int i = 2; i <= 1000000; i++)
            if (!ss[i])
                {
                    tot++;
                    l[tot] = i;
                    for (int j = 2; i * j <= 1000000; j++)
                        ss[i * j] = 1;
                }
        for (int ca = 1; ca <= tt; ca++)
            {
                cin >> d >> k;
                int up = 1;
                for (int i = 0; i < d; i++)
                    up *= 10;
                for (int i = 0; i < k; i++)
                    scanf("%d", &s[i]);
                printf("Case #%d: ", ca);
                if (k == 1)
                    {
                        printf("I don't know.\n");
                    }
                else
                    {
                        int next = -1;
                        bool duojie = 0;
                        for (int i = 1; i <= tot; i++)
                            if (l[i] <= up)
                                {
                                    int P = l[i];
                                    bool cant = 0;
                                    for (int j = 0; j < k; j++)
                                        if (s[j] >= P)
                                            {
                                                cant = 1;
                                                break;
                                            }
                                    if (cant)
                                        continue;
                                    for (int A = 0; A <= up; A++)
                                        {
                                            bool flag = 1;
                                            int B = P - ((A * s[0] - s[0 + 1] + P) % P);
                                            for (int j = 1; j < k - 1; j++)
                                                if (P - ((A * s[j] - s[j + 1] + P) % P) != B)
                                                    {
                                                        flag = 0;
                                                        break;
                                                    }
                                            if (flag)
                                                {
                                                    if (next != -1 && next != (A * s[k - 1] + B) % P)
                                                        duojie = 1;
                                                    else
                                                        next = (A * s[k - 1] + B) % P;
                                                }
                                        }
                                }
                        if (duojie)
                            printf("I don't know.\n");
                        else
                            printf("%d\n", next);
                    }
            }
    }
