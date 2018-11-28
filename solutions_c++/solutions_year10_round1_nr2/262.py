
#include <iostream>

using namespace std;

int a[101];
int d[101][257];

int Diff (int x) {
  if (x < 0) {
    return -x;
  }
  return x;
}

int D, I, M, n;
void Output() {
  cout << endl;
  for (int i = 0; i < n; ++i) {
    for (int j = 60; j <= 65; ++j) {
      cout << d[i][j] << ' ';
    }
    cout << endl;
  }
  cout << endl;
}



void process() {
  int EMPTY = 256;
  cin >> D >> I >> M >> n;
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }
  memset (d, 0, sizeof (d));
  d[0][EMPTY] = D;
  for (int i = 0; i <= 255; ++i) {
    d[0][i] = Diff (a[0] - i);
  }
  
  for (int i = 1; i < n; ++i) {
    for (int j = 0; j <= 255; ++j) {
      int ch = Diff (a[i] - j);
      int minv = d[i-1][j] + D;
      minv = min (minv, d[i-1][EMPTY] + ch);
      minv = min (minv, d[i-1][j] + ch);
      if (M > 0) {
        for (int k = 0; k <= 255; ++k) {
          int ins_diff = Diff (j - k) - 1; 
          int v = d[i-1][k] + ch;
          if (ins_diff >= 0) {
            v += (ins_diff / M) * I;
          }
          minv = min(minv, v);
        }
      }
      d[i][j] = minv;
      d[i][EMPTY] = d[i-1][EMPTY] + D;
    }
  }

  // Output();

  int ansv = (int)1e9;
  for (int i = 0; i <= EMPTY; ++i) {
    if (ansv > d[n-1][i]) {
      ansv = d[n-1][i];
    }
  }
  printf ("%d\n", ansv);
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t;++i) {
    printf ("Case #%d: ", i+1);
    process();
  }
}

