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
#define MAXN 10010

int n,m,q;
int ans,sum,tmp;
int MAX,MIN;

int a[MAXN];

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.txt","w",stdout);
    scanf("%d",&q);
    int h,l;
    for(int t=1;t<=q;t++)
    {
     scanf("%d%d%d",&n,&h,&l);
     FOR(i,0,n)
      scanf("%d",&a[i]);

     while(h<=l)
     {
      bool c=0;
      FOR(j,0,n)
       if(max(h,a[j])%min(h,a[j])!=0)
       { c=1; break; }
      if(!c) break;
      h++;
     }

     printf("Case #%d: ",t);
     if(h<=l) printf("%d\n",h);
     else printf("NO\n");
    }
}
