//#define debug
#define forr(x,y,z)for(int (x)=(y);(x)<(z);(x)++)
#include <string>
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int gcd(int x, int y) {
  while(x > 0) {
    x ^= y;
    y ^= x;
    x ^= y;
    x %= y;
  }

  return y;
}

void divbygcd(int& x, int& y) {
  if (x == 0) {
    y = 1;
    return;
  }
  int d = gcd(x,y);
  x /= d;
  y /= d;
}

int solve(int& a, int &b, int &c, int &d, int n) {
  if(c == 100 && a < 100) return 0;
  divbygcd(a,b);
  divbygcd(c,d);
  if(b > n) return 0;
  int k = 1, m = c;
  if(c == 0 && a > 0) return 0;
  while(c < a) {
    c += m;
    k++;
  }
  d *= k;
  if(d < b) return 0;
  return 1;
}

int main() {

  int t;
  cin >> t;
  forr(i,1,t+1) {
    int n, a, b, c, d;
    b = d = 100;
    cin >> n >> a >> c;
    if(solve(a,b,c,d,n)) {
      cout << "Case #" << i << ": Possible\n";
    } else {
      cout << "Case #" << i << ": Broken\n";
    }
  }

  return 0;
}

