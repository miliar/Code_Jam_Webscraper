/*
 * Author: OldY
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
using namespace std;
const int maxint = -1u>>1;
const double pi = acos(-1.0);
const int maxn = 500 + 5;

int T,r,c,d;
int g[maxn][maxn];
struct node{
    int x,y;
} f[maxn][maxn],ff[maxn][maxn];

void updata(int a , int b){
    f[a][b].x = f[a-1][b].x + f[a][b-1].x - f[a-1][b-1].x + b*g[a][b];
    f[a][b].y = f[a-1][b].y + f[a][b-1].y - f[a-1][b-1].y + a*g[a][b];
}
char tmp;
int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin >> T;
    for(int t = 1 ; t <= T ; t++){
        for(int i = 0 ; i < maxn ; i++){
            for(int j = 0 ; j < maxn ; j++){
                f[i][j].x = f[i][j].y = 0;
                ff[i][j].x = ff[i][j].y = 0;
            }
        }
        cin >> r >> c >> d;
        //cout << r <<" " << c << " " << d << endl;
        for(int i = 1 ; i <= r ; i++)
            for(int j = 1 ; j <= c ; j++){
                cin >> tmp;
                g[i][j] = tmp - '0';
            }
        //for(int i = 1 ; i <= r ; i++){
            //for(int j = 1 ; j <= c ; j++) cout << g[i][j] << " ";
            //cout << endl;
        //}
        f[1][1].x = f[1][1].y = g[1][1];
        ff[1][1].x = ff[1][1].y = g[1][1];
        for(int i = 2 ; i <= c ; i++){
            f[1][i].x = f[1][i-1].x + i*g[1][i];
            ff[1][i].x = ff[1][i-1].x + g[1][i];
            f[1][i].y = f[1][i-1].y + g[1][i];
            ff[1][i].y = ff[1][i-1].y + g[1][i];
        }
        for(int i = 2 ; i <= r ; i++){
            f[i][1].x = f[i-1][1].x + g[i][1];
            ff[i][1].x = ff[i-1][1].x + g[i][1];
            f[i][1].y = f[i-1][1].y + i*g[i][1];
            ff[i][1].y = ff[i-1][1].y + g[i][1];
        }
        for(int i = 2 ; i <= r ; i++)
            for(int j = 2 ; j <= c ; j++){
                updata(i,j);
                ff[i][j].x = ff[i-1][j].x + ff[i][j-1].x - ff[i-1][j-1].x + g[i][j];
                ff[i][j].y = ff[i-1][j].y + ff[i][j-1].y - ff[i-1][j-1].y + g[i][j];
            }
        //for(int i = 1 ; i <= r ; i++){
            //for(int j = 1 ; j <= c ; j++) cout << f[i][j].x << " ";
            //cout << endl;
        //}
        //cout << f[r][c].x << endl;
         //for(int i = 1 ; i <= r ; i++){
            //for(int j = 1 ; j <= c ; j++) cout << f[i][j].y << " ";
            //cout << endl;
        //}
        int ans = 0;
        for(int i = 1 ; i <= r ; i++){
            for(int j = 1 ; j <= c ; j++){
                for(int k = 3; i+k-1<=r && j+k-1<=c ; k++){
                    int x = i+k-1 , y = j+k-1;
                    int tmpx = f[x][y].x-f[x][j-1].x-f[i-1][y].x+f[i-1][j-1].x;
                    tmpx -= j*(g[i][j]+g[x][j])+y*(g[i][y]+g[x][y]);
                    int cntx = ff[x][y].x-ff[x][j-1].x-ff[i-1][y].x+ff[i-1][j-1].x;
                    cntx -= (g[i][j]+g[x][j])+(g[i][y]+g[x][y]);
                    //cout << "i = " << i << " j = " << j << endl;
                    //cout << "x = " << x << " y = " << y << endl;
                    //cout << "tmpx = " << tmpx << " cntx = " << cntx << endl;
                    //int tmpy = f[x][y].y-f[x][j-1].y-f[i-1][y].y+f[i-1][j-1].y;
                    //tmpy -= i*(g[i][j]+g[i][y])+x*(g[x][j]+g[x][y]);
                    //int cnty = ff[x][y].y-ff[x][j-1].y-ff[i-1][y].y+ff[i-1][j-1].y;
                    //cnty -= (g[i][j]+g[x][j])+(g[i][y]+g[x][y]);
                    //cout << "tmpy = " << tmpy << " cnty = " << cnty << endl;
                    if(2*tmpx == (y+j)*cntx){
                        int tmpy = f[x][y].y-f[x][j-1].y-f[i-1][y].y+f[i-1][j-1].y;
                        tmpy -= i*(g[i][j]+g[i][y])+x*(g[x][j]+g[x][y]);
                        int cnty = ff[x][y].y-ff[x][j-1].y-ff[i-1][y].y+ff[i-1][j-1].y;
                        cnty -= (g[i][j]+g[i][y])+(g[x][j]+g[x][y]);
                        if(2*tmpy == (x+i)*cnty) ans = max(ans,k);
                    }
                }
            }
        }
        cout << "Case #" << t << ": ";
        if(ans >= 3) cout << ans << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}

