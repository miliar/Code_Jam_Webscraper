#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <complex>
using namespace std;

// begin insert defines
template <class T> void PV(T &x) {for(__typeof__((x).begin()) i = (x).begin(); i != (x).end(); i++) cout << *i << " "; cout << endl;}
#define PR pair
 template<typename S, typename T> ostream& operator<<(ostream& os, pair<S,T> p){ return os << "(" << p.first << "," << p.second << ")"; };
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)
#define CR clear
#define ND second
#define FS first
#define MP make_pair
#define PB push_back
#define VR vector
// end insert defines

typedef PR<char, int> PCI;

int n;
VR<PCI> button;
VR<int> nextO, nextB;
queue<PCI> que;

void pre_set()
{
  nextO.CR(), nextB.CR();
  Rep(i, n) {
    nextO.PB(n);
    nextB.PB(n);
    for (int j = i + 1; j < n; j++)
      if (button[j].FS == 'O') {
        nextO.back() = j;
        break;
      }
    for (int j = i + 1; j < n; j++)
      if (button[j].FS == 'B') {
        nextB.back() = j;
        break;
      }
  }
  button.PB(MP('E', -1));
}

int sign(int x) {return x < 0 ? -1 : (x > 0);}

void work()
{
  pre_set();
  int nO = n, nB = n;
  for (int i = n - 1; i >= 0; i--) {
    if (button[i].FS == 'O') nO = i;
    if (button[i].FS == 'B') nB = i;
  }
  int locO = 1, locB = 1;
  int ans = 0;
  for (; !que.empty(); ans++) {
    PCI tp = que.front();
    if (tp.FS == 'O') {
      if (locO == tp.ND) {
        que.pop();
        nO = nextO[nO];
      }
      else locO += sign(button[nO].ND - locO);
      locB += sign(button[nB].ND - locB);
    }
    else {
      if (locB == tp.ND) {
        que.pop();
        nB = nextB[nB];
      }
      else locB += sign(button[nB].ND - locB);
      locO += sign(button[nO].ND - locO);
    }
  }
  cout << ans << endl;
}

void myin()
{
  while (!que.empty()) que.pop();
  cin >> n;
  button.CR();
  Rep(i, n) {
    PCI tt;
    cin >> tt.FS >> tt.ND;
    button.PB(tt);
    que.push(tt);
  }
}

int main()
{
  int tests;
  cin >> tests;
  Rep(CA, tests) {
    cout << "Case #" << CA + 1 << ": ";
    myin();
    work();
  }
  return 0;
}
