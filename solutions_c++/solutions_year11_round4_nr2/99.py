#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cmath>
using namespace std;
void tst()
{
    int r,c,d;
    scanf("%d%d%d\n",&r,&c,&d);
    int inp[c][r];
    for(int i=0;i<r;i++)
    {
        char in[c+1];
        gets(in);
        for(int j=0;j<c;j++)
            inp[j][i] = in[j]-'0';
    }
    int s1[c+1][r+1];
    for(int i=0;i<=c;i++)
        for(int j=0;j<=r;j++)
            if(i && j)
                s1[i][j] = inp[i-1][j-1];
            else
                s1[i][j]=0;
    for(int i=0;i<c;i++)
        for(int j=0;j<=r;j++)
            s1[i+1][j] += s1[i][j];
    for(int i=0;i<=c;i++)
        for(int j=0;j<r;j++)
            s1[i][j+1] += s1[i][j];
    int sx[c+1][r+1];
    for(int i=0;i<=c;i++)
        for(int j=0;j<=r;j++)
            if(i && j)
                sx[i][j] = (i-1)*inp[i-1][j-1];
            else
                sx[i][j]=0;
    for(int i=0;i<c;i++)
        for(int j=0;j<=r;j++)
            sx[i+1][j] += sx[i][j];
    for(int i=0;i<=c;i++)
        for(int j=0;j<r;j++)
            sx[i][j+1] += sx[i][j];
    int sy[c+1][r+1];
    for(int i=0;i<=c;i++)
        for(int j=0;j<=r;j++)
            if(i && j)
                sy[i][j] = (j-1)*inp[i-1][j-1];
            else
                sy[i][j]=0;
    for(int i=0;i<c;i++)
        for(int j=0;j<=r;j++)
            sy[i+1][j] += sy[i][j];
    for(int i=0;i<=c;i++)
        for(int j=0;j<r;j++)
            sy[i][j+1] += sy[i][j];
    int ANSANS = 0;
    for(int l = 3;l<=c && l<=r;l++)
    {
        for(int x=0;x+l<=c;x++)
            for(int y=0;y+l<=r;y++)
            {
                int w = s1[x+l][y+l] + s1[x][y] - s1[x+l][y] - s1[x][y+l];
                w -= inp[x][y] + inp[x][y+l-1] + inp[x+l-1][y] + inp[x+l-1][y+l-1];
                int mx = sx[x+l][y+l] + sx[x][y] - sx[x+l][y] - sx[x][y+l];
                mx -= x*inp[x][y] + x*inp[x][y+l-1] + (x+l-1)*inp[x+l-1][y] + (x+l-1)*inp[x+l-1][y+l-1];
                int my = sy[x+l][y+l] + sy[x][y] - sy[x+l][y] - sy[x][y+l];
                my -= y*inp[x][y] + (y+l-1)*inp[x][y+l-1] + y*inp[x+l-1][y] + (y+l-1)*inp[x+l-1][y+l-1];
                if(fabs(w*(x+(l-1)/2.0) - mx) < 0.0001)
                    if(fabs(w*(y+(l-1)/2.0) - my) < 0.0001)
                        ANSANS = l;
            }
    }
    if(ANSANS>0)
        printf("%d\n",ANSANS);
    else
        printf("IMPOSSIBLE\n");
}
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        tst();
    }

}
