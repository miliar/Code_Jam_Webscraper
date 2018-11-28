#include<iostream>
#include<math.h>
#include<stdlib.h>
using namespace std;
int main(void){
  int t,n,k,s;
  while(cin>>t){
    for(int i=1;i<=t;++i){
      cin>>n>>k;
      s = (int)ceil(pow(2,n));
      if(k%s == s-1)
        cout<<"Case #"<<i<<": ON"<<endl;
      else 
        cout<<"Case #"<<i<<": OFF"<<endl;      
    }
  }
  return 0;
}
