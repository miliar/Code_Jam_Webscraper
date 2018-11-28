// Problem C. Recycled Numbers.cpp : Defines the entry point for the console application.
//

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;

#define forab(i,a,b) for(int i = (a); i <= (int)(b); i++)
#define forn(i,n) for(int i = 0; i < (int)(n); i++)
// need declare it for vc, vc can not use <typeof> keyword
#define foreach(it,c) for(it = c.begin(); it != c.end(); ++it)

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define zero(a) memset(a, 0, sizeof(a))

#define pb push_back
#define mp make_pair

int t;
vector<int> vec;
vector<int> vec2;

void MakeVec(int x, vector<int>& v) {
  v.clear();
  while (x > 0) {
    v.push_back(x % 10);
    x /= 10;
  }
}

int MakeNumber(const vector<int>& v) {
  int y = 0;
  for (int i = v.size() - 1; i >= 0; i--) {
    y *= 10;
    y += v[i];
  }
  return y;
}

void GenerateNext(int offset) {
  vec2.clear();
  int n = vec.size();
  vec2.resize(n, 0);
  int j = offset - 1;
  for (int i = n -1; i >= n - offset; i--) {
    vec2[j] = vec[i];
    j--;
  }
  for (int i = n - offset - 1; i >= 0; i--) {
    vec2[i + offset] = vec[i];
  }
}

void Print(vector<int> v) {
  for (int i = v.size() - 1; i >= 0; i--) {
    cout << v[i];
  }
  cout << endl;
}

int RecycledNumbers(int x, int a, int b) {
  MakeVec(x, vec);
  int num = 0;
  for (int i = 1; i < vec.size(); i++) {
    GenerateNext(i);
    if (vec2[vec2.size() - 1] == 0)
      continue;
    int y = MakeNumber(vec2);
    if (y < x && y >= a && y <= b) {
      num++;
    }
  }
  return num;
}

int Solve(int a, int b) {
  int res = 0;
  for (int x = b; x >= a; x--) {
    res += RecycledNumbers(x, a, b);
  }
  return res;
}

int main() {
  //freopen("1.in", "r", stdin);
  //freopen("1.out", "w", stdout);

  freopen("C-small-attempt0.in", "r", stdin);
  freopen("C-small-attempt0.out", "w", stdout);

  //freopen("X-large.in", "r", stdin);
  //freopen("X-large.out", "w", stdout);

  cin >> t;
  for (int cc = 1; cc <= t; cc++) {
    int a, b;
    cin >> a >> b;
    cout << "Case #" << cc << ": " << Solve(a, b) << endl;
  }
  return 0;
}
