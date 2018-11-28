#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> vi;

int main(){
  int k, i = 0;
  cin >> k;
  while(k--){
    int ret = 0;
    int n, s, p;
    cin >> n >> s >> p;
//    cout << "s: " << s << " p: " << p << endl;
    vi data(n);
    for(int j = 0; j < n; ++j) cin >> data[j];
    int mini = p + max(0, p-2) + max(0, p-2);
    int maxi = p + max(0, p-1) + max(0, p-1);
//    cout << "mini: " << mini << " maxi: " << maxi << endl;
    for(int j = 0; j < n; ++j){
      if(data[j] < mini) continue;
      if(data[j] >= maxi)
        ++ret;
      else if(s){
        ++ret;
        --s;
      }
    }
    cout << "Case #" << ++i << ": " << ret << endl;
  }
}

