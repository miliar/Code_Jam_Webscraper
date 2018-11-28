#include <iostream>
#include <vector>

using namespace std;

typedef pair<int, int> ii;

// orange = 1, blue = 0

int sgn(int i) {
  if (i > 0) return 1;
  if (i < 0) return -1;
  return 0;
}

struct Case {
  int nr;
  vector<ii> seq;
  int seqdone;
  
  int res;
  
  int pos[2];
  
  Case(int n) : nr(n) {
    seqdone = 0;
    res = 0;
    pos[0] = pos[1] = 0;
    
    read();
    solve();
    print();
  }
  
  void read() {
    int n; cin >> n;
    for (int i=0;i<n;i++) {
      int k; char c;
      cin.ignore();
      cin >> c >> k;
      seq.push_back(ii(c=='O', k));
    }
  }
  
  int next(int robot) {
    for (int i=seqdone; i < (int)seq.size(); i++) {
      if (seq[i].first == robot)
        return sgn(seq[i].second - pos[robot]);
    }
    return 1;
  }
  
  void solve() {
    while (seqdone < (int)seq.size()) {
      bool step = 0;
      for (int i=0; i<2; i++) {
        int n = next(i);
        step |= (n==0 && seq[seqdone].first == i);
        pos[i] += n;
      }
      seqdone += step;
      res++;
    }
  }
  
  void print() {
    printf("Case #%d: %d\n", nr, res-1);
  }
  
};

int main() {
  int n; cin >> n;
  for(int i=1; i<=n; i++) {
    Case c(i);
  }
}