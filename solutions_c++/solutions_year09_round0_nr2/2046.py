#include <string>
using namespace std;
int N, H, W;
int grid[100][100];
char ans[100][100];
bool seen[100][100];
int di[] = {-1, 0, 0, 1};
int dj[] = {0, -1, 1, 0};
char c;
char dfs(int i, int j)
{
    if(ans[i][j]!='A')return ans[i][j];
    int ni =- 1, nj = -1;
int min =10000;
    for(int k =0;k<4;k++)
    {
	if(i+di[k] >= 0 && i+di[k] < H && j +dj[k]>=0 && j+dj[k]<W && grid[i+di[k]][j+dj[k]]< grid[i][j] && grid[i+di[k]][j+dj[k]]< min)
	{
	  min = grid[i+di[k]][j+dj[k]];
           ni =i + di[k];
           nj =j+ dj[k];
	}
    }
    if(ni == -1)
    {
      if(ans[i][j]=='A'){return ans[i][j] = c++;}
       return ans[i][j];
    }
   return ans[i][j] = dfs(ni, nj);
}
int main()
{
    scanf("%d", &N);
int cas= 1;
    while(N--)
    {
         c = 'a';
        scanf("%d%d", &H, &W);
        for(int i=0;i<H;i++)
           for(int j =0;j<W;j++){
              scanf("%d", &grid[i][j]);
            ans[i][j] ='A';
	    }
        for(int i=0;i<H;i++)
           for(int j=0;j<W;j++)
           { 
                  if(ans[i][j] =='A')
                  dfs(i, j);
           }

          printf("Case #%d:\n", cas++);
            for(int i=0;i<H;i++)
               for(int j=0;j<W;j++){
                    if(j!=W-1)
                 printf("%c ",ans[i][j]);
		      else
                  printf("%c\n",ans[i][j]);
               }

    }
}
