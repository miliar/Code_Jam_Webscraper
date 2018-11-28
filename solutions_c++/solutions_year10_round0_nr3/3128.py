#include <iostream>
#include <queue>

using namespace std;

void solve(int tc) {
  int R, k, N; cin >> R >> k >> N;
  int res = 0;
  deque<int> q;
  while(N--) {
    int g; cin >> g;
    q.push_back(g);
  }
  
  while(R--) {
    int r = 0;
    for(int i=0; i < q.size(); i++) {
      int g = q.front();
      if (r+g > k)
        break;
      r += g;
      res += g;
      q.pop_front();
      q.push_back(g);
    }
  }
  printf("Case #%d: %d\n", tc, res);
}

int main() {
	int n; cin >> n;
	for(int i=1; i<=n; i++) solve(i);
}