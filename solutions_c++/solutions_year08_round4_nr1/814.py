#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>

using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size

typedef long long INT;

#define sf scanf
#define pf printf

int m,v;

int inf=100000;
int value[10005];
int gate[10005];
int change[10005];

int dp[10005][2][2];

int call(int u, int val, int gt) {
    if ( u >(m-1)/2 ) {
     if ( value[u] == val ) re 0;
     else re inf;
     
    }
    if ( dp[u][val][gt] != -1 ) re dp[u][val][gt];
    int cngcost=0;
    if ( gate[u] != gt )
      if ( change[u] == 0 ) re inf;
      else cngcost = 1;
   
      int minleftor1 = call(u*2,1,0);
      int minleftand1 = call(u*2,1,1);
      int minleftor0 = call(u*2,0,0);
      int minleftand0 = call(u*2,0,1);
      
      int minritor1 = call(u*2+1,1,0);
      int minritand1 = call(u*2+1,1,1);
      int minritor0 = call(u*2+1,0,0);
      int minritand0 = call(u*2+1,0,1);
      
      if ( val == 1 ) {
         if ( gt == 1 ) {
              //and
              int a,b,c,d;
              a= minleftand1+minritand1;
              b = minleftor1+minritand1;
              c = minleftand1+minritor1;
              d = minleftor1 + minritor1;
              if ( b < a ) a = b;
              if ( c<a) a = c;
              if ( d<a ) a = d;
            dp[u][val][gt] = a+cngcost; 
         }
         else if ( gt == 0 ) {
              // or
              int a,b,c;
              a = (minleftand1<minleftor1?minleftand1:minleftor1)+
                   (minritand0<minritor0?minritand0:minritor0);
              b = (minleftand0<minleftor0?minleftand0:minleftor0)+
                   (minritand1<minritor1?minritand1:minritor1);
              
              c=  (minleftand1<minleftor1?minleftand1:minleftor1)+
                   (minritand1<minritor1?minritand1:minritor1);
              if ( b < a ) a = b;
              if ( c<a) a = c;
              dp[u][val][gt] = a + cngcost;    
         }
             
      }
      else { // val == 0
           if ( gt == 1 ) {
              //and
              int a,b,c;
              a = (minleftand0<minleftor0?minleftand0:minleftor0)+
                   (minritand0<minritor0?minritand0:minritor0);
              b = (minleftand1<minleftor1?minleftand1:minleftor1)+
                   (minritand0<minritor0?minritand0:minritor0);
              
              c=  (minleftand0<minleftor0?minleftand0:minleftor0)+
                   (minritand1<minritor1?minritand1:minritor1);
              if ( b < a ) a = b;
              if ( c<a) a = c;
              dp[u][val][gt] = a + cngcost;
              
           }
           else {  
                // or
                int a,b,c,d;
              a= minleftand0+minritand0;
              b = minleftor0+minritand0;
              c = minleftand0+minritor0;
              d = minleftor0 + minritor0;
              if ( b < a ) a = b;
              if ( c<a) a = c;
              if ( d<a ) a = d;
              dp[u][val][gt] = a+cngcost;
               
           }
      }
      
   re dp[u][val][gt]; 
}

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int kase=1;
    int t;
    sf("%d",&t);
    while ( t-- ) {
     int i;
     sf("%d %d",&m,&v);
     for(i=1;i<=(m-1)/2;i++)
      sf("%d %d",&gate[i],&change[i]);
     for( ;i<=m;i++) sf("%d",&value[i]);
     int j,k;
     for(i=1;i<=m;i++)
      for(j=0;j<2;j++)
       for(k=0;k<2;k++)
        dp[i][j][k] = -1;
     int mincost = call(1,v,0);
     int newval = call(1,v,1);
     if ( newval < mincost) mincost = newval;
     if ( mincost <= m )
        pf("Case #%d: %d\n",kase++,mincost);
     else 
       pf("Case #%d: IMPOSSIBLE\n",kase++);
    }
	return 0;
}
