/*
ID: azhai1
LANG: C++
TASK: spin_blade
*/

#include <cstdio>
#include <algorithm>
#include <cassert>
using namespace std;

void init();

FILE *in  = fopen ("spin_blade.in", "r");
FILE *out = fopen ("spin_blade.out", "w");

const int DIM_MAX = 512;

int R, C;
int x_weights[DIM_MAX][DIM_MAX];
int y_weights[DIM_MAX][DIM_MAX];
int tot_weights[DIM_MAX][DIM_MAX];

int x_col_sums[DIM_MAX][DIM_MAX];
int y_col_sums[DIM_MAX][DIM_MAX];
int tot_col_sums[DIM_MAX][DIM_MAX];

int x_blade_weights[DIM_MAX][DIM_MAX];
int y_blade_weights[DIM_MAX][DIM_MAX];
int tot_blade_weights[DIM_MAX][DIM_MAX];

int inline get_cut_blade_weight(int source[][DIM_MAX], int blade_weights[][DIM_MAX], 
				int size, int i, int j) {
  return (blade_weights[i][j] - source[i][j] - source[i - size + 1][j - size + 1]
	  - source[i - size + 1][j] - source[i][j - size + 1]);
}

void get_col_sums(int source[][DIM_MAX], int target[][DIM_MAX], int size) {
  for (int j = 0; j < C; j++)
    target[0][j] = source[0][j];
  for (int i = 1; i < size; i++) {
    for (int j = 0; j < C; j++)
      target[i][j] = source[i][j] + target[i - 1][j];
  }
  for (int i = size; i < R; i++) {
    for (int j = 0; j < C; j++)
      target[i][j] = source[i][j] + target[i - 1][j] - source[i - size][j];
  }
}

void get_blade_weight(int source[][DIM_MAX], int col_sum[][DIM_MAX], 
		      int target[][DIM_MAX], int size) {
  for (int i = size - 1; i < R; i++) {
    target[i][size - 1] = 0;
    for (int j = 0; j < size; j++)
      target[i][size - 1] += col_sum[i][j];
    for (int j = size; j < C; j++)
      target[i][j] = col_sum[i][j] + target[i][j - 1] - col_sum[i][j - size];
  }
}

bool can_make_size(int size) {
  get_col_sums(x_weights, x_col_sums, size);
  get_col_sums(y_weights, y_col_sums, size);
  get_col_sums(tot_weights, tot_col_sums, size);

  get_blade_weight(x_weights, x_col_sums, x_blade_weights, size);
  get_blade_weight(y_weights, y_col_sums, y_blade_weights, size);
  get_blade_weight(tot_weights, tot_col_sums, tot_blade_weights, size);

  for (int i = size - 1; i < R; i++) {
    for (int j = size - 1; j < C; j++) {
      int x = get_cut_blade_weight(x_weights, x_blade_weights, size, i, j);
      int y = get_cut_blade_weight(y_weights, y_blade_weights, size, i, j);
      int tot = get_cut_blade_weight(tot_weights, tot_blade_weights, size, i, j);

      if (tot * (2 * j - (size - 1)) == 2 * x
	  && tot * (2 * i - (size - 1)) == 2 * y) {

	//	printf("made at %d, %d\n", i, j);
	return true;

      }
    }
  }

  return false;
}

void print_matrix(int m[][DIM_MAX]) {
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++)
      printf("%d ", m[i][j]);
    printf("\n");
  }
  printf("\n\n");
}

int main() {
  int T;
  fscanf(in, "%d\n", &T);

  for (int t = 0; t < T; t++) {
    printf("Working on case %d\n", t + 1);

    int answer = 2;
    init();

    for (int i = 3; i <= min(R, C); i++) {
      if (can_make_size(i)) {
	answer = i;
	//	printf("Can make size %d\n", i);
      }
    }

    if (answer == 2)
      fprintf(out, "Case #%d: IMPOSSIBLE\n", t + 1);
    else
      fprintf(out, "Case #%d: %d\n", t + 1, answer);
  }

  return 0;
}

void init() {
  int D; char c;
  fscanf(in, "%d %d %d\n", &R, &C, &D);
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      fscanf(in, "%c", &c);
      int weight = c - '4';
      x_weights[i][j] = j * weight;
      y_weights[i][j] = i * weight;
      tot_weights[i][j] = weight;
    }
    fscanf(in, "\n");
  }
}

