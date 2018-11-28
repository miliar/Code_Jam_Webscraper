#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

typedef signed   long long i64;
typedef unsigned long long u64;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define setall(x, val) memset((x), (val), sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define For(i, st, en) for(iint i=(st); i<=(en); i++)
#define Ford(i, st, en) for(iint i=(st); i>=(en); i--)
#define forn(i, n) for(int i=0; i<(n); i++)
#define fors(i, n, s) for(int i=s; i<(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)
#define ind(i, j, cols) (i * cols + j)

char mat[101][101];
double wp[101], owp[101], oowp[101], rpi[101];
int n;

double calcWP(int i) {
  int won=0, lost=0;
  forn(j, n)
    if (mat[i][j] == '1') won++;
    else if (mat[i][j] == '0') lost++;
  return won + lost == 0 ? 0.0 : (double)won / (double) (won+lost);
}

double calcWP1(int i, int j) {
  int won=0, lost=0;
  forn(k, n) if (k != i && k != j) {
    if (mat[i][k] == '1') won++;
    else if (mat[i][k] == '0') lost++;
  }
  return (won + lost == 0) ? 0.0 : (double)won / (double) (won+lost);
}

double calcOWP(int i) {
  double sum;
  int tot = 0;
  forn(j, n) {
    if (i != j && mat[i][j] != '.') {
      sum += calcWP1(j, i);
      tot++;
    }
  }
  return (tot == 0) ? 0.0 : sum / tot;
}

double calcOOWP(int i) {
  double sum;
  int tot = 0;
  forn(j, n) if (i != j && mat[i][j] != '.'){
    sum += owp[j];
    tot++;
  }
  return (tot == 0) ? 0.0 : sum / tot;
}


void calc() {
  int t, res, d;
  scanf("%d\n", &t);
  forn(tt, t) {
    scanf("%d", &n);
    forn(i, n) {
      string s;
      cin >> s;
      forn(j, n) mat[i][j] = s[j];
    }
    forn(i, n) {
      wp[i] = calcWP(i);
      printf("", i + 'A', wp[i]);
    }
    forn(i, n) {
      owp[i] = calcOWP(i);
      printf("", i + 'A', owp[i]);
    }
    forn(i, n) {
      oowp[i] = calcOOWP(i);
      printf("", i + 'A', oowp[i]);
    }
    printf("Case #%d:\n", tt+1);
    forn(i, n) {
      double rpi = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
      printf("%.9lf\n", rpi);
    }
  }
}

int main() {
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);

  calc();

  return 0;
}
