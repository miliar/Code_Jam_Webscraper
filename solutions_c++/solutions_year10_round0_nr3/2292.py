#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
using namespace std;
typedef long long ll;
int g[1010];

ll solve(int r, int k, int n)
{
  int start = 0;
  ll cost = 0;

  ll total = 0;
  for (int i = 0; i < n; i++)
    total += g[i];
  
  if (total <= k) {
    return r * total;
  }

  for (int i = 0; i < r; i++) {
    int num_pass = k;
    while (num_pass > 0) {
      //cerr << num_pass << ", " << g[start] << endl;
      if (g[start] <= num_pass) {
        num_pass -= g[start];
        start = (start +1) % n;
      } else break;
    }
    cost += (k - num_pass);
  }
  return cost;
}

int main(int argc, char **argv)
{
  int T;
  cin >> T;
  
  for (int i = 0; i < T; i++) {
    int R, k, N;
    cin >> R >> k >> N;
    memset(g, 0, sizeof(g));
    for (int j = 0; j < N; j++) {
      cin >> g[j];
    }
    ll num = solve(R, k, N);
    cout << "Case #" << i+1 << ": " << num << endl;
  }
  
  return 0;
}
