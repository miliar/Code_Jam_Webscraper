#include<iostream>
#include<cstring>

using namespace std;

bool ada[101][101];
int i,j,k,l,kasus,jawab,total,minx,miny,maxx,maxy,banyak,x1,x2,y1,y2;

int main()
{
     scanf("%d",&kasus);
     for (l=1;l<=kasus;l++)
     {
          memset(ada,0,sizeof(ada));
          total = 0;

          scanf("%d",&banyak);
          minx = miny = 101;
          maxx = maxy = 0;
          for (k=1;k<=banyak;k++)
          {
               scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
               minx = min(minx,x1);
               miny = min(miny,y1);
               maxx = max(maxx,x2);
               maxy = max(maxy,y2);

               for (i=y1;i<=y2;i++)
               {
                    for (j=x1;j<=x2;j++)
                    {
                         if (!ada[i][j])
                         {
                              ada[i][j] = true;
                              total++;
                         }
                    }
               }
          }

          jawab = 0;
          while (total)
          {
               jawab++;
               for (i=maxy;i>=miny;i--)
               {
                    for (j=maxx;j>=minx;j--)
                    {
                         if ((ada[i][j])&&(!ada[i-1][j])&&(!ada[i][j-1]))
                         {
                              ada[i][j] = false;
                              --total;
                         }
                         else if ((!ada[i][j])&&(ada[i-1][j])&&(ada[i][j-1]))
                         {
                              ada[i][j] = true;
                              ++total;
                         }
                    }
               }
          }

          printf("Case #%d: %d\n",l,jawab);
     }
     return 0;
}
