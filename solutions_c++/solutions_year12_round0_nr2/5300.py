#include <iostream>

using namespace std;

int tCase() {
  int p,s,n,c,t;
  t = 0;
  cin >> n >> s >> p;
  for (int i = 0; i < n; ++i) {
    cin >> c;
    if (c >= p + ((p-1)>0?p-1:0)*2 && p <= p*3 ) {
      ++t;
    }
    else if (s > 0 && c >= p + ((p-2)>0?p-2:0)*2 && p <= p*3) {
      --s;
      ++t;
    }
  }
  return t;
}

int main () {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cout << "Case #" << (i+1) << ": " << tCase() << endl;
  }
  return 0;
}

