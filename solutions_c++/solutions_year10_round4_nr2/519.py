#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <set>
using namespace std;


int n;
int m[1024];
int pri[1024];
int stat[1024][16];

int run(int node, int miss) {
  if (stat[node][miss] != -1) return stat[node][miss];

  if (node < (1 << (n - 1)) - 1) {
    int a = run(node * 2 + 1, miss + 1);
    int b = run(node * 2 + 2, miss + 1);
    int t = -2;
    if (a >= 0 && b >= 0) {
      t = a + b;
    }

    a = run(node * 2 + 1, miss);
    b = run(node * 2 + 2, miss);
    if (a >= 0 && b >= 0) {
      int tt = a + b + pri[node];
      if (t == -2 || t > tt) {
        t = tt;
      }
    }
    return (stat[node][miss] = t);
  } else {
    int k = node - ((1 << (n - 1)) - 1);
    int a = m[k * 2], b = m[k * 2 + 1];
    if (miss + 1 <= a && miss + 1 <= b) {
      return (stat[node][miss] = 0);
    } else if (miss <= a && miss <= b) {
      return (stat[node][miss] = pri[node]);
    } else {
      return (stat[node][miss] = -2);
    }
  }
}

int Go() {
  cin >> n;
  for (int i = (1 << n) - 1; i >= 0; --i) {
    cin >> m[i];
  }
  for (int i = (1 << n) - 2; i >= 0; --i) {
    cin >> pri[i];
  }
  for (int i = 0; i < 1024; ++i) {
    for (int j = 0; j < 16; ++j) {
      stat[i][j] = -1;
    }
  }
  return run(0, 0);
}


int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cout << "Case #" << i + 1 << ": " << Go() << endl;
  }

  return 0;
}