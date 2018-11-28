#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
using namespace std;
#define Size 101
#define INF 10000000
int level[Size][Size];
int color[Size][Size];
int H, W;
int curColor;
int r[4] = {-1, 0, 0, 1};
int c[4] = {0, -1, 1, 0};
int k, indexa, mina;
void init()
{
     int i, j;
     for(i=0; i<H; i++)
     for(j=0; j<W; j++)
     color[i][j] = -1;
     curColor = 0;
}
int getColor(int i, int j)
{
    int k;
    if(color[i][j]!=-1)
    return color[i][j];
    
	mina = INF; indexa = 0;
    for(k=0; k<4; k++)
    {
      if(i+r[k]>=0&&i+r[k]<H&&j+c[k]>=0&&j+c[k]<W&&level[i][j]>level[i+r[k]][j+c[k]]&&level[i+r[k]][j+c[k]]<mina)
      {
        mina= level[i+r[k]][j+c[k]];
		indexa = k;
      }
    }
    if(mina<INF)
	{
		color[i][j] = getColor(i+r[indexa], j+c[indexa]);
		return color[i][j];
	}
    color[i][j] = curColor;
    curColor++;
    return color[i][j];
}
int main()
{
    int T, i, j, casenum = 0;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	scanf("%d", &T);
    for(casenum = 1; casenum<=T; casenum++)
    {
     scanf("%d%d", &H, &W);
     for(i=0; i<H; i++)
     for(j=0; j<W; j++)
     scanf("%d", &level[i][j]);
     init();
     
     for(i=0; i<H; i++)
     for(j=0; j<W; j++)
     getColor(i, j);
     
     printf("Case #%d:\n", casenum);
     for(i=0; i<H; i++)
     {
              for(j=0; j<W; j++)
              {
              printf("%c", color[i][j]+'a');
              if(j<W-1) printf(" ");
              }
              printf("\n");
     }
    }
    return 0;
}
