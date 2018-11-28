#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int T,n,a[1005];

int calc(int LF,int RF)
{
    vector< pair<int,int> > store;
    for (int i = LF; i <= RF; i++)
    {
        int pos = -1,best = n + 2;
        for (int j = 0; j < store.size(); j++) if (a[i] - store[j].first == 1 && store[j].second < best)
        {
            best = store[j].second;  pos = j;
        }
        if (pos < 0) store.push_back(make_pair(a[i],1)); else
        {
            store[pos].first++;  store[pos].second++;
        }
    }
    int ans = n;
    for (int i = 0; i < store.size(); i++) ans = min(ans,store[i].second);
    return ans;
}

int main()
{
    freopen("b.i2","r",stdin);
    freopen("b.o2","w",stdout);

    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
        printf("Case #%d: ", it);
        scanf("%d", &n);
        if (!n) printf("0\n"); else
        {
            for (int i = 0; i < n; i++) scanf("%d", &a[i]);
            sort(a,a + n);
            int LF = 0,ret = n;
            while (LF < n)
            {
                int RF = LF + 1;
                while (RF < n && a[RF] - a[RF - 1] < 2) RF++;
                ret = min(ret,calc(LF,RF - 1));
                LF = RF;
            }
            printf("%d\n", ret);
        }
    }
}
