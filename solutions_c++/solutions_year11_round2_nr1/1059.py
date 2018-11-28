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
#define MAXN 110

int n,m,q;
int ans,sum,tmp;
int MAX,MIN;

char a[MAXN][MAXN];
double wp[MAXN],owp[MAXN],oowp[MAXN],x[MAXN],y[MAXN];

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.txt","w",stdout);
    scanf("%d",&q);
    for(int t=1;t<=q;t++)
    {
     scanf("%d",&n);
     FOR(i,0,n)
      scanf("%s",a[i]);
     FOR(i,0,n)
     {
      x[i]=y[i]=0;
      FOR(j,0,n)
      {
       if(a[i][j]!='.') y[i]++;
       if(a[i][j]=='1') x[i]++;
      }
      if(y!=0) wp[i]=x[i]/y[i];
      else wp[i]=0;
     }
     FOR(i,0,n)
     {
      double Sum=0,d=0;
      FOR(j,0,n)
       if(a[j][i]!='.')
       {
        if(a[j][i]=='1') Sum+=(x[j]-1.0)/(y[j]-1.0);
        else Sum+=(x[j])/(y[j]-1.0);
        d++;
       }
      owp[i]=Sum/d;
     }
     FOR(i,0,n)
     {
      double Sum=0,d=0;
      FOR(j,0,n)
       if(a[i][j]!='.')
        Sum+=owp[j],d++;
      oowp[i]=Sum/d;
     }

     printf("Case #%d:\n",t);
     FOR(i,0,n)
      printf("%.12lf\n",0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i]);
    }
}
