#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int candy_split(vector<int> candy){
  int xord = 0, sum = 0;
  for (int i = 0; i < candy.size(); ++i){
    xord = xord ^ candy[i];
    sum += candy[i];
  }
  //cout<<xord<<endl;
  if (xord)
    return -1;
  sort(candy.begin(), candy.end());
  return sum - candy[0];
}

int main(){
  int t; cin>>t;
  for (int count = 1; count <= t; ++count){
    int n; cin>>n;
    vector<int> candy;
    for (int i = 0; i < n; ++i){
      int temp; cin>>temp; candy.push_back(temp);
    }
    int result = candy_split(candy);
    cout<<"Case #"<<count<<": ";
    if (result < 0)
      cout<<"NO";
    else
      cout<<result;
    cout<<endl;
  }
}
