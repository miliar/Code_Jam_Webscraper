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

int a[520][520];
int n,m;
int kind = 0;
int num[520] = {0};
int dic[130];

bool can(int x, int y, int s)
{
   for(int i = x; i < x + s; i++)
   {
      int k = 0;
      int sum = 0;
      for(int j = y; j < y + s; j++)
      {
         if(a[i][j] == -1) return(0);
         if(j < y+s-1 && a[i][j] == a[i][j+1]) return(0);
         if(i < x+s-1 && !(a[i][j] ^ a[i+1][j])) return(0);
      }
   }
   return(1);
}

void process(int x, int y, int s)
{
   for(int i = x; i < x+s; i++)
      for(int j = y; j < y+s; j++)
         a[i][j] = -1;
}
         
void solve(int s)
{
   
   for(int i = 1; i <= n-s+1; i++)
   {
      unsigned int k = 0;
      for(int j = 1; j <= m-s+1; j++)
      {
         if(a[i][j] >= 0 && can(i,j,s))
         {
            if(!num[s]) kind ++;
            num[s] ++;
            process(i,j,s);
         }
      }
   }
}
            
int main()
{
freopen("C-large.in","r",stdin);
freopen("E:/out.txt","w",stdout);
   int t,test = 0;
   dic['A'] = 10;dic['B'] = 11;dic['C'] = 12;dic['D'] = 13;dic['E'] = 14;dic['F'] = 15;
   dic['0'] = 0;dic['1'] = 1;dic['2'] = 2;dic['3'] = 3;dic['4'] = 4;
   dic['9'] = 9;dic['8'] = 8;dic['7'] = 7;dic['6'] = 6;dic['5'] = 5;
   scanf("%d",&t);
   while(t--)
   {
      scanf("%d%d",&n,&m);
      for(int i = 1; i <= n; i++)
         for(int j = 1; j <= m; j++)
            a[i][j] = 0;
      for(int i = 1; i <= n; i++)
      {
         char tmp[200];
         scanf("%s",&tmp);
         int k1;
         for(int j = 0; j < m/4; j++)
         {
            k1 = dic[tmp[j]];
            for(int k = 0; k < 4; k++)
            {
               if((1<<k) & k1) a[i][j*4+4-k] = 1;
            }
         }
      }
      memset(num,0,sizeof(num));
      kind = 0;
      for(int i = min(n,m); i >= 1; i--)
      {
          solve(i);
      }
      printf("Case #%d: ",++test);
      printf("%d\n",kind);
      for(int i = min(n,m); i >= 1; i--)
      {
         if(num[i]) printf("%d %d\n",i,num[i]);
      }
   }
   return(0);
}
