#ifndef INCLUDES

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <time.h>
#include <unistd.h>
#include <utility>
#include <vector>
using namespace std;

#endif

#ifndef MACROS

#define ST first
#define ND second
#define PB push_back
#define MP make_pair
#define SZ(c) ((int)(c).size())
#define CLR(c,v) memset(c, v, sizeof(c))
#define REP(i,e) for(int i = 0; i < (signed)(e); ++i)
#define REPS(i,c) for(int i = 0; i < (int) (c).size(); ++i)
#define FORU(i,b,e) for(__typeof(b) i = (b); i != (e); ++i)
#define FORD(i,b,e) for(__typeof(b) i = (b); i != (e); --i)
#define FORC(i,c) FORU(i,c.begin(),c.end())
typedef vector<int> vi; typedef long long Int;

#endif

#ifndef TOOLS

string i2bs (unsigned long long n, long b = 64, bool zeros = true) {
  string res = "0000000000000000000000000000000000000000000000000000000000000000";
  int c = b; --b;
  while (n) {res[b] += (n&1); --b; n >>= 1;}
  if (!zeros) return res.substr(b+1,c-b-1);
  return res.substr(0,c);
}

#endif

int T;
char line[5];

int main(int argc, char *argv[]) {
  cerr.precision(15);
  cout.precision(15);

  scanf("%d\n",&T);
  REP(testcase,T) {
    int oBitMask = 0;
    int xBitMask = 0;
    int used = 0;
    REP(r,4) {
      scanf("%s\n",line);
      REP(c,4) {
        if (line[c] == 'O') {
          oBitMask |= (1 << (((4-r-1)<<2)+c));
          ++used;
        } else if (line[c] == 'X') {
          xBitMask |= (1 << (((4-r-1)<<2)+c));
          ++used;
        } else if (line[c] == 'T') {
          oBitMask |= (1 << (((4-r-1)<<2)+c));
          xBitMask |= (1 << (((4-r-1)<<2)+c));
          ++used;
        }
      }
    } scanf("\n");

    // cout << i2bs(oBitMask,16); cout << " 0x" << std::hex << oBitMask << '\n';
    // cout << i2bs(xBitMask,16); cout << " 0x" << std::hex << xBitMask << '\n';

    solution:
    printf("Case #%d: ",testcase+1);
    bool winner = false;

    // O won ?

    if (// horizontal
        ((oBitMask & 0xf000) == 0xf000) ||
        ((oBitMask & 0x0f00) == 0x0f00) ||
        ((oBitMask & 0x00f0) == 0x00f0) ||
        ((oBitMask & 0x000f) == 0x000f) ||
        // vertical
        ((oBitMask & 0x8888) == 0x8888) ||
        ((oBitMask & 0x4444) == 0x4444) ||
        ((oBitMask & 0x2222) == 0x2222) ||
        ((oBitMask & 0x1111) == 0x1111) ||
        // diagonal
        ((oBitMask & 0x8421) == 0x8421) ||
        ((oBitMask & 0x1248) == 0x1248)
    ) {
      winner = true;
      printf("O won");
    }

    // X won ?

    if (// horizontal
        ((xBitMask & 0xf000) == 0xf000) ||
        ((xBitMask & 0x0f00) == 0x0f00) ||
        ((xBitMask & 0x00f0) == 0x00f0) ||
        ((xBitMask & 0x000f) == 0x000f) ||
        // vertical
        ((xBitMask & 0x8888) == 0x8888) ||
        ((xBitMask & 0x4444) == 0x4444) ||
        ((xBitMask & 0x2222) == 0x2222) ||
        ((xBitMask & 0x1111) == 0x1111) ||
        // diagonal
        ((xBitMask & 0x8421) == 0x8421) ||
        ((xBitMask & 0x1248) == 0x1248)
    ) {
      winner = true;
      printf("X won");
    }

    if (!winner) {
      if (used == 16) {
        printf("Draw");
      } else {
        printf("Game has not completed");
      }
    }

    printf("\n");
  }

  return 0;
}