#include <algorithm>
#include <bitset>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <utility>
using namespace std;

int dx[4] = {1,1,0,-1};
int dy[4] = {0,1,1,1};
int n,k;
char a[60][60],b[60][60],c[60][60];

int main()
{
    freopen("a.i2","r",stdin);
    freopen("a.o2","w",stdout);
    int T;
    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
            printf("Case #%d: ", it);
            scanf("%d %d\n", &n, &k);
//            if (it == 4) cout << n << ' ' << k << endl;
            for (int i = 1; i <= n; i++)
              for (int j = 1; j <= n; j++)
              {
                    a[i][j] = '.';  b[i][j] = '.';  c[i][j] = '.';
              };
            for (int i = 1; i <= n; i++)
              for (int j = 1; j <= n; j++)
              {
                    char ch;
                    while (1)
                    {
                        scanf("%c", &ch);
                        if (ch == '.' || ch == 'R' || ch == 'B') break;
                    };
                    a[i][j] = ch;
              };
/*            if (it == 4)
                for (int i = 1; i <= n; i++)
                {
                    for (int j = 1; j <= n; j++) cout << a[i][j];
                    cout << endl;
                };*/
            //Rotate
            for (int i = 1; i <= n; i++)
              for (int j = 1; j <= n; j++) b[j][n + 1 - i] = a[i][j];
            
/*            for (int i = 1; i <= n; i++)
            {
                for (int j = 1; j <= n; j++) if (b[i][j] != 'R' && b[i][j] != 'B') printf("."); else printf("%c", b[i][j]);
                printf("\n");
            };*/
            //Gravity
            for (int j = 1; j <= n; j++)
            {
               int pos = n; 
               for (int i = n; i > 0; i--)
                 if (b[i][j] == 'B' || b[i][j] == 'R')
                 {
                        c[pos][j] = b[i][j];  pos--;
                 };
            };
/*            for (int i = 1; i <= n; i++)
            {
                for (int j = 1; j <= n; j++) if (c[i][j] != 'R' && c[i][j] != 'B') printf("."); else printf("%c", c[i][j]);
                printf("\n");
            };*/
            
            //Check
            bool wb = false,wr = false;
            for (int i = 1; i <= n; i++)
              for (int j = 1; j <= n; j++) if (c[i][j] == 'R' || c[i][j] == 'B')
                for (int d = 0; d < 4; d++)
                {
                    int t = 0,fx = i,fy = j;
                    while (t < k && 0 < fx && fx <= n && 0 < fy && fy <= n && c[fx][fy] == c[i][j])
                    {
                        t++;  fx += dx[d];  fy += dy[d];
                    };
                    if (t == k)
                    {
                        if (c[i][j] == 'R') wr = true; else wb = true;
//                        cout << i << ' ' << j << endl;
                    };
                };
              
            if (wb && wr) printf("Both");
            if (!wb && wr) printf("Red");
            if (wb && !wr) printf("Blue");
            if (!wb && !wr) printf("Neither");
            printf("\n");
    };
};
