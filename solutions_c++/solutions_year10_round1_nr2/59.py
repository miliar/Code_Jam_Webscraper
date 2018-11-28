#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX_VALUE 9999999

void merge(vector<int>& g2, int k, int v) {
  if(v < g2[k]) {
    g2[k] =v;
  }
}

int foo() {
  int D, I, M, N;
  int a[100];

  cin >> D >> I >> M >> N;
  for(int i = 0; i < N; ++i) {
    cin >> a[i];
  }

  vector<int> g(300, MAX_VALUE);
  vector<int> g2(300, MAX_VALUE);

  g[256] = 0;
  for(int i = 0; i < N; ++i) {
    int x0 = a[i];
    for(int j = 0; j < 257; ++j) {
      if(g[j] == MAX_VALUE) continue;
      int k = j;
      int v0 = g[j];
      merge(g2, k, v0+D);
      for(int x = 0; x < 256; ++x) {
        int v = v0 + abs(x-x0);
        if(k == 256) {
          merge(g2, x, v);
        } else if(abs(k-x) <= M) {
          merge(g2, x, v);
        } else if(M != 0) {
          merge(g2, x, v+(abs(k-x)-1)/M*I);
        }
      }
    }
    g.swap(g2);
    vector<int> g3(300, MAX_VALUE);
    g2.swap(g3);
      
  }
  return *min_element(g.begin(), g.end());
  
}

int main() {
  int n;
  cin >> n;
  for(int i = 0; i < n; ++i) {
    int res = foo();
    cout << "Case #" << (i+1) << ": " << res << endl;
  }

}
