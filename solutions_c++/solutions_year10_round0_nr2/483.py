#include <iostream>
#include <cstring>
  using namespace std;
  int n,a[10];
int gcd(int x,int y){
  if (y==0)return x;
  return gcd(y,x % y);
};
int main(){
  freopen("b.in","r",stdin);freopen("bb.out","w",stdout);
  int  test,tt,x,y,z,ans,tem,i,j,k;
  scanf("%d\n",&test);
  for(tt=1;tt<=test;tt++){
    printf("Case #%d: ",tt);
    cin>>n;
    for(i=1;i<=n;i++)cin>>a[i];
    ans=0;
    for(i=1;i<n;i++)
    for(j=i+1;j<=n;j++){
      k=abs(a[i]-a[j]);
      if(k==0)continue;
      ans=gcd(ans,k);
      };
    k=a[1]%ans;
    ans=(ans-k)%ans;
    cout<<ans<<endl;
    };
  return 0;
}
      
