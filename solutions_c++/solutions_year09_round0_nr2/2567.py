#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
    
int H,W;

int map[105][105];
int flag[105][105];
char res[105][105];
struct 
{
       int x,y;       
}dir[4]={ {-1,0}, {0,-1}, {0,1}, {1,0} };
int modify;
char c;
void solve(int x,int y)
{
      if(flag[x][y]==1) 
      {
              modify = 1;          
              c = res[x][y];          
              return;                  
      }
      int t = map[x][y];
      int sx,sy;
      int tx = -1;
      int ty = -1;
      for(int k=0;k<4;k++)
      {
              sx = x + dir[k].x;
              sy = y + dir[k].y;
              if( sx>=0 && sx<H && sy>=0 &&sy<W && map[sx][sy]<t )
              {
                      tx = sx;
                      ty = sy;
                      t = map[sx][sy];
              }
      }
      if( tx!=-1 && ty!=-1 )
      {
              solve(tx,ty); 
      } 
      flag[x][y] = 1;
      res[x][y] = c;  
      return ;
}

int main(int argc, char *argv[])
{
    freopen("B-large.in","r",stdin);
  //  freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
      
    int N;
    scanf("%d",&N);
    
    int CASE = 1;
    while(N--)
    {
          scanf("%d%d",&H,&W);    
          memset(map,-1,sizeof(map)); 
          memset(flag,-1,sizeof(flag));   
          memset(res,-1,sizeof(res));
          for(int i=0;i<H;i++)
                  for(int j=0;j<W;j++)
                          scanf("%d",&map[i][j]);

          
          char num = 'a';      
 //         res[0][0] = 1;
 //         flag[0][0] = 1;        
          for(int i=0;i<H;i++)
                  for(int j=0;j<W;j++)
                  {
                             c = num;
                             modify = 0; 
                             solve(i,j); 
                             if(modify==0) num++;        
                  }                
          printf("Case #%d:\n",CASE);
          for(int i=0;i<H;i++)
          {
                  for(int j=0;j<W;j++)
                  {
                          printf("%c ",res[i][j]);        
                  }
                  printf("\n");
          }    
          CASE++;     
    }

    return 0;
}
