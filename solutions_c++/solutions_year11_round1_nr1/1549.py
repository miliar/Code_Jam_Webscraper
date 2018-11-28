/*
  ------ HachiInfinity ------
  ------ Worrachate Bosri ------
  ------ Mahidol Wittayanusorn ------
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<utility>
using namespace std;

#define FOR(i,ST,FN) for(int i=ST;i<FN;i++)
#define mod
#define inf
#define PAUSE system("pause")
#define upper_bound high=mid-1
#define lower_bound low=mid+1
#define MAXN 200200

int n,m,q;
int ans,sum,tmp;
int MAX,MIN;

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.txt","w",stdout);
    int t,pd,pg;
    scanf("%d",&t);
    FOR(k,0,t)
    {
     scanf("%d%d%d",&n,&pd,&pg);
     printf("Case #%d: ",k+1);
     if(pd!=100&&pg==100) printf("Broken\n");
     else if(pd!=0&&pg==0) printf("Broken\n");
     else
     {
      int c=0;
      for(int i=1;i<=n;i++) if(i*pd%100==0) { c=1; break; }
      if(c) printf("Possible\n");
      else printf("Broken\n");
     }
    }
}
