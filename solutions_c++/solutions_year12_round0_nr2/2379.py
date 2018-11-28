#include <iostream>
#include <vector>
using namespace std;

unsigned maxReach(const vector<int>& v, int g, int s, int p){
  int min = p * 3 - 2;
  unsigned count = 0;
  for (int i = 0; i < v.size(); ++i){
    if (v[i] >= min)
      ++count;
    else if (v[i] >= min - 2 && min - 2 > 0 && s > 0) {
      --s; ++count;
    }
  }
  return count;
}

int main() {
  int n; cin>>n;
  for (int i = 0; i < n; ++i){
    int g, s, p; cin>>g>>s>>p;
    vector<int> v;
    for (int j = 0; j < g; ++j){
      int temp; cin>>temp;
      v.push_back(temp);
    }
    cout<<"Case #"<<i+1<<": "<<maxReach(v,g,s,p)<<endl;
  }
}
