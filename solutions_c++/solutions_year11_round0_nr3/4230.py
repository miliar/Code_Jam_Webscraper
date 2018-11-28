#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<int> candy;

int main()
{
  int T;
  scanf("%d ", &T);
  
  for (int i = 0; i < T; i++) {
    scanf("%d ", &N);
    candy.clear();
    for (int j = 0; j < N; j++) {
      int x;
      scanf("%d ", &x);
      candy.push_back(x);
    }

    printf("Case #%d: ", i + 1);
    int a = 0, sum = 0;
    for (int i = 0; i < N; i++) {
      a ^= candy[i];
      sum += candy[i];
    }
    if (a != 0) {
      printf("NO\n");
    } else {
      printf("%d\n", sum - *min_element(candy.begin(), candy.end()));
    }
  }
}
