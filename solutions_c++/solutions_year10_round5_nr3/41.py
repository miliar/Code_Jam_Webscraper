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

int tt, n, p, v;
map <int, int> hash[2];
int main()
    {
        freopen("C-small-attempt1.in", "r", stdin);
        freopen("C-small-attempt1.out", "w", stdout);
        cin >> tt;
        for (int ca = 1; ca <= tt; ca++)
            {
                cin >> n;
                hash[0].clear();
                hash[1].clear();
                int nn = 0;
                for (int i = 0; i < n; i++)
                    {
                        scanf("%d%d", &p, &v);
                        hash[0][p] = v;
                    }
                bool mov = 1;
                int ti = 0;
                while (mov)
                    {
                        map <int, int> :: iterator it = hash[nn].begin();
                        nn ^= 1;
                        hash[nn].clear();
                        mov = 0;
                        for (; it != hash[nn ^ 1].end(); it++)
                            {
                                if (it->second == 1)
                                    hash[nn][it->first] += 1;
                                else
                                if (it->second > 1)
                                    {
                                        mov = 1;
                                        hash[nn][it->first + 1] += 1;
                                        hash[nn][it->first - 1] += 1;
                                        hash[nn][it->first] += it->second - 2;
                                        ti++;
                                    }
                            }
                    }
                printf("Case #%d: ", ca);
                printf("%d\n", ti);
            }
    }
