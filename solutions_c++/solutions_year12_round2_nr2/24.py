#include <stdio.h>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <memory.h>
#include <queue>
#include <string>
#include <string.h>
#include <cmath>
#include <utility>
#include <bitset>
#include <time.h>
#include <climits>

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))
#define OUT_RT cerr << (float(clock()) / CLOCKS_PER_SEC) << endl

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;



struct Tp{
    int x, y;
    double d;

    Tp(int x = 0, int y =0, double d =0):x(x),y(y),d(d){}
};
int dx[] = {0, 1, 0, -1}, dy[] = {1, 0, -1, 0};

#define eps 1e-10
int c[111][111], f[111][111], n, m;
double h, d[111][111];

int main(void){
    freopen("in","r",stdin);
    freopen("out","w",stdout);

    int T;
    scanf("%d\n",&T);
    for(int _=1;_<=T;_++){
        cin >> h >> n >> m;

        for (int i = 1; i <= n; i++) 
            for (int j = 1; j <= m; j++)
                cin >> c[i][j];
        for (int i = 1; i <= n; i++) 
            for (int j = 1; j <= m; j++)
                cin >> f[i][j];

        for (int i = 1; i <= n; i++) 
            for (int j = 1; j <= m; j++)
                d[i][j] = 1e100;                         

        queue< Tp > q;
        d[1][1] = 0.;

        q.push(Tp(1, 1, 0));
        while (!q.empty()) {
            Tp t = q.front(); q.pop();
            int x = t.x, y = t.y;
            double D = t.d;
            if (d[x][y] < D) continue;
            for (int i = 0; i < 4; i++) {
                int xx = x + dx[i];
                int yy = y + dy[i];
                if (xx < 1 || yy < 1 || xx > n || yy > m) continue;
                if (f[xx][yy] + 50 > c[x][y]) continue;
                if (f[x][y]   + 50 > c[xx][yy]) continue;
                if (f[xx][yy] + 50 > c[xx][yy]) continue;
                if (h + 50. < c[xx][yy] + eps && d[xx][yy] > D + 1 + eps) {
                    d[xx][yy] = D + 1;
                    q.push(Tp(xx, yy, d[xx][yy]));
                }
            }
        }

        for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            if (d[i][j] < 1e90) {
                d[i][j] = 0 ;
                q.push(Tp(i, j, 0));
            }
        while (!q.empty()) {
            Tp t = q.front(); q.pop();
            int x = t.x, y = t.y;
            double D = t.d;
            if (d[x][y] < D) continue;

            for (int i = 0; i < 4; i++) {
                int xx = x + dx[i];
                int yy = y + dy[i];
                if (xx < 1 || yy < 1 || xx > n || yy > m) continue;
                if (f[xx][yy] + 50 > c[x][y]) continue;
                if (f[x][y]   + 50 > c[xx][yy]) continue;
                if (f[xx][yy] + 50 > c[xx][yy]) continue;

                if (h - D * 10. + 50. < c[xx][yy] + eps) {
                    if (h - D * 10 - 20 + eps > f[x][y]) {
                        if (d[xx][yy] > D + 1 + eps) {
                            d[xx][yy] = D + 1;
                            q.push(Tp(xx, yy, d[xx][yy]));
                        }
                    } else {
                        if (d[xx][yy] > D + 10 + eps) {
                            d[xx][yy] = D + 10;
                            q.push(Tp(xx, yy, d[xx][yy]));
                        }
                    }
                } else {
                    double dd = (h - (c[xx][yy] - 50.)) / 10.;
                    if (h - dd * 10 - 20 + eps > f[x][y]) {
                        if (d[xx][yy] > dd + 1 + eps) {
                            d[xx][yy] = dd + 1;
                            q.push(Tp(xx, yy, d[xx][yy]));
                        }
                    } else {
                        if (d[xx][yy] > dd + 10 + eps) {
                            d[xx][yy] = dd + 10;
                            q.push(Tp(xx, yy, d[xx][yy]));
                        }
                    }
                }
            }
        }
        
        printf("Case #%d: %.10lf\n",_, d[n][m]);
    }

    return 0;;    
}
