#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

const int maxn = 500 + 5;
const int maxsum = 2 * 1000 * 1000 + 5;
int a[maxn];
int used[maxsum];

void view(int mask, int n)
{
  for (int i = 0; i < n; ++i) {
    if (mask & (1 << i)) {
      cout << a[i] << ' ';
    }
  }
  cout << '\n';
}

void solve(int test_id)
{
  cout << "Case #" << test_id << ":\n";
  
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }
  
  memset(used, 0, sizeof(used));
  
  int mm = 1 << n;
  for (int mask = 0; mask < mm; ++mask) {
    int sum = 0;
    for (int i = 0; i < n; ++i) {
      if (mask & (1 << i)) {
        sum += a[i];
      }
    }
    
    if (used[sum]) {
      view(used[sum], n);
      view(mask, n);
      return;
    }
    
    used[sum] = mask;
  }
  
  cout << "Impossible\n";
}

int main()
{
  freopen("C.in", "r", stdin);
  
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    solve(i);
  }
  
  return 0;
}