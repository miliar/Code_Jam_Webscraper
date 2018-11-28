#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int maxn = 105;
bool g[maxn][maxn],h[maxn][maxn];

int calc(int x1,int y1,int x2,int y2){
    int num = 0;
    for (int i=x1; i<=x2; ++i)
        for (int j=y1; j<=y2; ++j)
            if (h[i][j]) num++;
    return num;
}

int main()
{
    freopen("C.in","r",stdin);freopen("C.out","w",stdout);
    int total; scanf("%d",&total);
    for (int casenum=1; casenum<=total; ++casenum){
        int n; scanf("%d",&n);
        memset(h,false,sizeof(h));
        int minx = 1000,maxx = 0;
        int miny = 1000,maxy = 0;
        for (int i=1; i<=n; ++i){
            int x1,y1,x2,y2;
            scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
            if (x1 > x2){
                int tmp = x1; x1 = x2; x2 = tmp;
            }
            if (y1 > y2){
                int tmp = y1; y1 = y2; y2 = tmp;
            }
            if (x1 < minx) minx = x1;
            if (x2 > maxx) maxx = x2;
            if (y1 < miny) miny = y1;
            if (y2 > maxy) maxy = y2;
            for (int j=x1; j<=x2; ++j)
                for (int k=y1; k<=y2; ++k)
                    h[j][k] = true;
        }
        int t = 0;
        while (1){
            int num = calc(minx,miny,maxx,maxy);
            if (num == 0) break; t++;
            for (int i=minx; i<=maxx; ++i)
                for (int j=miny; j<=maxy; ++j)
                    if (h[i][j]){
                        if (!h[i-1][j] && !h[i][j-1])
                            g[i][j] = false;
                        else
                            g[i][j] = true;
                    } else if (h[i-1][j] && h[i][j-1])
                                g[i][j] = true;
                            else g[i][j] = false;
            memcpy(h,g,sizeof(g));
        }
        printf("Case #%d: %d\n",casenum,t);
    }
    return 0;
}
