#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdlib>
#define N 110
#define maxn 100000000
  using namespace std;
  int f[N][N],n;
  int a[N],c[N];
int main(){
  freopen("a.in","r",stdin);freopen("a.out","w",stdout);
  int i,j,k,x,y;
  int tc,tt,dx;
  char ch;
  scanf("%d",&tc);
  for(tt=1;tt<=tc;tt++){
    printf("Case #%d: ",tt);
    scanf("%d",&n);
    for(i=1;i<=n;i++){
      scanf(" %c%d",&ch,&a[i]);
      if(ch=='O')c[i]=0;
      else c[i]=1;
      }
    a[0]=c[0]=1;
    for(i=0;i<=n;i++)
      for(j=0;j<=100;j++)f[i][j]=maxn;
    f[0][1]=0;
    for(i=0;i<n;i++)
      for(x=1;x<=100;x++)
        if(f[i][x]<=maxn){
          if(c[i]==c[i+1]){
            dx=abs(a[i]-a[i+1])+1;
            for(y=x-dx;y<=x+dx && y<=100;y++){
              if(y<1)continue;
              if(f[i+1][y]>f[i][x]+dx)f[i+1][y]=f[i][x]+dx;
              }
            }
          else{
            dx=abs(a[i+1]-x)+1;
            for(y=a[i]-dx;y<=a[i]+dx && y<=100;y++){
              if(y<1)continue;
              if(f[i+1][y]>f[i][x]+dx)f[i+1][y]=f[i][x]+dx;
              }
            }
          }
    k=maxn;
    //cout<<endl;
  //  for(i=1;i<=n;i++)cout<<c[i]<<' '<<a[i]<<endl;
    for(i=1;i<=100;i++)
      if(f[n][i]<k)k=f[n][i];
    cout<<k<<endl;
    }
  return 0;
}
            
              
      
      
 
