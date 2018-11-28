//this is the default for Google code jam only
#include <string>
#include <vector>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

#define pii pair<int, int>

using namespace std;

//ifstream fi("A-small-attempt0.in");
ifstream fi("A-large.in");
//ifstream fi("A-small-practice.in");
//ifstream fi("sample.in");
ofstream fo("sample.out");

int test;

int n;
long long d[10000], l[10000];
long long f[10000];
long long D;
bool res;

void input();
void solve();
void output();

int main() {
  int ntest;
  fi >> ntest;
  for (test = 1; test <= ntest; test ++) {
    input();
    solve();
    output();
  }
  fi.close();
  fo.close();
  return 0;
}

void input() {
  //start code here
  fi >> n;
  for (int i = 0; i < n; i ++) fi >> d[i] >> l[i];
  fi >> D;
}

void solve() {
  f[0] = d[0];
  for (int i = 1; i < n; i ++) {
    f[i] = 0;
    for (int j = i - 1; j >= 0; j --)
      if (d[j] + f[j] >= d[i]) {
	f[i] = max(f[i], min(l[i], d[i] - d[j]));
      }
  }
  res = false;
  for (int i = 0; i < n; i ++)
    if (d[i] + f[i] >= D) {
      res = true;
      return;
    }
}

void output() {
  if (res)
    fo << "Case #" << test << ": YES" << endl;
  else 
    fo << "Case #" << test << ": NO" << endl;
}
