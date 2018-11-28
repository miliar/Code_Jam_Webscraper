#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <queue>
#include <stack>
using namespace std;
    int cross(int x1 , int y1 , int x2 , int y2 , int x3 , int y3){
        int a,b;
        int a2,b2;
        a=x2-x1;
        b=y2-y1;
        a2=x3-x1;
        b2=y3-y1;
        int cross = (a * b2) - (a2 * b);
        return abs(cross);
    }

int main()
{
  int N;
  scanf("%d",&N);
   for(int kk=0;kk<N;kk++)
   {
   int n,m,a,flag=0;  
      scanf("%d%d%d",&n,&m,&a);
    // for(int x=0;x<=n;x++)
     //for(int y=0;y<=m;y++)
      for(int r=0;r<=n&&!flag;r++)       
         for(int c=0;c<=m&&!flag;c++)
           for(int j=0;j<=n&&!flag;j++)
             for(int k=0;k<=m && !flag;k++)
              {              
                if( cross( 0,0,r,c,j,k )==a )
                 {
                    printf("Case #%d: %d %d %d %d %d %d\n",kk+1,0,0,r,c,j,k);
                    flag=1;
                 }
              }       
              if(!flag)
               printf("Case #%d: IMPOSSIBLE\n",kk+1);
   }     
return 0;
 }
 