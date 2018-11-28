/* 
 * File:   main.cpp
 * Author: mac
 *
 * Created on March 27, 2012, 1:48 AM
 */

#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
#include <iterator>

using namespace std;

#define FOR(i,a,b) for(int i=a,_b=b;i<=_b;i++)
#define REP(i,a) FOR(i,0,a-1)
#define FORD(i,a,b) for(int i=a,_b=b;i>=_b;i--)
#define REPD(i,a) FORD(i,a-1,0)
#define _m(a,b) memset(a,b,sizeof(a))

void do_case(int numberOfTestCase) {
  int A, B;
  scanf("%d %d", &A, &B);
  int r = 0;
  int n, nd, d, m, ni;

  FOR(i, A, B) {
    if (i <= 11) continue;

    n = i;
    nd = 0;
    m = 10;
    while (n > 9) {
      n /= 10;
      nd++;
      m *= 10;
    }

    n = i;
    d = 1;
    REP(j, nd) {
      d *= 10;
      m /= 10;

      ni = n / d + (n % d) * m;

      if (ni > n && ni <= B) {
        r++;
      }
    }
  }

  printf("Case #%d: %d\n", numberOfTestCase, r);
}

int main(int argc, char** argv) {
  freopen("C-small-attempt0.in", "r", stdin);
  freopen("C-small-attempt0.out", "w", stdout);
  int TC;
  scanf("%d\n", &TC);
  REP(i, TC) do_case(i + 1);
  return 0;
}

