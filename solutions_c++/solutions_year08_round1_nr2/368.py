#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;
set < pair < int , int > > mapi[1000];
int bin[1000],res[1000],best,n,m;
bool cumple(  )
 {
   for(int r=0;r<m;r++)
    {
    int th=0;
       for(int c=0;c<n;c++)
        {
          if(mapi[r].count( make_pair( c,bin[c] ) ))
            th=1;
        }
      if(!th)
      return false;
    }
    return true;
 }
void rec(int p,int cant)
{
   if(p==n)
    {     
      if(cumple())
        {
           if(cant<best)
            {
              best=cant;
              for(int r=0;r<n;r++)
                res[r]=bin[r];
            }
        }
    }
    else
    {
       rec(p+1,cant);
       bin[p]=1;
       rec(p+1,cant+1);
       bin[p]=0;
    }
}
int main()
{
int h=0;
scanf("%d",&h);
for(int kk=0;kk<h;kk++)
{
 best=1<<30;
 memset(bin,0,sizeof(bin));
 memset(res,0,sizeof(res));
scanf("%d%d",&n,&m);
  for(int r=0;r<m;r++)
  {
    mapi[r].clear();
    int t,a,b;
    scanf("%d",&t);
    for(int c=0;c<t;c++)
    scanf("%d%d",&a,&b),mapi[r].insert(make_pair(a-1,b));
  }  
  rec(0,0);
    if(best==1<<30)
      printf("Case #%d: IMPOSSIBLE\n",kk+1);
      else
      {
        printf("Case #%d: ",kk+1);
        for(int r=0;r<n;r++)
          printf("%d ",res[r]);
          printf("\n");
      }  
    }
  return 0;
}
