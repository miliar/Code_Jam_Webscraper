#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int array[100][100];
char mask[100][100];

int height, width;

char current;

int connected(int x1, int y1, int x2, int y2, int height,int width){
   if(array[x1][y1] == array[x2][y2])
       return 0;
   int t;
   
   
   if(array[x1][y1] > array[x2][y2])
   {
      t = x1;
      x1 = x2;
      x2 = t;
      t = y1;
      y1 = y2;
      y2 = t; 
   }
   
   int n,w,e,s;
   
   if(y2 > 0)
     n = array[x2][y2-1];
   else
     n = 100000;
   if(x2 > 0)
     w = array[x2-1][y2];
   else 
     w = 100000;
   if(y2 < (height - 1))
     s = array[x2][y2 + 1];
   else 
     s = 100000;
   if (x2 < (width - 1))
     e = array[x2 + 1][y2];
   else
     e = 100000;
   if((n < array[x2][y2]) && (n <= w) && (n <= e) && (n <= s))
     if(y1 == (y2 -1))
      return 1;
     else 
      return 0;
    if ((w < array[x2][y2]) && (w <= e) && (w <= s) && (w <= n))
      if(x1 == (x2 - 1))
      return 1;
      else
      return 0;
    if((e < array[x2][y2]) && (e <= w) && (e <= n) && (e <= s))
     if(x1 == (x2 + 1))
      return 1;
     else 
      return 0;
     if((s < array[x2][y2]) && (s <= w) && (s <= e) && (s <= n))
     if(y1 == (y2 +1))
      return 1;
      else 
      return 0;
   return 0;
}


int dfs(int x,int y,int h,int w){
    mask[x][y] = current;
    if (x > 0)
      if (connected(x-1,y,x,y,h,w) && (mask[x-1][y] < 0))
        dfs(x-1,y,h,w);
    if (y > 0)
      if (connected(x,y-1,x,y,h,w) && (mask[x][y-1] < 0))
        dfs(x,y-1,h,w);
    if (x < (w - 1))
     if (connected(x+1,y,x,y,h,w) && (mask[x+1][y] < 0))
        dfs(x+1,y,h,w);
    if (y < (h - 1))
      if (connected (x,y+1, x, y, h,w) && (mask[x][y+1] < 0))
        dfs(x,y+1,h,w);
    return 1;
}

int solve()
{
    for (int i = 0; i < width; i++)
       for (int j = 0; j < height; j++)
          mask[i][j] = -1;
    current = ('a' - 1);
    int u,v;
    
    u = -1;
    v = 0;
    
    while(1)
    {
        while(1)
        {
           u++;
           if(u >= width)
           {
            u = 0;
            if(v >= (height - 1))
              return 1;
            else
              v++;
            }
            if(mask[u][v] < 0)
              break;
        }    
        current++;
        mask[u][v] = current;
        dfs(u,v,height,width);
    }
    return 1;
}
int main(){
    FILE *fIn = fopen("B.IN","r");
    FILE *fOut = fopen("B.OUT","w");
    int T;
    fscanf(fIn,"%d",&T);
    for(int i = 0; i < T;i++)
    {
        fscanf(fIn,"%d",&height);
        fscanf(fIn,"%d", &width);
        for(int j = 0; j < height; j++)
          for(int k = 0; k < width; k++)
            fscanf(fIn,"%d",&array[k][j]);
        solve();
        fprintf(fOut,"Case #%d:\n",(i+1));
         for(int j = 0; j < height; j++)
         {
          for(int k = 0; k < width; k++)
            fprintf(fOut,"%c ",mask[k][j]);
          fprintf(fOut,"\n");
          }
     }
     fflush(fOut);
     fclose(fIn);
     fclose(fOut);
     return 1;
}
