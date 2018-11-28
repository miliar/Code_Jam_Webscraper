#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <climits>
#include <string>
#include <cctype>
#include <cstring>
#include <queue>
#include <stack>
#include <set>

using namespace std;

int main() {
  int T, C, D, N;

  cin >> T;
  cin.ignore();

  int ncase = 0;
  while (cin >> C) {
    ncase++;
    // combinations and destructions table
    char getCombo[128][128];
    bool isOpp[128][128];
    for (int i = 0; i < 128; i++) {
      for (int j = 0; j < 128; j++) {
        getCombo[i][j] = 0;
        isOpp[i][j] = false;
      }
    }
    for (int i = 0; i < C; i++) {
      string combo;
      cin >> combo; // 3 characters
      char ch1, ch2, r;
      ch1 = combo[0];
      ch2 = combo[1];
      r = combo[2];
      getCombo[ch1][ch2] = getCombo[ch2][ch1] = r;
    }
    cin >> D;
    for (int i = 0; i < D; i++) {
      string opp;
      cin >> opp;
      char ch1, ch2;
      ch1 = opp[0];
      ch2 = opp[1];
      isOpp[ch1][ch2] = isOpp[ch2][ch1] = true;
    }
    cin >> N;

    string elems;
    cin >> elems;
    cin.ignore();
    string result; // final list
    for (int i = 0; i < elems.length(); i++) {
      result += elems[i];
      int L = result.length() - 1;
      if (result.length() <= 1) continue;

      char c1, c2, r;
      c1 = result[L - 1];
      c2 = result[L];
      r = getCombo[c1][c2];
      string sr;
      stringstream ss;
      ss << r;
      ss >> sr;
      if (r) {
        result = result.replace(L - 1, 2, sr);
        c2 = r;
      }

      // check for opposites to new char
      for (int j = 0; j < result.length() - 1; j++) {
        if (isOpp[c2][result[j]]) {
          result = "";
          break;
        }
      }
    }
    printf("Case #%d: [", ncase);
    if (!result.length())
      printf("]\n");
    else {
      for (int i = 0; i < result.length() - 1; i++)
        printf("%c, ", result[i]);
      printf("%c]\n", result[result.length() - 1]);
    }
  }
}