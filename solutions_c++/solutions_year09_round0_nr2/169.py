#include<iostream>
using namespace std;
const int MAXN = 1200;
const int inf = 1000000000;
bool visited[MAXN][MAXN];
char str[MAXN][MAXN];
const int d[][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int n,m;
int a[MAXN][MAXN];
char cur;
struct node
{
       int x,y;
}queue[MAXN * MAXN];
int head,tail;
int ansx,ansy;
bool bfs(const int x,const int y)
{
     node pre,next;
     int i,minn;
     int xx,yy;
     head = tail = 0;
     pre.x = x;
     pre.y = y;
     visited[x][y] = true;
     queue[tail++] = pre;
     while(tail > head)
     {
           pre = queue[head++];
           minn = inf;
           for(i = 0;i < 4;i++)
           {
               next.x = pre.x + d[i][0];
               if(next.x < 0 || next.x >= n) continue;
               next.y = pre.y + d[i][1];
               if(next.y < 0 || next.y >= m) continue;
               if(a[next.x][next.y] >= a[pre.x][pre.y]) continue;
               if(a[next.x][next.y] < minn)
               {
                 minn = a[next.x][next.y];
                 xx = next.x;
                 yy = next.y;
               }
           }
           if(minn == inf) return false;
           if(visited[xx][yy])
           {
              ansx = xx; ansy = yy;
              return true;
           }
          visited[xx][yy] = true; 
          next.x = xx; next.y = yy;
          queue[tail++] = next;
     }
   return false;
}                         
     
int main()
{
    int ncase,casenum = 1;
    int i,J,k;
    freopen("B.txt","w",stdout);
    scanf("%d",&ncase);
    while(ncase--)
    {
          scanf("%d%d",&n,&m);
          for(i = 0;i < n;i++)
           for(J = 0;J < m;J++)
           scanf("%d",&a[i][J]);
          memset(visited,false,sizeof(visited));
          cur = 'a';
          for(i = 0;i < n;i++)
           for(J = 0;J < m;J++)
           if(visited[i][J]==false)
           {
               if(bfs(i,J))
               {
                  
                  for(k = 0;k < tail;k++)
                  str[queue[k].x][queue[k].y] = str[ansx][ansy];
                              
               }
               else
               {
                  for(k = 0;k < tail;k++)
                  str[queue[k].x][queue[k].y] = cur;
                 cur++;     
               }
               /* 
               for(k = 0;k < tail;k++)
                printf("%d %d    ",queue[k].x,queue[k].y);
               putchar('\n'); */
           }
         printf("Case #%d:\n",casenum++);  
         for(i = 0;i < n;i++)
         {
             for(J = 0;J < m - 1;J++)
             {
                 putchar(str[i][J]);
                putchar(' ');
             }
            putchar(str[i][J]);
           putchar('\n');
         }                         
    }     
    return 0;
}
