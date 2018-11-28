#include <iostream>
#include <cstring>
#include <cmath>
  using namespace std;
int main(){
  freopen("a.in","r",stdin);freopen("a.out","w",stdout);
  int test,tt;
  int x,y,i,j,k;
  cin>>test;
  for(tt=1;tt<=test;tt++){
    printf("Case #%d: ",tt);
    cin>>x>>y;
    i=(1<<x);
    y=y%i;
    if(y==i-1)cout<<"ON"<<endl;
    else cout<<"OFF"<<endl;
    };
  return 0;
}
