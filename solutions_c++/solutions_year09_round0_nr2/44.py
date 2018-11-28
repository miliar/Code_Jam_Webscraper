#include <cstdio>
#include <cstring>

int alts[102][102];
int basins_found;
int NORTH = 0;
int WEST = 1;
int EAST = 2;
int SOUTH = 3;
int dirs[4][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };

int parent[100 * 100 + 1];

int chars_used = 0;
char char_map[100 * 100 + 1];

// find a's ultimate sink. if it returns -1, a is a sink.
int get_parent(int a) {
  int sink = a;
  while (parent[sink] != -1)
    sink = parent[sink];
  // Now we know that temp is the final sink so far for these nodes.
  while (parent[a] != -1) {
    int next = parent[a];
    parent[a] = sink;
    a = next;
  }
  return sink;
}

// make a the parent of b. in other words, b flows directly into a.
void make_parent(int a, int b) {
  int parent_a = get_parent(a);
  parent[b] = parent_a;
}

int main(void) {
  int cC, nC;
  int height, width;

  scanf("%d", &nC);
  for (cC = 0; cC < nC; cC++) {
    memset(parent, -1, sizeof(parent));
    scanf("%d%d", &height, &width);
    for (int i = 0; i <= width + 1; i++) {
      alts[0][i] = alts[height + 1][i] = 100000;
    }
    for (int i = 0; i <= height + 1; i++) {
      alts[i][0] = alts[i][width + 1] = 100000;
    }
    for (int i = 1; i <= height; i++) {
      for (int j = 1; j <= width; j++) {
        scanf("%d", &alts[i][j]);
      }
    }
    basins_found = 0;
    for (int i = 1; i <= height; i++) {
      for (int j = 1; j <= width; j++) {
        int index = (i - 1) * width + j;
        int lowest = alts[i][j];
        int lowest_dir = -1;
        for (int dir = 0; dir < 4; dir++) {
          if (alts[i + dirs[dir][0]][j + dirs[dir][1]] < lowest) {
            lowest = alts[i + dirs[dir][0]][j + dirs[dir][1]];
            lowest_dir = dir;
          }
        }
        // If I am a sink...
        if (lowest_dir == -1)
          continue;
        make_parent((i + dirs[lowest_dir][0] - 1) * width +
                     j + dirs[lowest_dir][1], index);
      }
    }
    chars_used = 0;
    memset(char_map, ' ', sizeof(char_map));
    printf("Case #%d:\n", cC + 1);
    for (int i = 1; i <= height; i++) {
      for (int j = 1; j <= width; j++) {
        if (j != 1) printf(" ");
        int index = (i - 1) * width + j;
        int parent = get_parent(index);
        if (parent == -1) parent = index;
        if (char_map[parent] == ' ') {
          char_map[parent] = 'a' + chars_used;
          chars_used++;
        }
        printf("%c", char_map[parent]);
      }
      printf("\n");
    }
  }
  return 0;
}
