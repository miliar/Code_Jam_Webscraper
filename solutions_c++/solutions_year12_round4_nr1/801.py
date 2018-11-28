#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int T, N, D;
long long d[10000], l[10000];
long long maxDs[10000], ress[10000];

long long dfs(int from, long long maxGo) {

  long long maxD = d[from] + maxGo;
  if (maxDs[from] > maxD)
    return ress[from];
  
  if (maxD >= D) return maxD;
  
  long long res = maxD;
  
  for (int i = from+1; i < N && d[i] <= maxD; i++)
    res = max(res, dfs(i, min(d[i] - d[from], l[i])));
  
  maxDs[from] = maxD;
  ress[from] = res;
  
  return res;

}

int main() {

  cin >> T;
  for (int CASE = 1; CASE <= T; CASE++) {
    bool res = true;
    cin >> N;
    for (int i = 0; i < N; i++) {
      cin >> d[i] >> l[i];
      maxDs[i] = 0;
    }
    cin >> D;
    
    res = dfs(0, d[0]) >= D;
    
    printf("Case #%d: %s\n", CASE, res ? "YES" : "NO");
  }

}
