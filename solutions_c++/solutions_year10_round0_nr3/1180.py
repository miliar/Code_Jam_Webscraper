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

long long tt, r, k, n;
long long g[1100], bl[1100], us[1100];
int main()
    {
        freopen("C-large.in", "r", stdin);
        freopen("C-large.out", "w", stdout);
        cin >> tt;
        for (int nu = 1; nu <= tt; nu++)
            {
                cin >> r >> k >> n;
                long long su = 0;
                for (long long i = 0; i < n; i++)
                    {
                        int a1;
                        scanf("%d", &a1);
                        g[i] = a1;
                        su += (long long)g[i];
                    }
                long long ans;
                if (su <= k)
                    ans = (long long)r * (long long)su;
                else
                    {
                        memset(bl, -1, sizeof(bl));
                        ans = 0;
                        long long st = 0, nr = r, co = 0;
                        while (bl[st] == -1 && r)
                            {
                                bl[st] = co;
                                us[st] = r;
                                long long now = 0;
                                for (long long i = 0; i < n; i++)
                                    {
                                        long long id = (i + st) % n;
                                        if (now + g[id] > k)
                                            {
                                                st = id;
                                                break;
                                            }
                                        now += g[id];
                                        co += g[id];
                                        ans += g[id];
                                    }
                                r--;
                            }
                        if (r != 0)
                            {
                                long long del = us[st] - r, cost = co - bl[st];
                                ans += (long long)(r / del) * (long long)cost;
                                r %= del;
                                while (r)
                                    {
                                        long long now = 0;
                                        for (long long i = 0; i < n; i++)
                                            {
                                                long long id = (i + st) % n;
                                                if (now + g[id] > k)
                                                    {
                                                        st = id;
                                                        break;
                                                    }
                                                now += g[id];
                                                ans += g[id];
                                            }
                                        r--;
                                    }
                            }
                    }
                printf("Case #%d: ", nu);
                cout << ans << endl;
            }
    }
