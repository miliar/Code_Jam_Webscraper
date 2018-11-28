#include <stdio.h>
#include <iostream>

#define mp make_pair

using namespace std;

const double eps = 1e-3;

typedef pair<double, double> Vec;

int r, c, d;
char str[16][16];
int w[16][16];

void init()
{
    scanf("%d %d %d\n", &r, &c, &d);
    for(int i = 0; i < r; i ++)
        scanf("%s", &str[i]);
    
    for(int i = 0; i < r; i ++)
        for(int j = 0; j < c; j ++)
            w[i][j] = (str[i][j] - '0') + d;
}

bool check(int sz, int x, int y)
{
    Vec cen = mp((double)(2 * x + sz) / 2.0, (double)(2 * y + sz) / 2.0);
    Vec res = mp(0.0, 0.0);
    
    for(int i = x; i < x + sz; i ++)
        for(int j = y; j < y + sz; j ++)
        {
            if(i == x && j == y) continue;
            if(i == x && j == y + sz - 1) continue;
            if(i == x + sz - 1 && j == y) continue;
            if(i == x + sz - 1 && j == y + sz - 1) continue;
            Vec tmp = mp((double)i + 0.5, (double)j + 0.5);
            res.first += (tmp.first - cen.first) * (double)w[i][j];
            res.second += (tmp.second - cen.second) * (double)w[i][j];
        }
    return (res.first >= -eps && res.first <= eps && res.second >= -eps && res.second <= eps);
}

void solve()
{
    /*cout << endl;
    for(int i = 0; i < r; i ++)
    {
        for(int j = 0; j < c; j ++) cout << w[i][j] << " ";
        cout << endl;
    }*/
    
    for(int k = min(r, c); k >= 3; k --)
        for(int i = 0; i + k <= r; i ++)
            for(int j = 0; j + k <= c; j ++)
                if(check(k, i, j))
                {
                    printf("%d\n", k);
                    return;
                }
    printf("IMPOSSIBLE\n");
}

void doit()
{
    init();
    solve();
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i ++)
    {
        printf("Case #%d: ", i);
        doit();
    }
    
    return 0;
}
