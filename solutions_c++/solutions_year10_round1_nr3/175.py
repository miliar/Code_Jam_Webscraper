#include<iostream>
#include<map>
#include<algorithm>
#include<cstdio>
using namespace std;

int gcd(int x, int y) {
  //cout << "before gcd\n";
  if (x < y) swap(x, y);
  while (y) {
    x %= y;
    swap(x, y);
  }
  //cout << "after gcd\n";
  return x;
}

map<int, bool> a[1000005]; // true means who get to choose at that state wins
bool solve(int x, int y) {
  if (x < y) swap(x, y);
  int g = gcd(x, y);
  if (g > 1) {
    x /= g;
    y /= g;
  }
  
  // assume x > y > 0
  map<int,bool>::iterator it = a[x].find(y);
  if (it != a[x].end()) {
    return it->second;
  }
  bool ret = false;
  for (int z = y*((x-1)/y); z >= y; z -= y) {
    bool tmp = solve(y, x-z);
    if (! tmp) { // y, x-z is losing, so i'm winning
      ret = true;
      break;
    }
  }
  a[x][y] = ret;
  return a[x][y];
}

int main() {
  int cases, a1, a2, b1, b2;
  
  cin >> cases;
  for (int q = 1; q <= cases; q++) {
    cin >> a1 >> a2 >> b1 >> b2;
    int ans = 0;
    for (int i = a1; i <= a2; i++) {
      for (int j = b1; j <= b2; j++) {
	if (solve(i, j)) {
	  ans++;
	}
      }
    }
    printf("Case #%d: %d\n", q, ans);
  }
  return 0;
}
