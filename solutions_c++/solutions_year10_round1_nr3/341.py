#include <iostream>
#include <cstring>
#include <cmath>
#define N 1100
  using namespace std;
  int a1,a2,b1,b2,ans;
int gcd(int x,int y){
  if(y==0)return x;
  return gcd(y,x % y);
};
bool dfs(int x,int y){
  if(x==y)return false;
  int k;
  if(x<y){
    k=x;x=y;y=k;
    };
  if(x % y==0)return true;
  k=x/y;
  if(k==1){
    if(!dfs(y,x%y))return true;
    else return false;
    }
  else return true;
};
int main(){
  freopen("c1.in","r",stdin);freopen("c1.out","w",stdout);
  int tst,tt,i,j,x,y,k;
  scanf("%d\n",&tst);
  for(tt=1;tt<=tst;tt++){
    printf("Case #%d: ",tt);
    scanf("%d%d%d%d\n",&a1,&a2,&b1,&b2);
    ans=0;
    for(i=a1;i<=a2;i++)
    for(j=b1;j<=b2;j++)
    if(dfs(i,j))ans++;
    cout<<ans<<endl;
    };
  return 0;
}
