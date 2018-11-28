#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>

using namespace std;

const int MAX_N = 1005;

char grid[MAX_N][MAX_N];
int nSources[MAX_N][MAX_N];
int width, height;

struct Point {
  Point(int x = 0, int y = 0) : x(x), y(y) {}
  int x, y;
};

Point charMap[0x100][2];

int main() {
  charMap[(unsigned int) '|'][0] = Point(0, 1);
  charMap[(unsigned int) '|'][1] = Point(0, -1);
  charMap[(unsigned int) '-'][0] = Point(1, 0);
  charMap[(unsigned int) '-'][1] = Point(-1, 0);
  charMap[(unsigned int) '/'][0] = Point(1, -1);
  charMap[(unsigned int) '/'][1] = Point(-1, 1);
  charMap[(unsigned int) '\\'][0] = Point(1, 1);
  charMap[(unsigned int) '\\'][1] = Point(-1, -1);

  int nCases;
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    scanf("%d%d", &height, &width);
    for (int y = 0; y < height; y++) {
      for (int x = 0; x < width; x++) {
        scanf(" %c", &grid[x][y]);
      }
    }
    int iMax = 1 << (width * height);
    int nSolutions = 0;
    for (int i = 0; i < iMax; i++) {
      for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
          nSources[x][y] = 0;
        }
      }
      int mask = 1;
      bool isValid = true;
      for (int y = 0; y < height && isValid; y++) {
        for (int x = 0; x < width; x++) {
          int bit = (i & mask) ? 1 : 0;
          Point& p = charMap[(unsigned char) grid[x][y]][bit];
          int xx = x + p.x, yy = y + p.y;
          if (xx >= width) xx -= width;
          else if (xx < 0) xx += width;
          if (yy >= height) yy -= height;
          else if (yy < 0) yy += height;
          if ((++nSources[xx][yy]) > 1) {
            isValid = false;
            break;
          }
          mask <<= 1;
        }
      }
      nSolutions += isValid;
    }
    printf("Case #%i: %i\n", iCase, nSolutions);
  }
  return 0;
}
