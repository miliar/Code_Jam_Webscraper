#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <sstream>

namespace {
size_t CalcTime() {
  size_t N = 0;
  std::cin >> N;

  size_t o_pos = 1;
  size_t b_pos = 1;
  
  char amari_char = 'a';
  size_t amari_dist = 0;

  size_t result = 0;
  for (size_t n = 0; n < N; ++n) {
    char button;
    size_t pos = 0;
    std::cin >> button >> pos;

    if (button == amari_char) {
      size_t dist = 1;
      if (button == 'O') {
        dist += abs(o_pos - pos);
        o_pos = pos;
      } else {
        dist += abs(b_pos - pos);
        b_pos = pos;
      }
      amari_dist += dist;
      result += dist;
    } else {
      size_t dist = 1;
      if (button == 'O') {
        int tmp_dist = abs(o_pos - pos) - amari_dist;
        if (tmp_dist > 0)
          dist += tmp_dist;

        o_pos = pos;
      } else {
        int tmp_dist = abs(b_pos - pos) - amari_dist;
        if (tmp_dist > 0)
          dist += tmp_dist;

        b_pos = pos;
      }

      amari_char = button;
      amari_dist = dist;
      result += dist;
    }
  }

  return result;
}

void PrintOutput(size_t iter, size_t result) {
  printf("Case #%d: %d\n", iter+1, result);
}

} //namespace

int main() {
  size_t T = 0;
  std::cin >> T;

  for (size_t iter = 0; iter < T; ++iter) {
    size_t result = CalcTime();
    PrintOutput(iter, result);
  }
}
