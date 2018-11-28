#include<iostream>
#include<utility>
using namespace std;

typedef pair<int,int> pii;
typedef long long LL;

pii calc(int a[], int cur, int n, int k) {
  int val = 0;
  int i;
  for (i = 0; i < n; i++) {
    if (val + a[(cur+i)%n] <= k) {
      val += a[(cur+i)%n];
    }
    else break;
  }
  return pii((cur+i)%n, val);
}

int main() {
  int ncase, r, k, n, j;
  int index[1005], val[1005], next[1005], a[1005];
  
  cin >> ncase;
  for (int i = 1; i <= ncase; i++) {
    cin >> r >> k >> n;
    for (j = 0; j < n; j++) {
      cin >> a[j];
    }
    memset(next, -1, sizeof(next));
    memset(val, -1, sizeof(val));
    memset(index, -1, sizeof(index));
    int cur = 0;
    int counter = 0;
    while (next[cur] < 0) {
      pii tmp = calc(a, cur, n, k);
      next[cur] = tmp.first;
      val[cur] = tmp.second;
      index[cur] = counter;
      cur = next[cur];
      counter++;
    }
    int cycle = counter - index[cur];
    int offset = index[cur];
    LL val2 = 0;
    j = cur;
    do {
      val2 += val[j];
      j = next[j];
    }
    while (j != cur);

    LL ans = 0;
    cur = 0;
    while (offset > 0 && r > 0) {
      ans += val[cur];
      cur = next[cur];
      r--;
      offset--;
    }
    
    LL tmp = r / cycle;
    ans += tmp * val2;

    r -= tmp * cycle;

    while (r > 0) {
      ans += val[cur];
      cur = next[cur];
      r--;
    }
    printf("Case #%d: ", i);
    cout << ans << endl;
  }
}
