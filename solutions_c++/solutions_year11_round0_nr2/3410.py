#include <stdio.h>

#include <iostream>
#include <list>
#include <set>
#include <algorithm>

namespace {
//{Q, W, E, R, A, S, D, F}
void init(char combine[8][8], bool opposed[8][8]) {
  for (size_t i = 0; i < 8; ++i) {
    for (size_t j = 0; j < 8; ++j) {
      combine[i][j] = ' ';
      opposed[i][j] = false;
    }
  }
}

size_t BaseToInt(const char base) {
  switch(base) {
    case 'Q':
      return 0;
    case 'W':
      return 1;
    case 'E':
      return 2;
    case 'R':
      return 3;
    case 'A':
      return 4;
    case 'S':
      return 5;
    case 'D':
      return 6;
    case 'F':
      return 7;
    default:
      break;
  }
  return 8;
}

void ProcessInput(std::list<char>& result,
                  char combine[8][8],
                  bool opposed[8][8]) {
  size_t C = 0;
  std::cin >> C;

  for (size_t c = 0; c < C; ++c) {
    char base_one, base_two, non_base;
    std::cin >> base_one >> base_two >> non_base;
    combine[BaseToInt(base_one)][BaseToInt(base_two)] = non_base;
    combine[BaseToInt(base_two)][BaseToInt(base_one)] = non_base;
  }

  size_t D = 0;
  std::cin >> D;

  for (size_t d = 0; d < D; ++d) {
    char base_one, base_two;
    std::cin >> base_one >> base_two;
    opposed[BaseToInt(base_one)][BaseToInt(base_two)] = true;
    opposed[BaseToInt(base_two)][BaseToInt(base_one)] = true;
  }

  size_t N = 0;
  std::cin >> N;

  size_t prev = 8;
  std::set<size_t> prev_set;
  
  for (size_t n = 0; n < N; ++n) {
    char character;
    std::cin >> character;
    result.push_back(character);

    size_t cur = BaseToInt(character);
    bool combine_flg = false;

    if (prev != 8) {
      if (combine[prev][cur] != ' ') {
        result.pop_back();

        char tmp = result.back();
        result.pop_back();
        if (find(result.begin(), result.end(), tmp) == result.end())
          prev_set.erase(prev);

        result.push_back(combine[prev][cur]);
        combine_flg = true;
      }
    }

    bool opposed_flg = false;
    if (!combine_flg) {
      for (std::set<size_t>::iterator it = prev_set.begin();
           it != prev_set.end();
           ++it) {
        if (opposed[*it][cur] == true) {
          result.clear();
          prev_set.clear();
          opposed_flg = true;
          break;
        }
      }
    }

    if (!opposed_flg && !combine_flg) {
      prev_set.insert(cur);
      prev = cur;
    } else {
      prev = 8;
    }
  }
}

void PrintOutput(size_t t, std::list<char>& result) {
  size_t result_size = result.size();
  if (result_size == 0) {
    printf("Case #%d: []\n", t+1);
    return;
  }

  printf("Case #%d: [", t+1);
  for (size_t i = 0; i < result_size - 1; ++i) {
    printf("%c, ", result.front());
    result.pop_front();
  }

  printf("%c]\n", result.front());
}

} //namespace

int main() {
  size_t T = 0;
  std::cin >> T;

  for (size_t t = 0; t < T; ++t) {
    char combine[8][8];
    bool opposed[8][8];
    init(combine, opposed);
    
    std::list<char> result;
    ProcessInput(result, combine, opposed);
    PrintOutput(t, result);
  }

  return 0;
}
