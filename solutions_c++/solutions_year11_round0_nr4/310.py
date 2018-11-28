#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <boost/format.hpp>
using namespace std;
int main(){
  int T;cin >> T;
  for(int c=1;c<=T;++c){
    int N;cin>>N;
    vector<int> arr(N);
    for(int i=0;i<N;++i)cin>>arr[i];
    vector<bool> check(N);fill(check.begin(),check.end(),false);
    double res = 0.0;
    for(int i=0;i<N;++i){
      if(!check[i]){
        int tmp = 0;
        int t = i;
        while(!check[t]){
          check[t]=true;
          tmp++;
          t=arr[t]-1;
        }
        res+=(tmp<=1)?0:tmp;
      }
    }
    cout << "Case #"<<c<<": "<<boost::format("%.6f")%res << endl;
  }
}
