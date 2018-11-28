#include<iostream>
using namespace std;
long long gcd(long long a,long long b){
  if(b)
    while((a=a%b) && (b=b%a));
  return a+b;
}
int main(void){
  int t;
  cin>>t;
  for(int c=1;c<=t;++c){
    long long n,d,g;
    cin>>n>>d>>g;
    cout<<"Case #"<<c<<": ";
    if(g==0 && d!=0 || g==100&&d!=100)
      cout<<"Broken";
    else if(100/gcd(d,100) > n)
      cout<<"Broken";
    else
      cout<<"Possible";
    cout<<endl;
  }
  return 0;
}
