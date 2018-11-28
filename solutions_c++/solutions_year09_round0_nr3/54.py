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

const char pattern[] = "welcome to code jam";

const int TEXT_LENGTH = 1024;
const int PATTERN_LENGTH = 19;

const int MODULO = 10000;

string text;
int text_length;

int dp[TEXT_LENGTH][PATTERN_LENGTH];

int main() {
  ifstream input("test.in");
  ofstream output("test.out");

  int test_cases;
  string tmp;
  getline(input, tmp);
  istringstream str_input(tmp);
  str_input >> test_cases;

  for (int test_case = 1; test_case <= test_cases; test_case++) {

    getline(input, text);
    text_length = text.length();
    
    memset(dp, 0, sizeof(dp));

    for (int j = 0; j < text_length; j++) {
      if (text[j] == pattern[0]) {
        dp[j][0] = 1;
      }
    }

    for (int i = 1; i < PATTERN_LENGTH; i++) {
      int pred = 0;
      for (int j = 0; j < text_length; j++) {
        if (text[j] == pattern[i]) {
          dp[j][i] = pred;
        }
        pred = (pred + dp[j][i - 1]) % MODULO;
      }
    }

    int cnt = 0;
    for (int j = 0; j < text_length; j++) {
      cnt = (cnt + dp[j][PATTERN_LENGTH - 1]) % MODULO;
    }

    output << "Case #" << test_case << ": ";
    if (cnt < 1000) {
      output << '0';
    }
    if (cnt < 100) {
      output << '0';
    }
    if (cnt < 10) {
      output << '0';
    }
    output << cnt << endl;
  }

  input.close();
  output.close();

  return 0;
}
