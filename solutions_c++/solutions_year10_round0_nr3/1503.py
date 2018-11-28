#include <iostream>
using namespace std;

int main() {
  int problem;
  cin >> problem;

  for(int iii=1; iii<=problem; iii++) {
    int r, k, n;
    cin >> r >> k >> n;

    int g[2*n];
    for(int i=0; i<n; i++) {
      cin >> g[i];
      g[n+i] = g[i];
    }

    int euros[n];
    int next[n];
    int head_count = 0;
    int tail = 0;
    for(int i=0; i<n; i++) {
      while(head_count+g[tail] <= k && tail < i+n) {
        head_count += g[tail++];
      }

      euros[i] = head_count;
      next[i] = tail % n;
      head_count -= g[i];
    }

    int pos=0;
    long long result=0;
    for(int i=0; i<r; i++) {
      result += euros[pos];
      pos = next[pos];
    }

    cout << "Case #" << iii << ": " << result << endl;
  }

  return 0;
}
