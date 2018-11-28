#include <algorithm>
#include <cstring>
#include <iostream>
#include <map>
#include <string>
#include <vector>

std::string solve(std::vector<std::string> replacement_patterns,
    std::vector<std::string> opposed_patterns,
    std::string input) {
  int table[256] = {};

  std::string result;
  for (std::size_t i = 0; i < input.size(); ++i) {
    result += input[i];
    ++table[(int)input[i]];
    while (result.length() > 1) {
      std::string last_two = result.substr(result.length() - 2);
      bool replacement_occurs = false;
      for (std::size_t j = 0; j < replacement_patterns.size(); ++j) {
        if (last_two == replacement_patterns[j].substr(0, 2)) {
          result.resize(result.length() - 2);
          result += replacement_patterns[j][2];
          --table[(int)replacement_patterns[j][0]];
          --table[(int)replacement_patterns[j][1]];
          ++table[(int)replacement_patterns[j][2]];
          replacement_occurs = true;
          break;
        }
      }
      if (!replacement_occurs) {
        std::reverse(last_two.begin(), last_two.end());
        replacement_occurs = false;
        for (std::size_t j = 0; j < replacement_patterns.size(); ++j) {
          if (last_two == replacement_patterns[j].substr(0, 2)) {
            result.resize(result.length() - 2);
            result += replacement_patterns[j][2];
            --table[(int)replacement_patterns[j][0]];
            --table[(int)replacement_patterns[j][1]];
            ++table[(int)replacement_patterns[j][2]];
            replacement_occurs = true;
            break;
          }
        }
        if (!replacement_occurs) {
          break;
        }
      }
    }
    if (result.length() == 1) {
      continue;
    }

    for (std::size_t j = 0; j < opposed_patterns.size(); ++j) {
      if (result[result.length() - 1] == opposed_patterns[j][1]) {
        if (table[(int)opposed_patterns[j][0]]) {
          std::memset(table, 0, sizeof(table));
          result.clear();
        }
      } else if (result[result.length() - 1] == opposed_patterns[j][0]) {
        if (table[(int)opposed_patterns[j][1]]) {
          std::memset(table, 0, sizeof(table));
          result.clear();
        }
      }
    }
  }
  return result;
}

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int C;
    std::cin >> C;
    std::vector<std::string> replacement_patterns;
    for (int c = 1; c <= C; ++c) {
      std::string replacement_pattern;
      std::cin >> replacement_pattern;
      replacement_patterns.push_back(replacement_pattern);
    }

    int D;
    std::cin >> D;
    std::vector<std::string> opposed_patterns;
    for (int d = 1; d <= D; ++d) {
      std::string opposed_pattern;
      std::cin >> opposed_pattern;
      opposed_patterns.push_back(opposed_pattern);
    }

    int N;
    std::cin >> N;
    std::string input;
    std::cin >> input;
    if (input.length() != (std::size_t)N) {
      std::cerr << "error: invalid format" << std::endl;
      return -1;
    }

    std::string result = solve(replacement_patterns, opposed_patterns, input);
    std::cout << "Case #" << t << ": [";
    for (std::size_t i = 0; i < result.length(); ++i) {
      if (i != 0) {
        std::cout << ", ";
      }
      std::cout << result[i];
    }
    std::cout << ']' << std::endl;
  }
  return 0;
}
