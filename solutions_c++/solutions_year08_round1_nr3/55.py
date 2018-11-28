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

ll Pow(int b, int e, int m) {
  if (e == 0) return 1;
  ll x = Pow(b, e/2, m);
  x = (x*x)%m;
  if (e%2 == 1) x = (x*b)%m;
  return x;
}

void SolveCase() {
  ll n;
  in >> n;
  if (n == 1) {
    out << "005" << endl;
    return;
  } else if (n == 2) {
    out << "027" << endl;
    return;
  }
  n %= 125;
  ll k1 = n*(n-1)/2;
  ll k2 = n*(n-1)*(n-2)*(n-3)/24;
  k1 %= 125;
  k2 %= 125;
  ll m125 = Pow(3, n, 125) + k1 * Pow(3, n-2, 125) * 5 + k2 * Pow(3, n-4, 125) * 25;
  m125 *= 2;
  m125 %= 125;
  ll x = 0;
  for (int i = 0; i < 8; i++) {
    x = 125*i + m125;
    if (x % 8 == 0)
      break;
  }
  x = (x+999)%1000;
  char buffer[4];
  sprintf(buffer, "%03i", int(x)); 
  out << buffer << endl;
}
