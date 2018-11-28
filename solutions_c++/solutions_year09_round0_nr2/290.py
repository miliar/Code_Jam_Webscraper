#include <cstdio>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <cmath>
#include <map>
#include <vector>
#include <queue>

using namespace std;

#define FOR(i, x) for (int i = 0; i < x; i++)
#define FORI(i,a, x) for (int i = a; i < x; i++)
#define ALL(x) (x).begin(), (x).end()
#define FORE(i, x) for (__typeof__((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())
#define INF 0x3F3F3F3F

#define MAX 100

int altitudes[MAX+1][MAX+1];
int names[MAX+1][MAX+1];
int flow[MAX+1][MAX+1];
char current;

//   1
//  203
//   4

void flood(int r, int c, char x)
{
   int dir = flow[r][c];
   names[r][c] = x;
   if(((dir&1)>0) && (names[r-1][c]==-1)) flood(r-1,c,x);
   if(((dir&2)>0) && (names[r][c-1]==-1)) flood(r,c-1,x);
   if(((dir&4)>0) && (names[r][c+1]==-1)) flood(r,c+1,x);
   if(((dir&8)>0) && (names[r+1][c]==-1)) flood(r+1,c,x);
}

int main()
{
   freopen("in/B-large.in","r",stdin);
   freopen("out/B-large.out","w",stdout);

   int H, W, T;
   
   scanf("%d",&T);
   
   FOR(t,T)
   {
      // Read Input
      scanf("%d%d",&H,&W);
      FOR(i,H)
      {
         FOR(j,W)
         {
            scanf("%d",&altitudes[i][j]);
            names[i][j] = -1;
            flow[i][j] = 0;
         }
      }

      //Calculate flows per cell
      int dir1, dir2, x, y, min;
      FOR(i,H)
      {
         FOR(j,W)
         {
            dir1 = 0, dir2=0, x=0, y=0, min = altitudes[i][j];
            if((i>0) && (min>altitudes[i-1][j])) dir1 = 1, dir2=8, x=-1, y=0, min = altitudes[i-1][j];
            if((j>0) && (min>altitudes[i][j-1])) dir1 = 2, dir2=4, x=0, y=-1, min = altitudes[i][j-1];
            if((j<W-1) && (min>altitudes[i][j+1])) dir1 = 4, dir2=2, x=0, y=1, min = altitudes[i][j+1];
            if((i<H-1) && (min>altitudes[i+1][j])) dir1 = 8, dir2=1, x=1, y=0, min = altitudes[i+1][j];
            flow[i][j] |= dir1, flow[i+x][j+y] |= dir2;
         }
      }

      //Label
      current = 'a';
      FOR(i,H)
      {
         FOR(j,W)
         {
            if(names[i][j]==-1)
            {
               flood(i,j,current);
               current++;
            }
         }
      }
      
      printf("Case #%d:\n",t+1);
      FOR(i,H)
      {
         printf("%c",names[i][0]);
         FORI(j,1,W)
         {
            printf(" %c",names[i][j]);
         }
         printf("\n");
      }      
   }


   
   return 0;
}
