#include <iostream>
#include <cstdlib>
#include <string>
#include <climits>
#include <cstring>

using namespace std;

int varix[4]={1,0,0,-1};
int variy[4]={0,1,-1,0};
int map[1001][1001];
int shed[1001][1001];
int x,y,m;

int dp(int i,int j)
{
    if(shed[i][j]!=-1)return shed[i][j];
    int least = map[i][j];
    int a,b,leastx,leasty;
    for(int k=0;k<4;k++){
      a = i+varix[k];
      b = j+variy[k];
      if(a<0||a>x-1||b<0||b>y-1)continue;
      if(map[a][b]<=least){
        if(map[a][b]==map[i][j])continue;
        least = map[a][b];
        leastx = a;
        leasty = b;
      }
    }
    if(least == map[i][j])shed[i][j]=m++;
    else shed[i][j] = dp(leastx,leasty);
    return shed[i][j];
}

int func()
{
    for(int i=0;i<x;i++)
    for(int j=0;j<y;j++)
    if(shed[i][j]==-1)dp(i,j);
}

int main()
{
    int t,f=1;
    scanf("%d",&t);
    while (t--) {
      scanf("%d %d",&x,&y);
      for (int i = 0; i < x; i++)
      for (int j = 0; j < y; j++)
      scanf("%d",&map[i][j]);
      memset(shed,-1,sizeof(shed));
      m=0;
      func();
      printf("Case #%d:\n",f++);
      for(int i=0;i<x;i++){
      for(int j=0;j<y;j++){
        printf("%c ",shed[i][j]+'a');
      }
      printf("\n");
      }
    }
    return 0;
}
