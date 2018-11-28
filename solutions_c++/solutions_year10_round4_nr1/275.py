#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAX_SIZE = 1000;
const int x0 = MAX_SIZE / 2, y0 = MAX_SIZE / 2;
int m[MAX_SIZE][MAX_SIZE];
int k;
int xMin, xMax, yMin, yMax;

void printM() {
  for (int y = y0 - k; y <= y0 + k; y++) {
    for (int x = x0 - k; x <= x0 + k; x++) {
      if (m[x][y] == -1)
        printf("_");
      else
        printf("%d", m[x][y]);
    }
    printf("\n");
  }
}

bool testSim(int xC, int yC, int& dMax) {
  dMax = 0;
  for (int y = yMin; y <= yMax; y++) {
    int x0 = xMin + ((y - y0) & 1);
    for (int x = x0; x <= xMax; x += 2) {
      int d = m[x][y];
      if (d != -1) {
        dMax = max(dMax, abs(xC - x) + abs(yC - y) + 1);
        int xSim = xC + xC - x;
        if (xSim >= xMin && xSim <= xMax && m[xSim][y] != -1 && m[xSim][y] != d) return false;
        int ySim = yC + yC - y;
        if (ySim >= yMin && ySim <= yMax && m[x][ySim] != -1 && m[x][ySim] != d) return false;
      }
    }
  }
  return true;
}

int main() {
  int nCases;
  scanf("%d", &nCases);
  for (int iCase = 0; iCase < nCases; iCase++) {
    scanf("%d", &k);
    
    yMin = y0 - k + 1;
    yMax = y0 + k - 1;
    xMin = x0 - k + 1;
    xMax = x0 + k - 1;
    for (int x = xMin; x <= xMax; x++) {
      fill(m[x] + yMin, m[x] + yMax + 1, -1);
    }

    for (int y = 0; y < 2 * k - 1; y++) {
      int dx = (y < k) ? (y + 1) : (2 * k - 1 - y);
      int xBase = (y < k) ? (x0 - y) : (x0 - (2 * k - 2 - y));
      for (int x = 0; x < dx; x++) {
        int d;
        scanf("%i", &d);
        m[xBase + 2 * x][y0 - k + 1 + y] = d;
      }
    }

    int minDMax = 10000000;

    for (int y = yMin; y <= yMax; y++) {
      for (int x = xMin; x <= xMax; x++) {
        int dMax = 0;
        if (testSim(x, y, dMax)) {
          //cout << "sim(" << x - x0 << "," << y - y0 << ")=" << dMax << endl;
          minDMax = min(minDMax, dMax);
        }
      }
    }
    
    //cout << "k=" << minDMax << " minDMax=" << minDMax << endl;
    cout << "Case #" << iCase + 1 << ": " << minDMax * minDMax - k * k << endl;

    //printM();
  }
  return 0;
}
