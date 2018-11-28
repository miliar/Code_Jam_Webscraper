#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

typedef __int64 ll;
const double kPi = atan(1.0) * 4;

ifstream in("in.txt");
ofstream out("out.txt");
void SolveCase();

int main() {
  int ncases;
  in >> ncases;
  for (int tc = 0; tc < ncases; tc++) {
    out << "Case #" << (tc+1) << ": ";
    SolveCase();
  }
  return 0;
}

void SolveCase() {
  int n;
  in >> n;
  vector<ll> a(n), b(n);
  for (int i = 0; i < n; i++) in >> a[i];
  for (int i = 0; i < n; i++) in >> b[i];
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());
  reverse(b.begin(), b.end());
  ll x = 0;
  for (int i = 0; i < n; i++) x += a[i]*b[i];
  out << x << endl;
}
