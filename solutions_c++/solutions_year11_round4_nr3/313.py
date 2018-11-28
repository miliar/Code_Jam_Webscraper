/*
ID: azhai1
LANG: C++
TASK: exp_dinner
*/

#include <cstdio>
#include <algorithm>

using namespace std;

FILE *in  = fopen ("exp_dinner.in", "r");
FILE *out = fopen ("exp_dinner.out", "w");

const int P_MAX = 1000032;
bool sieve[P_MAX];
int primes[P_MAX];
int prime_counter;

int get_exp(int p, int n) {
  int result = 0;
  while (n >= p) {
    n /= p;
    result++;
  }
  return result;
}

int get_answer(int n) {
  if (n == 1) return 0;
  int answer = 1;
  for (int i = 0; i < prime_counter && n >= primes[i]; i++)
    answer += (get_exp(primes[i], n) - 1);
  return answer;
}

int main() {
  
  for (int i = 2; i < P_MAX; i++) {
    if (!sieve[i]) { // if not composite
      for (int j = 2 * i; j < P_MAX; j += i)
	sieve[j] = true;
      primes[prime_counter++] = i;
    }
  }

  int T, N;
  fscanf(in, "%d\n", &T);
  for (int i = 0; i < T; i++) {
    fscanf(in, "%d\n", &N);
    fprintf(out, "Case #%d: %d\n", i + 1, get_answer(N));
  }

  return 0;
}

