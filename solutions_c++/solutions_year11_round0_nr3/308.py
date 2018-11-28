#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
using namespace std;
int main(){
  int T;cin >> T;
  for(int c=1;c<=T;++c){
    int N;cin>>N;
    int n = 0;
    int m = 1000000;
    int C;
    long long sum = 0;
    for(int i=0;i<N;++i){
      cin>>C;
      m=min(C,m);
      sum+=C;
      n^=C;
    }
    if(n!=0)cout << "Case #"<<c<<": NO" << endl;
    else cout << "Case #"<<c<<": "<<(sum-m) << endl;
  }
}

