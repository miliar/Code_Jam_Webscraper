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

char m[27] = "yhesocvxduiglbkrztnwjpfmaq";

void do_case(int numberOfTestCase) {
  char c, s[101];
  int len = 0;
  while (scanf("%c", &c) != EOF) {
    if (c == '\n') break;
    s[len++] = c;
  }
  s[len] = 0;
  char r[101] = "";

  REP(i, len) {
    if (s[i] - ' ') {
      r[i] = m[s[i] - 'a'];
    } else r[i] = s[i];
  }
  r[len] = 0;

  printf("Case #%d: %s\n", numberOfTestCase, r);
}

int main(int argc, char** argv) {
  freopen("A-small-attempt1.in", "r", stdin);
  freopen("A-small.out", "w", stdout);
  int TC;
  scanf("%d\n", &TC);
  REP(i, TC) do_case(i + 1);
  return 0;
}

