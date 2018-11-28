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
#define MAXN 60
#define MAXM 60

int n,m,q;
int ans,sum,tmp;
int MAX,MIN;

char a[MAXN][MAXM];

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.txt","w",stdout);
    scanf("%d",&q);
    for(int t=1;t<=q;t++)
    {
     scanf("%d%d",&n,&m);
     FOR(i,0,n)
      scanf("%s",a[i]);
     FOR(i,0,n-1)
      FOR(j,0,m-1)
       if(a[i][j]=='#'&&a[i+1][j]=='#'&&a[i][j+1]=='#'&&a[i+1][j+1]=='#')
        a[i][j]=a[i+1][j+1]='/',a[i+1][j]=a[i][j+1]='\\';

     bool c=0;
     FOR(i,0,n)
      FOR(j,0,m)
       if(a[i][j]=='#')
        c=1,i=n,j=m;

     printf("Case #%d:\n",t);
     if(c) printf("Impossible\n");
     else
      FOR(i,0,n)
       printf("%s\n",a[i]);
    }
}
