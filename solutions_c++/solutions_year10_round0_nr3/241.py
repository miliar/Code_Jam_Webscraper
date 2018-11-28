
#include <stdio.h>
#include <iostream>


using namespace std;

typedef long long LL;

int d[1000];
LL money[1000];
int iter[1000];


void process() {
  int r, k, n;
  cin >> r >> k >> n;
  for (int i = 0; i < n; ++i) {
    cin >> d[i];
  }
  int idx = 0;
  memset(money, 0, sizeof(money));
  memset(iter, -1, sizeof(iter));
  LL total = 0;
  iter[0] = 0;
  money[0] = 0;
  for (int i = 0; i < r;) {
    int sum = 0;
    for (int j = 0; j < n; ++j) {
      if (sum + d[idx] > k) {
        break;
      }
      sum += d[idx];
      idx = ++idx % n;
    }
    total += sum;
    if (iter[idx] != -1) {
      int cycle = i+1 - iter[idx];
      LL m = total - money[idx];
      LL quo = (r-i-1) / cycle;
      i += quo * cycle + 1;
      total += quo * m;
    } else {
      iter[idx] = i+1;
      money[idx] = total;
      ++i;
    }
  }
  cout << total << endl;
}





int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    printf("Case #%d: ", i+1);
    process();
  }
  return 0;
}
