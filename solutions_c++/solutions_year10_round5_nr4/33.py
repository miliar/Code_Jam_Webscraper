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

int ans = 0, js[20][20], n, b;
void dfs(int s, int b, int mi)
    {
        if (s == 0)
            {
                ans++;
/*                for (int i = 1; i <= 10; i++)
                    cout << js[1][i] << ' ';
                cout << endl;*/
                return;
            }
        for (int i = mi; i <= s; i++)
            {
                bool flag = 1;
                int tmp = i, co = 1;
                while (tmp)
                    {
                        js[co][tmp % b]++;
                        if (js[co][tmp % b] > 1)
                            flag = 0;
                        tmp /= b;
                        co++;
                    }
                if (flag)
                    dfs(s - i, b, i + 1);
                tmp = i, co = 1;
                while (tmp)
                    {
                        js[co][tmp % b]--;
                        tmp /= b;
                        co++;
                    }
            }
    }
int tt;
int main()
    {
        freopen("D-small-attempt0.in", "r", stdin);
        freopen("D-small-attempt0.out", "w", stdout);
        cin >> tt;
        for (int ca = 1; ca <= tt; ca++)
            {
                cin >> n >> b;
                memset(js, 0, sizeof(js));
                ans = 0;
                dfs(n, b, 1);
                
                printf("Case #%d: ", ca);
                printf("%d\n", ans);
            }
    }
