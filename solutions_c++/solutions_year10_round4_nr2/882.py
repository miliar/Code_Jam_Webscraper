#include <vector>
#include <utility>
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
#include <cstdio>
#include <list>

using namespace std;

typedef struct node{
        int id, val;
        };
bool flag[12][1025];
int p;
node m[1030];
int a[12][1025];

bool cmp(node x, node y)
{
   if(x.val == y.val) return(x.id < y.id);
   return(x.val > y.val);
}

int main()
{
freopen("B-small-attempt3.in","r",stdin);
freopen("E:/out.txt","w",stdout);
   int t,test = 0;
   scanf("%d",&t);
   while(t--)
   {
       scanf("%d",&p);
       memset(flag,0,sizeof(flag));
       for(int i = 1; i <= (1<<p); i++) { scanf("%d",&m[i].val); m[i].val = p - m[i].val; m[i].id = i; }
       for(int i = 1; i <= p; i++)
       {
           for(int j = 1; j <= 1<<(p-i); j++) scanf("%d",&a[i][j]);
       }
       sort(m+1,m+1+(1<<p),cmp);
       //for(int i = 1; i <= (1<<p); i++) cout<<m[i].id<<' '<<m[i].val<<endl;
       int ans = 0;
       for(int i = 1; i <= (1<<p); i++)
       {
           int num = m[i].val;
               if(!num) continue;
               //for(int j = 1; j <= p; j++)
               for(int j = p; j >= 1; j--)
               {
                   int tmp = m[i].id / (1<<j);
                   if(m[i].id % (1<<j) ) tmp++;
                   if(!flag[j][tmp]) 
                   {
                      ans ++; 
                      flag[j][tmp] = 1;
                      //cout<<m[i].id<<' ';
                   }
                   num --;
                   if(!num) break;
               }  //cout<<endl;
       }
       printf("Case #%d: %d\n",++test,ans);
   }
   return(0);
}
  
             
