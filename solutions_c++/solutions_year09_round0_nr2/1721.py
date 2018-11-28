#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <vector>

using namespace std;


static const int max_size = 10000;
static const int max_size_with_boundary = max_size + 2;
static int altitudes[max_size_with_boundary][max_size_with_boundary];
static int x_ref[max_size][max_size];
static int y_ref[max_size][max_size];
static char basin[max_size][max_size];
static int next_letter;

void print_map(int width, int height);
void find_next(int x, int y, int& next_x, int& next_y);

int main(int argc, char** argv) {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < max_size_with_boundary; i++) {
    altitudes[0][i] = 0xffff;
    altitudes[i][0] = 0xffff;
  }
  for (int dummy = 1; dummy <= n; dummy++) {
    next_letter = 0;
    int width, height;
    scanf("%d %d", &height, &width);
    for (int i = 0; i <= height; i++) {
      altitudes[i][width+1] = 0xffff;
    }
    for (int i = 0; i <= width; i++) {
      altitudes[height+1][i] = 0xffff;
    }
    for (int i = 0; i < height; i++) {
      for (int j = 0; j < width; j++) {
        scanf("%d", &altitudes[i+1][j+1]);
      }
    }
    memset(x_ref, -1, max_size*height*sizeof(int));
    memset(y_ref, -1, max_size*height*sizeof(int));
    memset(basin, '\0', max_size*height);
    for (int i = 1; i <= height; i++) {
      for (int j = 1; j <= width; j++) {
        if (!(altitudes[i][j] <= altitudes[i-1][j] && altitudes[i][j] <= altitudes[i+1][j] &&
            altitudes[i][j] <= altitudes[i][j-1] && altitudes[i][j] <= altitudes[i][j+1])) {
          int next_x, next_y;
          find_next(i, j, next_x, next_y);
          x_ref[i-1][j-1] = next_x - 1;
          y_ref[i-1][j-1] = next_y - 1;
        }
      }
    }
    printf("Case #%d:\n", dummy);
    print_map(width, height);
  }
  return 0;
}

struct point {
  int x;
  int y;
};

static vector<point> stack;

char find_letter(int x, int y) {
  stack.clear();
  while (x_ref[x][y] != -1 && y_ref[x][y] != -1 && basin[x][y] == '\0') {
    struct point point = {x,y};
    stack.push_back(point);
    x = x_ref[point.x][point.y];
    y = y_ref[point.x][point.y];
  }
  if (basin[x][y] == '\0') {
    basin[x][y] = 'a' + next_letter;
    next_letter++;
  }
  for (unsigned int i; i < stack.size(); i++) {
    basin[stack[i].x][stack[i].y] = basin[x][y];
  }
  return basin[x][y];


}

void print_map(int width, int height) {
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {
      printf("%c", find_letter(i,j));
      if (j < width - 1) {
        putchar(' ');
      }
    }
    putchar('\n');
  }
}

#define min(a,b) (a < b ? a : b)

void find_next(int x, int y, int& next_x, int& next_y) {
  int min_adjacent = min(min(altitudes[x-1][y], altitudes[x+1][y]), min(altitudes[x][y-1], altitudes[x][y+1]));
  if (altitudes[x-1][y] == min_adjacent) {
    next_x = x-1;
    next_y = y;
  } else if (altitudes[x][y-1] == min_adjacent) {
    next_x = x;
    next_y = y-1;
  } else if (altitudes[x][y+1] == min_adjacent) {
    next_x = x;
    next_y = y+1;
  } else if (altitudes[x+1][y] == min_adjacent) {
    next_x = x+1;
    next_y = y;
  }
  assert(min_adjacent < altitudes[x][y]);
}
