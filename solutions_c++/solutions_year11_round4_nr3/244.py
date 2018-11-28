#include <stdio.h>

int primes[1000001];

void getprimes() {
  for (int i=2;i<=1000000;++i) {
    if (!primes[i]) {
      int j = 2*i;
      while (j <= 1000000) {
	primes[j] = 1;
	j += i;
      }
    }
  }
}

int isprime(int x) {
  if (x<2) return 0;
  if (x == 2) return 1;
  if (x%2==0) return 0;
  if (x<=1000000) return !primes[x];
  int p=3;
  while (p*p<=x) {
    if (x%p==0) return 0;
    p+=2;
  }
  return 1;
}

int T;
long long N;

long long solve(long long n) {
  if (n==1)
    return 0;
  long long m = 0, M = 1;
  for (long long i=2;i*i<=n;++i) {
    if (isprime(i)) {
      ++m;
      long long c = 1;
      long long ii = i;
      while (ii <= n) {
	++c;
	ii *= i;
	if (ii<0 || i<0 || n<0 || m<0 || M<0) {
	  printf("BBBBBB\n");
	}
      }
      --c;
      M += c;
    }
  }
  return M-m;
}

int main() {
  getprimes();
  scanf("%d", &T);
  for (int TT=1;TT<=T;++TT) {
    scanf("%lld", &N);
    printf("Case #%d: %lld\n", TT, solve(N));
  }
  return 0;
}
