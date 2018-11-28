#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<pair<int, int> > vii;

int T, NA, NB;
vii A, B;

void load(vii& v, int n) {
  v.clear();
  for (int i = 0; i < n; i++) {
    int hh1, mm1, hh2, mm2;
    scanf("%d:%d%d:%d", &hh1, &mm1, &hh2, &mm2);
    v.push_back(make_pair(hh1 * 60 + mm1, hh2 * 60 + mm2));
  }
  sort(v.begin(), v.end());
}

void train(bool isA, int time) {
  time += T;
  vii& v = isA ? A : B;
  int pos = 0;
  while (pos < v.size() && v[pos].first < time) pos++;
  if (pos == v.size()) return;
  int end = v[pos].second; v.erase(v.begin() + pos);
  train(!isA, end);
}

int main() {
  int N; scanf("%d", &N);
  for (int n = 1; n <= N; n++) {
    scanf("%d%d%d", &T, &NA, &NB);
    load(A, NA); load(B, NB);
    
    int resA = 0, resB = 0;
    while (!(A.empty() && B.empty())) {
      bool isA = !A.empty() && (B.empty() || B[0].first > A[0].first);
      train(isA, -100);
      isA ? resA++ : resB++;
    }

    printf("Case #%d: %d %d\n", n, resA, resB);
  }

  return 0;
}