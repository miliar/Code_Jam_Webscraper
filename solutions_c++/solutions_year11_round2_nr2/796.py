#include <iostream>
#include <vector>
using namespace std;

const int MAX_OFFSET = 300000;
int D;

vector<int> cache;
vector<bool> is_computed;

typedef vector<int> Vendors;
Vendors v;

int index(int N, int L) {
  return N + (MAX_OFFSET + L) * v.size();
}

void reset_cache() {
  cache.clear();
  cache.resize(2 * MAX_OFFSET * v.size());
  is_computed.clear();
  is_computed.resize(2 * MAX_OFFSET * v.size());
}

int time(int, int);

int compute_time(int N, int L) {
  //  cout << "compute_time( " << N << ", " << L << ")\n";
  if(N >= v.size())
    return 0;

  if(N == v.size() - 1) {
    return abs(L);
  }

  int new_L = L + D - (v[N+1] - v[N]);
  if(new_L >= 0)
    return max(time(N+1, new_L), abs(L));

  int best_time = time(N+1, 0);
  for(int l=-1;l>=max(new_L, int(-D * v.size()));l--) {
    int t = time(N+1, l);
    if(t < best_time)
      best_time = t;
  }

  return max(best_time, abs(L));
}

int time(int N, int L) {
  const int i = index(N, L);
  if(!is_computed[i]) {
    cache[i] = compute_time(N, L);
    is_computed[i] = true;
  }

  //  cout << "time(" << N << ", " << L << ") = " << cache[i] << "\n";
  return cache[i];
}

int main()
{
  int T;
  cin >> T;
  for(int c=1;c<=T;c++) {
    int C;
    cin >> C;
    cin >> D;
    D *= 2;
    v.clear();
    for(int i=0;i<C;i++) {
      int P;
      int V;
      cin >> P >> V;
      for(int j=0;j<V;j++)
	v.push_back(2 * P);
    }

    reset_cache();
    int best_time = time(0, 0);
    for(int L=1;L<v.size() * D;L++) {
      int t = time(0, -L);
      if(t < best_time)
	best_time = t;
    }

    cout << "Case #" << c << ": " << .5 * best_time << "\n";
  }
  return 0;
}
