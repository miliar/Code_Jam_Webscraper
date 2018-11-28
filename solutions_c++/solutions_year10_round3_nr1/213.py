#include <iostream>
#include <vector>

using namespace std;

typedef pair<int, int> ii;

int solve(int tc) {
  int n; cin >> n;
  vector<ii> v;

  
  for(int i=n; i--;) {
    int a, b;
    cin >> a >> b;
    v.push_back(ii(a,b));
  }
  
  sort(v.begin(), v.end());
  
  int res = 0;
  
  for(int i=0; i<n; i++) {
    for(int j=0; j<n; j++) {
      if (i==j) continue;
      
      res += v[i].first > v[j].first && v[i].second < v[j].second;
      res += v[i].first < v[j].first && v[i].second > v[j].second;
    }
  }
  printf("Case #%d: %d\n", tc, res/2);
  return 1;
}

int main() {
  int t; cin >> t;
  for(int i=1; solve(i)&&i<t;i++);  
}