#include <iostream>
#include <algorithm> 
#include <map>
#include <vector>

using namespace std;

struct pitem {
  char a, b;

  pitem(char pa, char pb) : a(pa), b(pb) {
    if(a > b) {
      swap(a, b);
    }
  }

  bool operator==(const pitem& ci) const {
    return a == ci.a && b == ci.b;
  }

  bool operator<(const pitem& ci) const {
    if(a == ci.a)
      return b < ci.b;

    return a < ci.a;
  }
};

int main() {
  int T;
  cin >> T;
  for(int t = 0; t < T; t++) {
    map<pitem, char> combs;
    map<pitem, bool> opps;
    int C;
    cin >> C;
    for(int c = 0; c < C; c++) {
      char a, b, c;
      cin >> a >> b >> c;
      combs[pitem(a,b)] = c;
    }
    int D;
    cin >> D;
    for(int d = 0; d < D; d++) {
      char a, b;
      cin >> a >> b;
      opps[pitem(a,b)] = true;
    }
    int N;
    cin >> N;
    vector<char> inv;
    inv.reserve(N);
    for(int i = 0; i < N; i++) {
      char c;
      cin >> c;
      if(inv.size() && combs[pitem(inv.back(),c)]) {
	pitem p(inv.back(), c);
	inv.pop_back();
	inv.push_back(combs[p]);
      } else {
	inv.push_back(c);
      }

      for(int j = 0; j < (int)inv.size()-1; j++) {
	if(opps[pitem(inv[j],inv.back())]) {
	  inv.clear();
	  break;
	}
      }
    }

    cout << "Case #" << t+1 << ": [";
    for(int i = 0; i < (int) inv.size(); i++) {
      cout << inv[i];
      if(i < inv.size()-1)
	cout << ", ";
    }
    cout << "]" << endl;
  }

  return 0;
}
