#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
typedef long long LL;
using namespace std;

#define F_IN  "B-large.in"
#define F_OUT "B-large.out"

//#define F_IN  "B-small-attempt1.in"
//#define F_OUT "B-small-attempt1.out"
#define PI 3.1415926535897932384626433832795
#define INF 1e10
#define EPS 1e-8

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};
#define MAXN 110
struct
{
    int x, y;
} q[MAXN*MAXN];

int down[MAXN][MAXN];
int up[MAXN][MAXN];
double time[MAXN][MAXN];

int tail, head;
int down1, up1;
int down2, up2;
int x, y, h;
int x3, y3;
int x2, y2;
bool nn[MAXN][MAXN];

//priority_queue<int, int> qq; 

int main()
{
    int tc, tt;
    freopen(F_IN, "r", stdin);
    freopen(F_OUT, "w", stdout);
    scanf("%i", &tc);
    for(tt=1; tt<=tc; ++tt)
    {
        scanf("%i %i %i", &h, &y, &x);

        for(int i=1; i<=y; i++)
            for(int j=1; j<=x; ++j)
                scanf("%i", &up[i][j]);

        for(int i=1; i<=y; i++)
            for(int j=1; j<=x; ++j)
                scanf("%i", &down[i][j]);

        for(int i=0; i<=x+1; ++i) 
        {
            down[0][i] = up[0][i] = 0;
            down[y+1][i] = up[y+1][i] = 0;
        }
        for(int i=0; i<=y+1; ++i) 
        {
            down[i][0] = up[i][0] = 0;
            down[i][x+1] = up[i][x+1] = 0;
        }
        q[1].x = 1;
        q[1].y = 1;
        memset(nn, 0, sizeof(nn));
        nn[1][1] = true;
        tail = head = 1;
        while (tail <= head)
        {
            down1 = down[ q[tail].y ][ q[tail].x ];
            up1 = up[ q[tail].y ][ q[tail].x ];
            if (h > down1) down1 = h;
            for(int i=0; i<4; ++i)
            {
                x2 = q[tail].x + dx[i];
                y2 = q[tail].y + dy[i];
                down2 = down[y2][x2];
                up2 = up[y2][x2];

                if (h > down2) down2 = h;

                if (nn[y2][x2]) continue;
                if (up2 - down2 >= 50 && up1 - down2 >= 50 && up2 - down1 >= 50)
                {
                    nn[y2][x2] = true;
                    head++;
                    q[head].x = x2;
                    q[head].y = y2;
                }
            }

            tail++;
        }

        for(int i=1; i<=y; ++i)
            for(int j=1; j<=x; ++j) 
                if (nn[i][j])               
                    time[i][j] = 0.0;
                else
                    time[i][j] = 2*INF;
        
        memset(nn, 0, sizeof(nn));

        while (true)
        {
            double tmin = INF;
            double tmin2;
            x3 = y3 = -1;
            for(int i=1; i<=y; ++i)
                for(int j=1; j<=x; ++j) if (!nn[i][j] && time[i][j] < tmin)
                {
                    tmin = time[i][j];
                    y3 = i;
                    x3 = j;
                }
            if (x3 < 0) break;
            nn[y3][x3] = true;

            for(int i=0; i<4; ++i)
            {
                x2 = x3 + dx[i];
                y2 = y3 + dy[i];
                if (up[y2][x2] - down[y2][x2] < 50) continue;
                if (up[y3][x3] - down[y2][x2] < 50) continue;
                if (up[y2][x2] - down[y3][x3] < 50) continue;
                tmin2 = tmin;
                if (up[y2][x2] - h + tmin2*10.0 < 50.0)
                {
                    tmin2 = (50.0 - up[y2][x2] + h) / 10.0;
                }

                if (up[y3][x3] - h + tmin2*10.0 < 50.0)
                {
                    tmin2 = (50.0 - up[y3][x3] + h) / 10.0;
                }
                
                // by water?
                if (h - tmin2*10.0 - down[y3][x3] + EPS > 20.0)
                {
                    if (time[y2][x2] > tmin2 + 1.0)
                    {
                        time[y2][x2] = tmin2 + 1.0;
                    }
                }
                else
                {
                    if (time[y2][x2] > tmin2 + 10.0)
                    {
                        time[y2][x2] = tmin2 + 10.0;
                    }
                }
            }
        }

        printf("Case #%i: %.6f\n", tt, time[y][x]);
        fprintf(stderr, "%i\n", tt);
    }

    return 0;
}


