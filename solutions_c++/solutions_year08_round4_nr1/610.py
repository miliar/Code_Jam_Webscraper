//#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)


int n,goal,m;
int a[20000];
bool can[20000];
int f[20000][2];


void dfs(int x){

    f[x][0]=n+10; f[x][1]=n+10;
    if (x>m) {
        f[x][a[x]]=0;
        return;
    }    
    dfs(x*2);
    dfs(x*2+1);
    int i,j,m1,m2;
    
    rep(i,2) if (f[x*2][i]>=0)
      rep(j,2) if (f[x*2+1][j]>=0){
         m1=f[x*2][i];
         m2=f[x*2+1][j];
         if (can[x]) {
           f[x][i & j]<?=m1 + m2 + (a[x]==0);
           f[x][i | j]<?=m1 + m2 + (a[x]==1);    
         }    
         else {
            if (a[x])  f[x][i & j]<?=m1 + m2; else 
                       f[x][i | j]<?=m1 + m2;
         }    
      }    
}    

int main(){
    freopen("ainput2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,k,test,cases;
    
    cases=0;
    scanf("%d",&test);
    while (test){
        test--; cases++;
        scanf("%d%d",&n,&goal);
        m=(n-1)/2;
        foru(i,1,m){
          scanf("%d%d",&j,&k);
          a[i]=j; if (k==1) can[i]=true; else can[i]=false;
        }    
        foru(i,m+1,n) scanf("%d",&a[i]);
        dfs(1);
        
        if (f[1][goal]<=n)
        printf("Case #%d: %d\n",cases,f[1][goal]);
        else 
        printf("Case #%d: IMPOSSIBLE\n",cases);
    }
    return 0;
}
