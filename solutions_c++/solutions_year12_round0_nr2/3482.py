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
  int N, S, p, V, Vavg;
  scanf("%d %d %d", &N, &S, &p);

  int r = 0;

  REP(i, N) {
    scanf("%d", &V);

    Vavg = V / 3;
    V -= Vavg * 3;

    if (Vavg >= p || Vavg == p - 1 && V) {
      r++;
    } else if (((Vavg == p - 2 && V == 2) || (Vavg && Vavg == p - 1)) && S) {
      r++;
      S--;
    }
  }

  printf("Case #%d: %d\n", numberOfTestCase, r);
}

int main(int argc, char** argv) {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  int TC;
  scanf("%d\n", &TC);
  REP(i, TC) do_case(i + 1);
  return 0;
}

