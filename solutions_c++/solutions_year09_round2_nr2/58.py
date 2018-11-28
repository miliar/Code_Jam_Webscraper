#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int iT=0; iT<T; ++iT) {
    string n;
    cin >> n;
    assert(n!="0");
    if (next_permutation(n.begin(),n.end())) {
      cout << "Case #" << iT+1 << ": " << n << endl;
    }
    else {
      n+='0';
      sort(n.begin(),n.end());
      int j=0;
      for (; j<n.size() && n[j]=='0'; ++j);
      n=n[j]+n.substr(0,j)+n.substr(j+1);
      cout << "Case #" << iT+1 << ": " << n << endl;
    }
  }
}
