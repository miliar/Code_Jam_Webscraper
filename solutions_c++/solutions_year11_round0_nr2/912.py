#include <iostream>
#include <string>

using namespace std;

const int DEBUG = 0;

char combine_rules[26][26];
bool opposed_rules[26][26];

void PrintCombineRules() {
  for (int i = 0; i < 26; ++i) {
    for (int j = 0; j < 26; ++j) {
      printf("%c ", combine_rules[i][j]);
    }
    printf("\n");
  } 
}

void PrintOpposedRules() {
  for (int i = 0; i < 26; ++i) {
    for (int j = 0; j < 26; ++j) {
      printf("%d ", opposed_rules[i][j]?1:0);
    }
    printf("\n");
  }
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int C;
    cin >> C;
    memset(combine_rules, '\0', sizeof(combine_rules));
    for (int i = 0; i < C; ++i) {
      string combine_rule;
      cin >> combine_rule;
      int tx = combine_rule[0]-'A';
      int ty = combine_rule[1]-'A';
      char tc = combine_rule[2];
      combine_rules[ty][tx] = tc;
      combine_rules[tx][ty] = tc;
    }
    if (DEBUG) {
      PrintCombineRules();
    }

    int D;
    cin >> D;
    memset(opposed_rules, false, sizeof(opposed_rules));
    for (int i = 0; i < D; ++i) {
      string opposed_rule;
      cin >> opposed_rule;
      int tx = opposed_rule[0]-'A';
      int ty = opposed_rule[1]-'A';      
      opposed_rules[ty][tx] = true;
      opposed_rules[tx][ty] = true;
    }
    if (DEBUG) {
      PrintOpposedRules();
    }
    
    int N;
    string elements;
    cin >> N;
    cin >> elements;
    string element_list = "";
    for (int n = 0; n < N; ++n) {
      element_list += elements[n];
      int len = element_list.length();
      if (len < 2) continue;
      int tx = element_list[len-2]-'A';
      int ty = element_list[len-1]-'A';
      if (combine_rules[tx][ty] != '\0') {
	element_list = element_list.substr(0, len-2);
	element_list += combine_rules[tx][ty];
      }
      len = element_list.length();
      if (len < 2) continue;
      tx = element_list[len-1]-'A';
      for (int i = len-2; i >= 0; --i) {
	int ty = element_list[i]-'A';
	if (opposed_rules[tx][ty]) {
	  element_list = "";
	  break;
	}
      }
    }
    printf("Case #%d: [", t);
    int len = element_list.length();
    for (int i = 0; i < len; ++i) {
      printf("%c", element_list[i]);
      if (i != len-1) printf(", ");
    }
    printf("]\n");
  }
}
