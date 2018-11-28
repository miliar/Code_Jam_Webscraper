#include <cstdio>

using namespace std;

namespace {

struct input {
  char array[4][5];
};

const char kUniversal = 'T';

bool check(const input &input, int begin_x, int begin_y, int delta_x,
           int delta_y, char player) {
  while (begin_x < 4 && begin_y < 4) {
    if (input.array[begin_x][begin_y] != player &&
        input.array[begin_x][begin_y] != kUniversal) {
      return false;
    }
    begin_x += delta_x;
    begin_y += delta_y;
  }
  return true;
}

bool has_won(const input &this_input, char player) {
  for (int i = 0; i < 4; i++) {
    if (check(this_input, 0, i, 1, 0, player)) return true;
    if (check(this_input, i, 0, 0, 1, player)) return true;
  }
  if (check(this_input, 0, 0, 1, 1, player)) return true;
  if (check(this_input, 0, 3, 1, -1, player)) return true;

  return false;
}

bool is_incomplete(const input &this_input) {
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      if (this_input.array[i][j] == '.') return true;
    }
  }
  return false;
}

void process_one(int case_num) {
  input this_input;
  for (int i = 0; i < 4; i++) {
    scanf("%s", &this_input.array[i][0]);
  }

  printf("Case #%d: ", case_num);
  if (has_won(this_input, 'O')) {
    printf("O won\n");
  } else if (has_won(this_input, 'X')) {
    printf("X won\n");
  } else if (is_incomplete(this_input)) {
    printf("Game has not completed\n");
  } else {
    printf("Draw\n");
  }
}

}

int main() {
  int case_count = 0;
  scanf("%d", &case_count);

  for (int i = 0; i < case_count; i++) {
    process_one(i + 1);
  }
  return 0;
}
