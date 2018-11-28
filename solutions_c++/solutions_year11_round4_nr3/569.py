#include <vector>
#include <utility>
#include <iostream>

std::vector<bool> data;

std::vector<std::pair<long long, int> > primes(long long number)
{
  std::vector<std::pair<long long, int> > result;
  for (long long i = 2; i <= number; i++) {
    if (data[i]) {
      int n = number;
      int cnt = 0;
      while (n >= i) {
        cnt++;
        n /= i;
      }
  //    printf("%d %d\n", (int) i, cnt);
      result.push_back(std::make_pair(i, cnt));
    }
  }

  return result;
}

#define FOR(q,n) for(int q=0; q<n; q++)

void solve() {
  long long int n;
  std::cin >> n;
  std::vector<std::pair<long long, int> > f = primes(n);
  int c = 0;
  for (int i = 0; i < (int) f.size(); i++)
    c += f[i].second;

  if (n == 1) {
  printf("0\n");
  } else {
  printf("%d\n", c - f.size() + 1);
  }

}


int main() {
  int size = 1000000;
 data.resize(size);
 data[0] = false;
 data[1] = false;
 for (long long  i = 2; i < size; i++) {
   data[i] = true;
 }

 for (long long  i = 2; i < size; i++) if (data[i]) {
   for (long long  j = 2 * i; j < size; j += i)
     data[j] = false;
 }

  int t;
  scanf("%d", &t);
  FOR(q, t) {
    printf("Case #%d: ", q+1);
    solve();
  }

}
