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

struct Center {
  int x;
  int y;
  int weight;
  void clear() {
    x = 0;
    y = 0;
    weight = 0;
  }
  void addPoint(int px, int py, int pw) {
    x += px * pw;
    y += py * pw;
    weight += pw;
  }
};

ostream& operator<<(ostream& os, const Center& c) {
  os << "xs=" << c.x << " ys=" << c.y << " w=" << c.weight << " x=" << (double) c.x / c.weight << " y=" << (double) c.y / c.weight;
  return os;
}

const int MAX = 500;

int grid[MAX][MAX];
Center colCenter[MAX];
Center sqCenter;
int width, height;

void initColCenter(int k) {
  for (int x = 0; x < width; x++) {
    Center& c = colCenter[x];
    c.clear();
    for (int y = 0; y < k; y++) {
      c.addPoint(x, y, grid[x][y]);
    }
  }
}

void shiftColCenter(int oldY, int k) {
  int newY = oldY + k;
  for (int x = 0; x < width; x++) {
    Center& c = colCenter[x];
    c.addPoint(x, oldY, -grid[x][oldY]);
    c.addPoint(x, newY, grid[x][newY]);
  }
}

void initSqCenter(int y, int k) {
  sqCenter.clear();
  for (int x = 0; x < k; x++) {
    Center& c = colCenter[x];
    sqCenter.x += c.x;
    sqCenter.y += c.y;
    sqCenter.weight += c.weight;
  }
}

void shiftSqCenter(int oldX, int y, int k) {
  Center& c1 = colCenter[oldX];
  Center& c2 = colCenter[oldX + k];
  sqCenter.x += c2.x - c1.x;
  sqCenter.y += c2.y - c1.y;
  sqCenter.weight += c2.weight - c1.weight;
}

bool testX(int x, int y, int k) {
  Center c = sqCenter;
  c.addPoint(x, y, -grid[x][y]);
  c.addPoint(x + k - 1, y, -grid[x + k - 1][y]);
  c.addPoint(x, y + k - 1, -grid[x][y + k - 1]);
  c.addPoint(x + k - 1, y + k - 1, -grid[x + k - 1][y + k - 1]);
  //cout << "x=" << x << " y=" << y << " k=" << k << " cx=" << (double) c.x / c.weight << " cy=" << (double) c.y / c.weight << endl;
  if ((c.x * 2) % c.weight == 0
      && (c.x * 2) / c.weight == (x * 2) + k - 1
      && (c.y * 2) % c.weight == 0
      && (c.y * 2) / c.weight == (y * 2) + k - 1) {
    return true;
  }
  return false;
}

bool testY(int y, int k) {
  initSqCenter(y, k);
  for (int x = 0; x <= width - k; x++) {
    if (testX(x, y, k)) return true;
    if (x < width - k) shiftSqCenter(x, y, k);
  }
  return false;
}

bool testK(int k) {
  initColCenter(k);

  for (int y = 0; y <= height - k; y++) {
    /*for (int x = 0; x < width; x++) {
      cout << "colX=" << x << " y=" << y << " center:" << colCenter[x] << endl;
    }*/
    if (testY(y, k)) return true;
    if (y < height - k) shiftColCenter(y, k);
  }
  return false;
}

int main() {
  int nCases;
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    cerr << "iCase=" << iCase << endl;
    char digit;
    
    scanf("%d%d%*d", &height, &width);
    
    for (int y = 0; y < height; y++) {
      for (int x = 0; x < width; x++) {
        scanf(" %c", &digit);
        grid[x][y] = (digit - '0') + 1; //FIXME TEST
      }
    }
    
    int optK = -1;
    for (int k = min(width, height); k >= 3; k--) {
      if (testK(k)) {
        optK = k;
        break;
      }
    }
    if (optK != -1)
      printf("Case #%i: %i\n", iCase, optK);
    else
      printf("Case #%i: IMPOSSIBLE\n", iCase);
  }
  return 0;
}
