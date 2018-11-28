#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int i = 0; i < T; ++i){
    int ret = 0;
    int n, h;
    cin >> n;
    vector<int> data;
    for(int j = 0; j < n; ++j){
      cin >> h;
      data.push_back(h);
    }
    sort(data.begin(), data.end());
    data.push_back(0);
    vector<int> s1(n, 0), s2(n, 0);
    int r = 0;
    for(int j = 0; j < n; ++j)
      s1[j] = r = r xor data[j];
    r = 0;
    for(int j = n - 1; j >= 0; --j)
      s2[j] = r = r xor data[j];
    for(int j = 0; j < n; ++j) if(s1[j] == s2[j + 1]){
      for(int k = j + 1; k < n; ++k)
        ret += data[k];
      break;
    }
    if(ret == 0) cout << "Case #" << i + 1 << ": NO" << endl;
    else cout << "Case #" << i + 1 << ": " << ret << endl;
  }
}
