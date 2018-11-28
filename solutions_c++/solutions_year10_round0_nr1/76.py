#include<iostream>
#include<cstdio>
using namespace std;
#define rep(i,s,e) for(int i=(s),___e=(e);i<___e;++i)
#define REP(i,n) rep(i,0,n)
typedef unsigned int ui;
typedef long long ll;
int in() {
  int x = 0, c;
  while ((ui)((c = getchar()) - '0') >= 10) { }
  do { x = 10 * x + (c - '0'); } while ((ui)((c = getchar()) - '0') < 10);
  return x;
}

int main()
{
  int T = in();
  REP(turn, T) {
    int N = in(), K = in();
    int M = K % (1 << N);
    printf("Case #%d: %s\n", turn + 1, (M == (1 << N) - 1) ? "ON" : "OFF");
  }
  return 0;
}

