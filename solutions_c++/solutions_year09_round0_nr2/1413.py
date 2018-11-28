#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define FOR(zzz,a) for(int zzz=0; zzz<(int)(a); zzz++)
#define FORE(zzzz,a) for(int zzzz=1; zzzz<=(int)(a); zzzz++)
#define All(v) (v).begin(), (v).end()
#define zfill(a) memset(&a, 0 , sizeof(a))
#define nfill(a) memset(&a, -1, sizeof(a))
#define S(aaa) scanf("%d",&aaa)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;

int t,sol[105][105],i,j,k,ii,h,w,mi;
int mat[105][105];
char cha[200];
void fill(int x,int y,int no)
{
     if(sol[x-1][y]==4)
     {
       sol[x-1][y]=no;
       fill(x-1,y,no);
     }
     if(sol[x+1][y]==1)
     {
        sol[x+1][y]=no;
        fill(x+1,y,no);
     }
     if(sol[x][y+1]==2)
     {
       sol[x][y+1]=no;
       fill(x,y+1,no);
     }
     if(sol[x][y-1]==3)
     {
       sol[x][y-1]=no;
       fill(x,y-1,no);
     }
     return ;
}
int main()
{

S(t);
FOR(ii,t)
         {
            nfill(mat);
            nfill(sol);
            zfill(cha);
            S(h);S(w);
            FORE(i,h)
               FORE(j,w)
                  S(mat[i][j]);
            int val=5;
            int cnt=0;
            int x[105],y[105];
            zfill(x);zfill(y);            
            FORE(i,h)
               FORE(j,w)
               {
                        mi = mat[i][j];
                        bool flag = false;
                        if(mi>mat[i-1][j] && mat[i-1][j]!=-1)
                        flag=true;
                        if(mi>mat[i][j-1] && mat[i][j-1]!=-1)
                        flag=true;
                        if(mi>mat[i][j+1] && mat[i][j+1]!=-1)
                        flag=true;
                        if(mi>mat[i+1][j] && mat[i+1][j]!=-1)
                        flag=true;
                        if(!flag) 
                        {                       
                           sol[i][j]=val++; 
                           x[cnt]=i;
                           y[cnt]=j;
                           cnt++;                           
                        }                                                                         
               }
 
          FORE(i,h)
             FORE(j,w)
                 {
                      
                      int dir = 0;
                      mi = 1000000;
                      if(sol[i][j]!=-1)continue;
                      if(mi>mat[i-1][j] && mat[i-1][j]!=-1 )     { sol[i][j]=1;  mi = mat[i-1][j]; } // U - N - 1
                      if(mi>mat[i][j-1] && mat[i][j-1]!=-1 )     { sol[i][j]=2;  mi = mat[i][j-1]; } // L - W - 2
                      if(mi>mat[i][j+1] && mat[i][j+1]!=-1 )     { sol[i][j]=3;  mi = mat[i][j+1]; } // R - E - 3
                      if(mi>mat[i+1][j] && mat[i+1][j]!=-1 )     { sol[i][j]=4;  mi = mat[i+1][j]; } // D - S - 4
                      
                 }
                                 
          FOR(k,cnt)
             {
                    fill(x[k],y[k],sol[x[k]][y[k]]);
             }
          printf("Case #%d:\n",ii+1);  
          char ch='a';
          FORE(i,h)
           {                  
                  FORE(j,w)
                  {
                           if(cha[sol[i][j]]==0)
                           cha[sol[i][j]]=ch++;
                           cout<<cha[sol[i][j]]<<" ";
                  }
                  cout<<endl;
           }     
                  
         }
return 0;
}
