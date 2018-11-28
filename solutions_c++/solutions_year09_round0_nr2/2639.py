#include <iostream>
using namespace std;
#define MAX 102
#define inf 999999
int ter[MAX][MAX];
int esc[MAX][MAX];
int fim[MAX][MAX];
int mini(int x, int y) {
   int c,d,e,t,b,menor;
   c=ter[x][y];
   t=ter[x-1][y];
   b=ter[x+1][y];
   e=ter[x][y-1];
   d=ter[x][y+1];
   menor=min(min(min(t,b),min(e,d)),c);
   if (menor==c)
      return 1;
   else if (menor==t)
      return 2;
   else if (menor==e)
      return 3;
   else if (menor==d)
      return 4;
   else
      return 5;
}

void mont2(int x, int y, int l) {
   fim[x][y]=l;
   if (esc[x-1][y]==5)
      mont2(x-1,y,l);
   if (esc[x+1][y]==2)
      mont2(x+1,y,l);
   if (esc[x][y+1]==3)
      mont2(x,y+1,l);
   if (esc[x][y-1]==4)
      mont2(x,y-1,l);
   return;
}

void mont(int x, int y, int l) {
   if (esc[x][y]==1) {
      mont2(x,y,l);
      return;
   } else {
      if (esc[x][y]==2)
         mont(x-1,y,l);
      if (esc[x][y]==3)
         mont(x,y-1,l);
      if (esc[x][y]==4)
         mont(x,y+1,l);
      if (esc[x][y]==5)
         mont(x+1,y,l);     
   }
}
int main(void) {
   int t,h,w;
   int i, j, k;
   int letra;
   cin >> t;
   for(k=0;k<t;k++) {
      letra=1;
      cin >> h >> w;
      for(i=0;i<=h+1;i++) {
         ter[0][i]=inf;
         ter[w+1][i]=inf;
      }
      for(i=0;i<=w+1;i++) {
         ter[i][0]=inf;
         ter[i][h+1]=inf;
      }
      for(i=1;i<=h;i++)
         for(j=1;j<=w;j++)
            fim[i][j]=esc[i][j]=0;
            cin >> ter[i][j];
      
      for(i=1;i<=h;i++)
         for(j=1;j<=w;j++)
            esc[i][j]=mini(i,j);
         
      for(i=1;i<=h;i++) {
         for(j=1;j<=w;j++) {
            if (fim[i][j]==0) {
               mont(i,j,letra);
               letra++;
            }
         }
      }
      cout << "Case #" << k+1 << ":" << endl;
      for(i=1;i<=h;i++) {
         for(j=1;j<=w;j++) {
            cout << fim[i][j];
         }
         cout << endl;
      }
      cout << endl;
   }
}
