#include <iostream>
#include <cstring>
#include <cmath>
#define N 52
  using namespace std;
  bool flag1,flag2;
  int n,m,ori[N][N],a[N][N];
int main(){
  freopen("a.in","r",stdin);freopen("a.out","w",stdout);
  int tst,tt,i,j,k,x,y;
  char s[60];
  scanf("%d\n",&tst);
  for(tt=1;tt<=tst;tt++){
    printf("Case #%d: ",tt);
    scanf("%d%d\n",&n,&m);
    for(i=1;i<=n;i++){
      scanf("%s\n",s);
      for(j=1;j<=n;j++){
        if(s[j-1]=='.')ori[i][j]=0;
        else if(s[j-1]=='B')ori[i][j]=1;
        else ori[i][j]=2;
        };
      };
    memset(a,0,sizeof(a));
    for(i=1;i<=n;i++)
    for(j=1;j<=n;j++)
    a[j][n+1-i]=ori[i][j];
   
    for(i=n-1;i>0;i--)
    for(j=1;j<=n;j++)
    if(a[i][j]>0){
      k=i;
      while(k<n && a[k+1][j]==0){
        a[k+1][j]=a[k][j];a[k][j]=0;
        k++;
        };
      };
    flag1=flag2=false;
    for(i=1;i<=n;i++)
    for(j=1;j<=n;j++)
    if(a[i][j]>0){
      k=0;
      while(a[i][j]==a[i][j+k])k++;
      if(k>=m){
        if(a[i][j]==1)flag1=true;
        else flag2=true;
        };
      k=0;
      while(a[i][j]==a[i+k][j])k++;
       if(k>=m){
        if(a[i][j]==1)flag1=true;
        else flag2=true;
        };
      k=0;
      while(a[i][j]==a[i+k][j+k])k++;
       if(k>=m){
        if(a[i][j]==1)flag1=true;
        else flag2=true;
        };
      k=0;
      while(a[i][j]==a[i+k][j-k])k++;
       if(k>=m){
        if(a[i][j]==1)flag1=true;
        else flag2=true;
        };
       };
    if(flag1 && flag2)cout<<"Both"<<endl;
    else if(flag1)cout<<"Blue"<<endl;
    else if(flag2)cout<<"Red"<<endl;
    else cout<<"Neither"<<endl;
    };
  return 0;
}
      
      
      
