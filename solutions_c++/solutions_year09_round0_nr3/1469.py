#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
using namespace std;

int main() {
  string sx, sy;
  int lex, ley, y, x, cases, q, ans, a[505][20];
  sx = "welcome to code jam";
  lex = sx.length();
  cin >> cases;
  getline(cin, sy);
  for (q = 1; q <= cases; q++) {
    getline(cin, sy);
    ley = sy.length();
    //cout << sy << endl;
    if (ley < lex) ans = 0;
    else {
      memset(a, 0, sizeof(a));
      if (sx[0] == sy[0]) a[0][0] = 1;
      for (y = 1; y < ley; y++) {
	a[y][0] = a[y-1][0];
	if (sy[y] == sx[0]) a[y][0]++;
	a[y][x] %= 10000;
      }
      for (y = 1; y < ley; y++) {
	for (x = 1; x < lex; x++) {
	  a[y][x] = a[y-1][x];
	  if (sy[y] == sx[x]) a[y][x] += a[y-1][x-1];
	  a[y][x] %= 10000;
	}
      }
      ans = a[ley-1][lex-1];
    }
    /*
    for (y = 0; y < ley; y++) {
      for (x = 0; x < lex; x++) {
	printf("%3d", a[y][x]);
      }
      cout << endl;
      }*/
    printf("Case #%d: %04d\n", q, ans);
    //return 0;
  }
  return 0;
}
