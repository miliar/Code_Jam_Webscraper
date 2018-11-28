#include <cstdio>
#include <iostream>

using namespace std;

typedef long double ld;

const int maxn = 200 + 5;
const int bp_steps = 200;

ld s[maxn];

void solve(int & test_id)
{
  int n;
  cin >> n;
  ld X = 0;
  for (int i = 0; i < n; ++i) {
    cin >> s[i];
    X += s[i];
  }
  
  ld sum = 0;
  cout << "Case #" << test_id << ": ";
  for (int i = 0; i < n; ++i) {
    ld l = 0, r = 1;
    for (int step = 0; step < bp_steps; ++step) {
      ld w = (l + r) / 2;
      
      bool good = 0;
      ld w_sum = 1 - w;
      ld pts = s[i] + X * w;
      for (int j = 0; j < n; ++j) if (j != i) {
        if (s[j] >= pts) {
          continue;
        }
        ld min_w = (pts - s[j]) / X;
        w_sum -= min_w;
      }
      
      good |= w_sum <= 0.0;
      
      if (good) {
        r = w;
      }
      else {
        l = w;
      }
    }
    
    ld w = l * 100;
    
    cout << w << ' ';
    sum += w;
  }
  
  //cout << " | " << sum;
  
  cout << '\n';
}

int main()
{
  freopen("A.in", "r", stdin);
  
  ios::sync_with_stdio(0);
  cout.setf(ios::fixed);
  cout.precision(6);
  
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    solve(i);
  }
  
  return 0;
}