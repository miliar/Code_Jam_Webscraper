#include <cstdio>
#include <vector>

long long bin[501][501];

void binom()
{
  for(int i=0; i<501; ++i) {
    bin[i][0] = bin[i][i] = 1;
    for(int j=1; j<i; ++j)
      bin[i][j] = (bin[i-1][j] + bin[i-1][j-1])%100003;
  }
}

int main()
{
  binom();
  int T;
  scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    long long n;
    scanf("%lld", &n);
    std::vector<std::vector<long long> > v(n+1, std::vector<long long>(n+1));
    for(int i=2; i<=n; ++i)
      v[i][1] = 1;
    for(int i=3; i<=n; ++i)
      for(int j=2; j<i; ++j) {
	for(int k=1; k<j; ++k) {
	  v[i][j] += v[j][k]*bin[i-j-1][j-k-1];
	  v[i][j] %= 100003;
	}
      }
    long long sum=0;
    for(int i=1; i<n; ++i)
      sum += v[n][i];
    sum %= 100003;
    printf("Case #%d: %lld\n", t, sum);
  }
  return 0;
}
