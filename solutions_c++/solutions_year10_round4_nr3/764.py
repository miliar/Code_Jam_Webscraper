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

int n;
int a[102][102],b[102][102];

int main()
{
    freopen("c.i1","r",stdin);
    freopen("c.o1","w",stdout);
    int T;
    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
        printf("Case #%d: ", it);
        scanf("%d", &n);
        memset(a,0,sizeof(a));
        int r = 100,c = 100;
        for (int i = 0; i < n; i++)
        {
            int x1,x2,y1,y2;
            scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
//            cout << x1 << y1 << x2 << y2 << endl;
            for (int j = x1; j <= x2; j++)
              for (int k = y1; k <= y2; k++) a[j][k] = 1;
        };
        int ret = 0;
//      cout << "input completed" << endl;
//        cout << r << ' ' << c << endl;
        while (1)
        {
              ret++;
              memset(b,0,sizeof(b));
              bool flag = false;
              for (int i = 1; i <= r; i++)
                for (int j = 1; j <= c; j++)
                {
                    if (!a[i - 1][j] && !a[i][j - 1]) b[i][j] = 0;
                    else if (a[i - 1][j] && a[i][j - 1]) b[i][j] = 1;
                    else if (a[i][j]) b[i][j] = 1;
                    if (b[i][j]) flag = true;
                };
              if (!flag) break;
              for (int i = 1; i <= r; i++)
                for (int j = 1; j <= c; j++) a[i][j] = b[i][j];
        };
        printf("%d\n", ret);
    };
};
