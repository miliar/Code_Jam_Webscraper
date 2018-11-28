#include<iostream>

using namespace std;

long long gcd(long long a,long long b){
  long long tmp;
  while(b!=0){
    tmp=b;
    b=ldiv(a,b).rem;
    a=tmp;
  }
  return a;
}

int main(){
  int c; cin >> c;
  for(int x=0;x<c;x++){
    int n; cin >> n;
    long long a,b,c,g;
    if(n==2){
      cin >> a >> b;
      g=labs(a-b);
    }else{
      cin >> a >> b >> c;
      g=gcd(labs(a-b),gcd(labs(b-c),labs(a-c)));
    }
    long long ans=0;
    while(ans<a){
      ans+=g;
    }
    printf("Case #%d: ",x+1);
    cout << ans-a << endl;
  }
  return 0;
}
