#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
  int t;
  cin>>t;
  for(int i = 0 ; i < t; i++){
    int n;
    cin>>n;
    vector<int> can;
    long long sum = 0;
    int div = 0;
    for(int j = 0 ; j < n ; j++){
      int tmp;
      cin>>tmp;
      can.push_back(tmp);
      sum += tmp;
      div ^= tmp;
    }
    sort(can.begin() , can.end());
    if(div == 0){
      sum -= can[0];
      cout<<"Case #"<<(i+1)<<": "<<sum<<endl;
    }
    else{
      cout<<"Case #"<<(i+1)<<": NO"<<endl;
    }
    
  }
}
