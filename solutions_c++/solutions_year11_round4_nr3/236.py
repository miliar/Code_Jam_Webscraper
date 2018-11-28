/******************************************************************************

 @File Name : {PROJECT_DIR}/templ.cc

 @Creation Date : 07-05-2011

 @Last Modified : Fri 24 Jun 2011 10:47:00 PM CST

 @Created By: Zhai Yan

 @Purpose :
        template for gcj

*******************************************************************************/


#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>

using namespace std;

#define MAX_P 1000001
static bool primes[MAX_P];
static void get_prime()
{
  int i = 2, j;
  primes[0] = false;
  primes[1] = false;
  primes[2] = true;
  fill(primes, primes + MAX_P, true);
  for (i = 2; i < MAX_P; i++) if (primes[i]) {
    j = i + i;
    while (j < MAX_P) {
      primes[j] = false;
      j += i;
    }
  }
}

static long long compute_spread(long long n)
{
  long long result = 0;
  int i;
  long long half = (long long) sqrt(n);
  for (i = 2; i <= half; i++) if (primes[i]) {
  //  fprintf(stderr, "%d\n",i);
    int total = 0;
    long long temp = n;
    while (temp) {
      temp /= i;
      total++;
    }
    result += total - 1;
    //fprintf(stderr, "%lld %d %d\n", n, i, total);
  }
  result++; /* for 1 */
  for (i = 2; i <= half; i++) if (primes[i]) {
    result--;
  }
  return result;
}



static void solve(int t)
{
  long long n;
  scanf("%lld", &n);
  if (n == 1) printf("0");
  else
    printf("%lld", compute_spread(n));
}


int main()
{
  int T;
  get_prime();
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    printf("Case #%d: ", i + 1);
    solve(i + 1);
    printf("\n", i + 1);
  }
  return 0;
}





