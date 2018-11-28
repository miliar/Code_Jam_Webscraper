#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int T, N;

int main() {
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d", &N);
    vector<int> candies(N);
    for (int i = 0; i < N; ++i) {
      scanf("%d", &candies[i]);
    }
    sort(candies.begin(), candies.end());

    int candies_sum = 0;
    int true_candies_sum = 0;
    for (int i = 0; i < N; ++i) {
      candies_sum ^= candies[i];
      true_candies_sum += candies[i];
    }
    if (candies_sum != 0) {
      printf("Case #%d: NO\n", t);
    } else {
      printf("Case #%d: %d\n", t, true_candies_sum - candies[0]);      
    }    
  }
}
