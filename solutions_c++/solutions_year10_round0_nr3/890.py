#include <iostream>
using namespace std;

int main(){
  int T; scanf("%d", &T);
  int x[1000];
  int y[1000];
  long long z[1000];
  int f[1000];
  long long m[1000]; 
  long long ans;
  for (int ii = 1; ii <= T; ++ii){
    int R, k, N;
    scanf("%d %d %d", &R, &k, &N);
    for (int i = 0; i < N; ++i)
      scanf("%d", &x[i]);

    long long sum = 0;
    for (int i = 0; i < N; ++i)
      sum += x[i];
    if (sum < k){
      printf("Case #%d: ", ii);
      cout << sum * R; printf("\n");
      continue;
    }

    int i = 0, total = 0, j = 0;
    while (i < N){
      if (total + x[j] <= k){
	total += x[j];
	++j; if (j == N) j = 0;
      } else {
	y[i] = j;
	z[i] = total;
	total -= x[i];
	++i;
      }
    }

    for (int i = 1; i < N; ++i)
      f[i] = -1;
    f[0] = 0;
    m[0] = 0;

    i = 0;
    while ((f[y[i]] == -1) && (f[i] < R)){
      f[y[i]] = f[i] + 1;
      m[y[i]] = m[i] + z[i];
      i = y[i];
    }
    if (f[i] == R){
      ans = m[i];
    } else {
      long long cycle_money = (m[i] + z[i]) - m[y[i]];
      int cycle_length = (f[i] + 1) - f[y[i]];
      int num_cycles_to_jump = (R - f[i]) / cycle_length;
      ans = m[i] + cycle_money * num_cycles_to_jump;
      j = f[i] + cycle_length * num_cycles_to_jump;
      while (j < R){
	ans += z[i];
	i = y[i];
	j += 1;
      }
    }
    printf("Case #%d: ", ii);
    cout << ans; printf("\n");
  }
}
