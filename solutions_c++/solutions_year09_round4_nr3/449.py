#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int num_lines;
int num_points;
int data[100][25];
bool intersects[100][100];

int colors[100];
int number_of_colors;
int best_number = 10000000;

bool check(int a, int b) {
  for (int i = 0; i < num_points - 1; i++) {
    if (data[a][i] == data[b][i]) return true;
    if (data[a][i] > data[b][i] && data[a][i + 1] < data[b][i + 1])
      return true;
    if (data[a][i] < data[b][i] && data[a][i + 1] > data[b][i + 1])
      return true;
  }
  if (data[a][num_points - 1] == data[b][num_points - 1]) return true;
  return false;
}

void do_greedy() {
  int colors_used = 1;
  colors[0] = 0;
  for (int i = 1; i < num_lines; i++) {
    int can_use[100];
    memset(can_use, -1, sizeof(can_use));
    for (int j = i - 1; j >= 0; j--) {
      if (intersects[i][j])
        can_use[colors[j]] = 0;
    }
    bool found = false;
    for (int j = 0; j < colors_used; j++) {
      if (can_use[j]) {
        found = true;
        colors[i] = j;
        break;
      }
    }
    if (!found) {
      colors[i] = colors_used;
      colors_used++;
    }
  }
  best_number = colors_used;
}

void recurse(int k) {
  if (number_of_colors >= best_number) return;
  if (k == num_lines) {
    if (best_number > number_of_colors)
      best_number = number_of_colors;
    return;
  }
  for (int i = 0; i < number_of_colors + 1; i++) {
    colors[k] = i;
    bool valid = true;
    for (int j = 0; j < k; j++) {
      if (j == k) continue;
      if (intersects[j][k] && colors[k] == colors[j]) {
        valid = false;
        break;
      }
    }
    if (!valid) continue;
    if (i == number_of_colors) {
      number_of_colors++;
      recurse(k + 1);
      number_of_colors--;
    }
    else
      recurse(k + 1);
  }
}

int main(void) {
  int nC, cC;

  scanf("%d", &nC);
  for (cC = 0; cC < nC; cC++) {
    scanf("%d%d", &num_lines, &num_points);
    for (int i = 0; i < num_lines; i++) {
      for (int j = 0; j < num_points; j++) {
        scanf("%d", &data[i][j]);
      }
      for (int j = i - 1; j >= 0; j--) {
        intersects[i][j] = intersects[j][i] = check(i, j);
      }
    }

    memset(colors, -1, sizeof(colors));
    do_greedy();
    number_of_colors = 1;
    colors[0] = 0;
    recurse(1);
    printf("Case #%d: %d\n", cC + 1, best_number);
  }
  return 0;
}
