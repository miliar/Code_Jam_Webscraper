#include <iostream>

using namespace std;

bool answer(int n,int k);

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    int n,k;
    cin>>n>>k;
    cout<<"Case #"<<i+1<<": "<<(answer(n,k)?"ON":"OFF")<<'\n';
  }
}

bool answer(int n,int k){
  int p2=1<<n;
  int all=p2-1;
  k%=p2;
  return all==k;
}
