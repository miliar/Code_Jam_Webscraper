
#include <cassert>
#include <cmath>
#include <cstring>
#include <set>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

#define MAXP 2000000
bool prime[MAXP];

int nprimes = 0;
int primes[MAXP];

void mkprime()
{
  memset(prime, true, sizeof prime);

  prime[0] = prime[1] = false;
  for (int i = 4; i < MAXP; i += 2)
    prime[i] = false;


  primes[nprimes++] = 2;

  for (int i = 3; i < MAXP; i += 2)
    if (prime[i])
    {
      primes[nprimes++] = i;
      for (int j = 2*i; j < MAXP; j += i)
        prime[j] = false;
    }
}

int D, K;
int s[200];

void solve(int CASE)
{
  cin >> D >> K;

  int maxp = (int)pow(10, D);

  for (int i = 0; i < K; i++)
    cin >> s[i];

  if (K == 1) { printf("Case #%d: I don't know.\n", CASE); return; }

  set<int> nexts;
  for (int i = 0; i < nprimes && primes[i] <= maxp; i++)
  {
    int P = primes[i];
    for (int A = 0; A < P; A++)
      //for (int B = 0; B < P; B++)
      //{
      //  bool works = true;
      //  for (int j = 1; j < K; j++)
      //    if (s[j] != (A*s[j-1] + B) % P) { works = false; break; }

      //  if (works) { nexts.insert((A*s[K-1] + B) % P); }
      //  if (nexts.size() > 1) {
      //    printf("Case #%d: I don't know.\n", CASE);
      //    return;
      //  }
      //}
    {
      bool works = true;
      int B = (P + s[1] - (A*s[0]) % P ) % P;
      if (s[0] < P && s[1] < P)
        for (int j = 2; j < K; j++)
        {
          int B2 = (P + s[j] - (A*s[j-1]) % P ) % P;
          if (s[j] >= P || B2 != B) { /*printf("Trying A %d: failed at %d %d %d\n", A, B, B2, j);*/ works = false; break; }
        }
      else
        works = false;

      if (works) {
        //printf("%d * %d + %d %% %d = %d\n", A, s[K-1], B, P, (A*s[K-1] + B) % P);
        nexts.insert((A*s[K-1] + B) % P);
      }
    }
  }

  //printf("size: %u\n", nexts.size());
  //for (set<int>::iterator it = nexts.begin(); it != nexts.end(); it++)
  //  printf("- %d\n", *it);

  assert(nexts.size() != 0);

  if (nexts.size() != 1)
    printf("Case #%d: I don't know.\n", CASE);
  else
    printf("Case #%d: %d\n", CASE, *(nexts.begin()));
}

int main()
{
  int t;
  cin >> t;
  mkprime();
  for (int i = 0; i < t; i++) solve(i+1);
}
