#include <iostream>
#include <set>

using namespace std;

long long get(int &p, int max, int g[], int N) {
  long long sum = 0;
  set<int> s;

  while (sum + g[p] <= max && s.count(p) < 1) {
    sum += g[p];
    s.insert(p);
    p = (p+1)%N;
  }
  return sum;
}

int main(void) {
  int t;
  cin >> t;

  for (int j = 0; j < t; j++) {
    int R, k, N;
    cin >> R >> k >> N;
    int g[N];
    for (int i = 0; i < N; i++)
      cin >> g[i];

    set<int> s;
    int rep = 0, lon = 0;
    long long isum = 0, msum = 0;

    while (s.count(rep) < 1) {
      s.insert(rep);
      msum += get(rep, k, g, N);
      lon++;
    }

    for (int _j = 0; _j != rep; )
      msum -= get(_j, k, g, N);

    int idx = 0;

    while (R > 0 && idx != rep) {
      isum += get(idx, k, g, N);
      lon--;
      R--;
    }

    isum += (R/lon)*msum;

    R = R%lon;
    while (R > 0) {
      isum += get(rep, k, g, N);
      R--;
    }

    cout << "Case #" << j + 1 << ": " << isum << endl;
  }
}
