#include <algorithm>
#include <functional>

#include <cassert>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

typedef pair< int, int > point;
#define X first
#define T second

vector<point> A, B;

int main( void )
{
  int T; scanf("%d ", &T);

  for (int counter = 0; counter < T; ++counter) {
    printf("Case #%d: ", counter + 1);

    A.clear();
    B.clear();
    int n; scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      char c; int x; scanf(" %c %d", &c, &x); --x;
      if (c == 'B') {
        A.push_back(point(x, i));
      } else if(c == 'O') {
        B.push_back(point(x, i));
      } else {
        assert(false);
      }
    }

    int pozA = 0, oA = 0;
    int pozB = 0, oB = 0;

    int red = 0;
    A.push_back(point(100, n));
    B.push_back(point(100, n));

    int step = 0;
    int nov_red = -1;

    for (step = 0; red != n; ++step, red = nov_red) {
      nov_red = red;

      // prvi
      if (A[oA].X == pozA && A[oA].T == red) {
        nov_red = red + 1;
        ++oA;
      } else if (A[oA].X == pozA) {
        ;
      } else if (A[oA].X <  pozA) {
        pozA--;
      } else if (A[oA].X >  pozA) {
        pozA++;
      }

      // drugi
      if (B[oB].X == pozB && B[oB].T == red) {
        nov_red = red + 1;
        ++oB;
      } else if (B[oB].X == pozB) {
        ;
      } else if (B[oB].X <  pozB) {
        pozB--;
      } else if (B[oB].X >  pozB) {
        pozB++;
      }
    }

    printf("%d\n", step);
  }


  return (0-0);
}
