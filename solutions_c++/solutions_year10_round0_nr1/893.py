#include<iostream>

using namespace std;

int main(){
  int T,N,K;
  cin>>T;
  for (int i=1;i<=T;i++){
    cin>>N>>K;
    int test = (1<<N)-1;
    if ((K&test)==test)
      cout<<"Case #"<<i<<": ON"<<endl;
    else
      cout<<"Case #"<<i<<": OFF"<<endl;
  }
}
