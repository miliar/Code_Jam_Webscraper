#include <iostream>
#include <vector>
using namespace std;

int64_t run_test(int64_t rides, int64_t size, const vector<int64_t>& groups) {
  int64_t euros = 0;
  int64_t ng = 0;

  vector<pair<int64_t, int64_t> > cache(groups.size());

  for (int64_t r = 0; r < rides; ++r) {
    if (cache[ng].first == 0) {
      int64_t ride_cost = 0;
      int64_t room = size;
      int64_t went = 0;
      for (went = 0; went < groups.size(); ++went) {
        int64_t idx = (went + ng);
        if (idx >= groups.size()) idx -= groups.size();
        if (room < groups[idx]) {
          break;
        }
        room -= groups[idx];
        ride_cost += groups[idx];
      }

      cache[ng] = make_pair(ride_cost, went);
    }

    euros += cache[ng].first;
    ng += cache[ng].second;
    if (ng >= groups.size()) ng -= groups.size();
  }

  return euros;
}


int main() {
  int64_t t = -1;
  if (!(cin >> t) || t <= 0) {
    return 1;
  }
  int64_t R, k, N;
  for (int64_t cnum = 1; cnum <= t && cin >> R >> k >> N; ++cnum) {
    vector<int64_t> groups(N);
    for (int64_t i = 0; i < N; ++i) {
      cin >> groups[i];
    }

    cout << "Case #"  << cnum << ": ";
    int64_t res = run_test(R, k, groups);
    cout << res << endl;
  }
  return 0;
}
