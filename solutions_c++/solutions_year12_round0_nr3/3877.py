#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long lol;

#define sz(c) ((int) (c).size())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

int A,B;

int digits(int x) {
  int res = 0;
  while (x > 0) {
    x /= 10;
    ++res;
  }
  return res;
}

void proc( set < pair <int,int> > &rec, int x) { 
  int n = digits(x);
  int p = 1;
  for (int i = 0; i < n-1; ++i)
    p *= 10;
  int y = x;
  for (int i = 0; i < n-1; ++i) {
    int k = y % 10;
    y = y/10 + k*p;
    if (k != 0 && x < y && y >= A && y <= B) {
      rec.insert( mp(x,y) );
    }
  }
}

void solve(int testcase)
{
  printf("Case #%d: ", testcase);
  fprintf(stderr,"Case #%d: ", testcase);
  cin >> A >> B;
  set < pair <int,int> > rec;
  for (int i=A; i<=B; ++i) {
    proc(rec,i);
  }
  printf("%d\n", sz (rec));
  fprintf(stderr,"%d\n", sz (rec));
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; ++i) 
    solve(i);
  return 0;
}
