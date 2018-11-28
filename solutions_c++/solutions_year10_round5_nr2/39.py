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

typedef pair <long long, int> Item;
priority_queue <Item, vector<Item>, greater<Item> > dij;
int tt, n, le[200];
long long L, di[100100];
int main()
    {
        freopen("B-large.in", "r", stdin);
        freopen("B-large.out", "w", stdout);
        cin >> tt;
        for (int ca = 1; ca <= tt; ca++)
            {
                cin >> L;
                scanf("%d", &n);
                long long ma = -1992837465;
                for (int i = 0; i < n; i++)
                    {
                        scanf("%d", &le[i]);
                        if (le[i] > ma)
                            ma = le[i];
                    }
                dij.push(MP(L / ma, 0));
                memset(di, -1, sizeof(di));
                di[0] = L / ma;
                while (!dij.empty())
                    {
                        long long d = dij.top().first;
                        int x = dij.top().second;
                        dij.pop();
                        if (di[x] != d)
                            continue;
                        for (int i = 0; i < n; i++)
                            {
                                int tx = (x + le[i]) % ma;
                                long long td;
                                if (x + le[i] >= ma)
                                    td = d + 0;
                                else
                                    td = d + 1;
                                if (di[tx] == -1 || di[tx] > td)
                                    {
                                        di[tx] = td;
                                        dij.push(MP(td, tx));
                                    }
                            }
                    }
                long long D = di[(int)(L % (long long)ma)];
                printf("Case #%d: ", ca);
                if (D == -1)
                    printf("IMPOSSIBLE\n");
                else
                    cout << D << endl;
            }
    }
