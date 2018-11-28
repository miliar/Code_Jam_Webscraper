#include<stdio.h>
#include<string.h>
int surprise[35],no_surprise[35],f[100][101],t[101],ans;

void Init(){
  int a,b,c;
  memset(surprise,0,sizeof(surprise));
  memset(no_surprise,0,sizeof(no_surprise));
  
  for(a=0;a<=10;a++)
    for(b=a;b<=10;b++)
      for(c=b;c<=10;c++){
        if (c-b<=2 && c-a<=2 && b-a<=2) {
            if (b-a==2 || c-b==2 || c-a==2) {
                if (c>surprise[a+b+c]) surprise[a+b+c]=c;
            } else if (c>no_surprise[a+b+c]) no_surprise[a+b+c]=c;
        }
      }
}

int min(int a,int b){
  return (a>b)?b:a;
}

void DP(int n,int s,int p){
  int i,j,max;
  memset(f,0,sizeof(f));
  
  for(i=1;i<=n;i++){
     if (no_surprise[t[i]]>=p) f[i][0]=f[i-1][0]+1;
                          else f[i][0]=f[i-1][0];
  }
  
  for(i=1;i<=n;i++)
    for(j=1;j<=min(i,s);j++){
      if (i==j) {
        if (surprise[t[i]]>=p) f[i][j]=f[i-1][j-1]+1;
                         else  f[i][j]=f[i-1][j-1];
      } else {
        if (no_surprise[t[i]]>=p) max=f[i-1][j]+1;
                             else max=f[i-1][j];
        
        if (surprise[t[i]]>=p) {
          if (f[i-1][j-1]+1>max) max=f[i-1][j-1]+1;
        } else {
          if (f[i-1][j-1]>max) max=f[i-1][j-1];
        }
        f[i][j]=max;
      }
    }
  
  ans=f[n][s];
}

int main(){
  int n,s,p,tt,i,j;
  
  //freopen("B-large.in","r",stdin);
  //freopen("B-large.out","w",stdout);
  
  Init();
  scanf("%d",&tt);
  for(i=1;i<=tt;i++){
    scanf("%d%d%d",&n,&s,&p);
    for(j=1;j<=n;j++){
      scanf("%d",&t[j]);
    }
    DP(n,s,p);
    printf("Case #%d: %d\n",i,ans);
  }
  return 0;
}
