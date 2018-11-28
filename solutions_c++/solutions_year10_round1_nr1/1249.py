#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <list>

using namespace std;

int main()
{


freopen("A-small-attempt4.in","r",stdin);
freopen("E:/out.txt","w",stdout);
   int t,test = 0;
   scanf("%d",&t);
   while(t--)
   {
      int n,k1;
      char a[55][55];
      scanf("%d%d",&n,&k1);
      for(int i = 0; i < n; i++) scanf("%s",&a[i]);
      char r[55][55];
      char g[55][55];
      for(int i = 0; i < n; i++)
         for(int j = 0; j < n; j++)
         {
            g[i][j] = '.';
            r[i][j] = '.';
         }
      for(int i = 0; i < n; i++)
      {
         int j = n-1, k;
         while(1){
         while(a[i][j] != '.' && j >= 0) 
         {
            r[i][j] = a[i][j];
            j--;
         }
         if(j <= 0) break;
         else
         {
            k = j;
            while(a[i][k] == '.' && k >= 0) k--;
            if(k < 0) break;
            else
            {
               r[i][j] = a[i][k];
               a[i][k] = '.';
               j--;
               if(j < 0) break;
            }
         }
         }
      }
      /*
      for(int i = 0; i < n; i++)
      {
              for(int j = 0; j < n; j++) cout<<r[i][j];
              cout<<endl;}
              cout<<endl;
              */
      for(int i = 0; i < n; i++)
         for(int j = n-1; j >= 0; j--)
            { g[i][n-1-j] = r[j][i]; 
            }
      bool flag1 = 0, flag2 = 0;
      for(int i = 0; i < n; i++)
      {
          
          int j = 0;
          while(j < n){
                  int num1 = 0, num2 = 0;
          if(g[i][j] == 'R')
          {
             int tmp = 0;
             while(g[i][j] == 'R' && j < n)
             {
                j++;
                tmp++;
             }
             if(tmp > num1) num1 = tmp;
          }
          if(g[i][j] == 'B')
          {
             int tmp = 0;
             while(g[i][j] == 'B' && j < n)
             {
                j++;
                tmp++;
             }
             if(tmp > num2) num2 = tmp;
          }
          if(g[i][j] == '.') j++;
          
          if(num1 >= k1) flag1 = 1;
          if(num2 >= k1) flag2 = 1;  }        
      }
      for(int i = 0; i < n; i++)
      {
          int j = 0;
          while(j < n){
                  int num1 = 0, num2 = 0;
          if(g[j][i] == 'R')
          {
             int tmp = 0;
             while(g[j][i] == 'R' && j < n)
             {
                j++;
                tmp++;
             }
             if(tmp > num1) num1 = tmp;
          }
          if(g[j][i] == 'B')
          {
             int tmp = 0;
             while(g[j][i] == 'B' && j < n)
             {
                j++;
                tmp++;
             }
             if(tmp > num2) num2 = tmp;
          }
          if(g[j][i] == '.') j++;
          
          if(num1 >= k1) flag1 = 1;
          if(num2 >= k1) flag2 = 1; }     
      }
      for(int i = 0; i < n; i++)
      {
          int x = 0, y = i;
          while(x < n && y >= 0){
                  int num1 = 0, num2 = 0;
          if(g[x][y] == 'R')
          {
             int tmp = 0;
             while(g[x][y] == 'R' && x < n && y >= 0)
             {
                x++; y--;
                tmp++;
             }
             if(tmp > num1) num1 = tmp;
          }
          if(g[x][y] == 'B')
          {
             int tmp = 0;
             while(g[x][y] == 'B' && x < n && y >= 0)
             {
                x++; y--;
                tmp++;
             }
             if(tmp > num2) num2 = tmp;
          }
          if(g[x][y] == '.') {x++; y--; }
         
          if(num1 >= k1) flag1 = 1;
          if(num2 >= k1) flag2 = 1;  }
      }
      for(int i = 0; i < n; i++)
      {
          int x = i, y = n-1;
          while(x < n && y >= 0){
                  int num1 = 0, num2 = 0;
          if(g[x][y] == 'R')
          {
             int tmp = 0;
             while(g[x][y] == 'R' && x < n && y >= 0)
             {
                x++; y--;
                tmp++;
             }
             if(tmp > num1) num1 = tmp;
          }
          if(g[x][y] == 'B')
          {
             int tmp = 0;
             while(g[x][y] == 'B' && x < n && y >= 0)
             {
                x++; y--;
                tmp++;
             }
             if(tmp > num2) num2 = tmp;
          }
          if(g[x][y] == '.') {x++; y--; }
          if(num1 >= k1) flag1 = 1;
          if(num2 >= k1) flag2 = 1; }
      }
      for(int i = 0; i < n; i++)
      {

          int x = 0, y = i;
          while(x < n && y < n){
                  int num1 = 0, num2 = 0;
          if(g[x][y] == 'R')
          {
             int tmp = 0;
             while(g[x][y] == 'R' && x < n && y < n)
             {
                x++; y++;
                tmp++;
             }
             if(tmp > num1) num1 = tmp;
          }
          if(g[x][y] == 'B')
          {
             int tmp = 0;
             while(g[x][y] == 'B' && x < n && y < n)
             {
                x++; y++;
                tmp++;
             }
             if(tmp > num2) num2 = tmp;
          }
          if(g[x][y] == '.') x++; y++;         
          if(num1 >= k1) flag1 = 1;
          if(num2 >= k1) flag2 = 1;   }       
      }
      for(int i = 0; i < n; i++)
      {
          int num1 = 0, num2 = 0;
          int x = i, y = 0;
          while(x < n && y < n){
                  int num1 = 0, num2 = 0;
          if(g[x][y] == 'R')
          {
             int tmp = 0;
             while(g[x][y] == 'R' && x < n && y < n)
             {
                x++; y++;
                tmp++;
             }
             if(tmp > num1) num1 = tmp;
          }
          if(g[x][y] == 'B')
          {
             int tmp = 0;
             while(g[x][y] == 'B' && x < n && y < n)
             {
                x++; y++;
                tmp++;
             }
             if(tmp > num2) num2 = tmp;
          }
          if(g[x][y] == '.') x++; y++;
          if(num1 >= k1) flag1 = 1;
          if(num2 >= k1) flag2 = 1;  }        
      }
      printf("Case #%d: ",++test);
      if(flag1 && flag2) printf("Both\n");
      else if(flag1) printf("Red\n");
      else if(flag2) printf("Blue\n");
      else printf("Neither\n"); 
   }
   return(0);
}

            
      
