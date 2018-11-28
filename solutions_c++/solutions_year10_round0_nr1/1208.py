#include <iostream>

using namespace std;

int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    int n,k;
    cin>>n>>k;
    cout<<"Case #"<<i<<": "<<((((1<<n)-1) & ~k)?"OFF":"ON")<<endl;
  }
  return 0;
}
