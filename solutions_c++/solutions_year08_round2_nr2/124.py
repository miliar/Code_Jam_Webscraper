#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int vis[1000], used[1000], adj[1000][1000];
bool prime(long long x) {
  if (x < 2) return false;
  for (long long i = 2; i*i<=x; ++i)
    if (x%i==0)
      return false;
  return true;
}
vector<long long> primes;
void dfs(int x) {
  if (vis[x]) return;
  vis[x] = 1;
  for (int i = 0; i < primes.size(); ++i)
    if (adj[x][i])
      dfs(i);
}
int main() {
  int no_cases;
  cin >> no_cases;
  for (int rr = 1; rr <= no_cases; ++rr) {
    int ret = 0;
    memset(adj, 0, sizeof(adj));
    memset(vis, 0, sizeof(vis));
    memset(used, 0, sizeof(used));
    primes = vector<long long>();
    long long A, B, P;
    cin >> A >> B >> P;
    for (long long i = P; i <= B; ++i)
      if (prime(i)) 
	primes.push_back(i);
    for (long long i = A; i <= B; ++i) {
      vector<int> l;
      for (int j = 0; j < primes.size(); ++j)
	if (i % primes[j] == 0)
	  used[j] = 1, l.push_back(j);
      for (int k = 0; k < l.size(); ++k)
	for (int r = k + 1; r < l.size(); ++r)
	  adj[l[k]][l[r]] = adj[l[r]][l[k]] = 1;
      if (!l.size())
	++ret;
    }
    for (int i = 0; i < primes.size(); ++i)
      if (used[i] && !vis[i]) 
	++ret, dfs(i);
    printf("Case #%d: %d\n", rr, ret);
  }
  return 0;
}
