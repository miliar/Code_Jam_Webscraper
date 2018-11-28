#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

long a[300][300],b[300][300],i,j,k,n,t,m,p,x,y,sa[300],fa[300],sb[300],fb[300],A,B,q;
bool fix[300];


bool pathA(long s,long f){
  long i;
  fix[s]=true;
  if(s==f)return true;
  for(i=0;i<n+m+2;i++)
    if(a[s][i]>0&&!fix[i])
      if(pathA(i,f)){
        a[s][i]--;
        a[i][s]++;
        return true;
      }
  return false;
}


bool pathB(long s,long f){
  long i;
  fix[s]=true;
  if(s==f)return true;
  for(i=0;i<n+m+2;i++)
    if(b[s][i]>0&&!fix[i])
      if(pathB(i,f)){
        b[s][i]--;
        b[i][s]++;
        return true;
      }
  return false;
}


main(){
  freopen("b.in","r",stdin);
  freopen("b.out","w",stdout);
  scanf("%d",&t);
  for(q=0;q<t;q++){
    scanf("%d\n",&p);
    scanf("%d%d\n",&n,&m);
    for(i=0;i<n;i++){
      scanf("%d:%d",&x,&y);
      sa[i]=x*60+y;
      scanf("%d:%d",&x,&y);
      fa[i]=x*60+y;
    }
    for(i=0;i<m;i++){
      scanf("%d:%d",&x,&y);
      sb[i]=x*60+y;
      scanf("%d:%d",&x,&y);
      fb[i]=x*60+y;
    }
    for(i=0;i<n+m+2;i++)
      for(j=0;j<n+m+2;j++)
        a[i][j]=b[i][j]=0;
        
    for(i=0;i<n;i++)
      for(j=0;j<m;j++)
        if(fa[i]+p<=sb[j])
          a[i+1][n+j+1]=1;
    for(i=0;i<n;i++)
      a[0][i+1]=1;
    for(j=0;j<m;j++)
      a[n+j+1][n+m+1]=1;

    for(i=0;i<m;i++)
      for(j=0;j<n;j++)
        if(fb[i]+p<=sa[j])
          b[i+1][m+j+1]=1;
    for(i=0;i<m;i++)
      b[0][i+1]=1;
    for(j=0;j<n;j++)
      b[m+j+1][m+n+1]=1;
    A=0;
    while(1){
      for(i=0;i<n+m+2;i++) fix[i]=false;
      if(pathA(0,n+m+1)) A++; else break;
    }
    B=0;
    while(1){
      for(i=0;i<n+m+2;i++) fix[i]=false;
      if(pathB(0,n+m+1)) B++; else break;
    }
    printf("Case #%d: %d %d\n",q+1,n-B,m-A);
  }
}
