#include <stdio.h>
#define FOR(q,n) for(int q=0; q<n; q++)
#include <vector>
#include <algorithm>
using namespace std;

bool test(vector<int>& data, int distance, double time) {
 if (data.empty()) return true;
 double marker = data[0] - time;
 for (int q=1; q<(int) data.size(); q++) {
  marker += distance;
  double low = data[q] - time;
  double high = data[q] + time;
  double tmp = max(low, marker);
  if (tmp > high) return false;
  marker = tmp;
 }
  return true;
}

void solve() {
 int c;
 int d;
 scanf("%d %d", &c, &d);
 vector<int> data;
 FOR(q, c) {
   int x, cnt;
  scanf("%d %d", &x, &cnt);
  FOR(w, cnt)
    data.push_back(x);
 }
 double left = 0;
 double right = 1e15;
 FOR(q, 100) {
  double middle = (left + right)/2;
  if (test(data, d, middle)) {
    right = middle;
  } else {
    left = middle;
  }
 }

 printf("%lf\n", left);
}


int main() {
  int t;
  scanf("%d", &t);
  FOR(q, t) {
    fprintf(stderr, "case %d\n", q);
    printf("Case #%d: ", q+1);
    solve();
  }

}
