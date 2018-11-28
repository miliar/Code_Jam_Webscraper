#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>

using namespace std;

const int DIGITS = 256;

bool marked[DIGITS];
int value[DIGITS];

int main() {
  ifstream input("test.in");
  ofstream output("test.out");

  int test_cases;
  input >> test_cases;
  for (int test = 0; test < test_cases; test++) {
    string str;
    input >> str;
    int str_length = str.length();

    memset(marked, 0, sizeof(marked));
    memset(value, 0, sizeof(value));
    marked[str[0]] = true;
    value[str[0]] = 1;

    int base = 1;
    for (int i = 0; i < str_length; i++) {
      if (!marked[str[i]]) {
        if (base == 1) {
          value[str[i]] = 0;
        } else {
          value[str[i]] = base;
        }
        base++;
        marked[str[i]] = true;
      }
    }     

    if (base == 1) {
      base++;
    }

    __int64 result = 0;
    for (int i = 0; i < str_length; i++) {
      result = result * base + value[str[i]];
    }
    output << "Case #" << test + 1 << ": " << result << endl;
  }

  input.close();
  output.close();

  return 0;
}