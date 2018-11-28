#include <cstdio>
#include <climits>
#include <algorithm>

using namespace std;

const int MAX_SIZE = 1000;
const int GRID_MIDDLE = MAX_SIZE / 2;
bool grid[MAX_SIZE][MAX_SIZE];
int xMin, yMin, xMax, yMax;

bool simulation() {
  bool wasNotEmpty = false;
  for (int y = yMax; y >= yMin; y--) {
    for (int x = xMax; x >= xMin; x--) {
      if (grid[x][y]) {
        wasNotEmpty = true;
        if (!grid[x - 1][y] && !grid[x][y - 1])
          grid[x][y] = false;
      }
      else if (grid[x - 1][y] && grid[x][y - 1]) {
        grid[x][y] = true;
      }
    }
  }
  return wasNotEmpty;
}

void printGrid() {
  for (int y = yMin; y <= yMax; y++) {
    for (int x = xMin; x <= xMax; x++) {
      printf("%c", grid[x][y] ? 'x' : '-');
    }
    printf("\n");
  }
  printf("\n");
}

int main() {
  int nCases;
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    for (int y = 0; y < MAX_SIZE; y++) {
      for (int x = 0; x < MAX_SIZE; x++) {
        grid[x][y] = 0;
      }
    }
    int nRect;
    scanf("%d", &nRect);

    xMin = INT_MAX;
    yMin = INT_MAX;
    xMax = INT_MIN;
    yMax = INT_MIN;

    for (int i = 0; i < nRect; i++) {
      int x1, y1, x2, y2;
      scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
      x1 += GRID_MIDDLE;
      y1 += GRID_MIDDLE;
      x2 += GRID_MIDDLE;
      y2 += GRID_MIDDLE;
      xMin = min(xMin, x1);
      yMin = min(yMin, y1);
      xMax = max(xMax, x2);
      yMax = max(yMax, y2);
      for (int y = 0; y <= y2 - y1; y++) {
        for (int x = 0; x <= x2 - x1; x++) {
          grid[x + x1][y + y1] = true;
        }
      }
    }
    
    //printGrid();
    int nSteps = 0;
    
    while (simulation()) {
      //printGrid();
      nSteps++;
    }
    
    printf("Case #%i: %i\n", iCase, nSteps);
  }
  return 0;
}
