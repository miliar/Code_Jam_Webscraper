#include <math.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <deque> 
#include <iostream>

using namespace std;

static inline int getMaxn(long long m, long long n, int c)
{
  int count = 0;
  long long tmp1 = m;
  long long tmp2 = n;
  while (tmp1 < tmp2) {
    tmp1 *= c;
    tmp2 = (tmp2 + c - 1) / c;
    count++;
  }
  return count;
}

static int solve(long long m, long long n, int c)
{
  if (m * c >= n) return 0;

  int maxn  = getMaxn(m, n, c);
  long long next  = m;
  for (int i = 0 ; i < maxn; i++)
    next *= c;
  return solve(m, next, c) + 1;
}

int main()
{
  int T;

  //calcC();
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);

  for (int i = 1; i <= T; i++) {

    printf("Case #%d: ", i);
    long long m, n;
    int c ;
    scanf("%I64d%I64d%d", &m, &n, &c);

    printf("%d", solve(m, n, c));

    printf("\n");
  }

  return 0;
}
