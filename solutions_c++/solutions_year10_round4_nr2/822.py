#include <algorithm>
#include <bitset>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
typedef long long ll;
using namespace std;

bool chs[3000];
int p,miss[3000];

int main()
{
    freopen("b.i1","r",stdin);
    freopen("b.o1","w",stdout);
    int T;
    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
        scanf("%d", &p);
        int x;
        for (int i = 0; i < (1 << p); i++) scanf("%d", &miss[i]);
        for (int i = 1; i < (1 << p); i++) scanf("%d", &x);
        memset(chs,false,sizeof(chs));
        
        for (int i = 0; i < (1 << p); i++)
        {
            int last = ((1 << p) + i)/2;
            while (miss[i])
            {
                  miss[i]--;  last /= 2;
            };
            while (last)
            {
                  chs[last] = true;  last /= 2;
            };
        };
        
        int ret = 0;
        for (int i = 1; i < (1 << (p + 1)); i++) if (chs[i]) ret++;
        printf("Case #%d: %d\n", it, ret);
    };
};
