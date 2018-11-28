#include <cstdio>
#include <vector>
#include <cstring>

char comb[26][26];
char op[26][26];

int main() {
  int t;
  scanf("%d", &t);
  for (int ti = 0; ti < t; ++ti) {
    memset(comb, ' ', sizeof(comb));
    memset(op, ' ', sizeof(op));
    int c;
    scanf("%d", &c);
    for (int i = 0; i < c; i++) {
      char b1, b2, nb;
      scanf(" %c%c%c", &b1, &b2, &nb);
      comb[b1 - 'A'][b2 - 'A'] = nb;
      comb[b2 - 'A'][b1 - 'A'] = nb;
    }
    int d;
    scanf("%d", &d);
    for (int i = 0; i < d; i++) {
      char b1, b2;
      scanf(" %c%c", &b1, &b2);
      op[b1 - 'A'][b2 - 'A'] = true;
      op[b2 - 'A'][b1 - 'A'] = true;
    }
    
    int n;
    scanf("%d", &n);
    std::vector<char> result;
    for (int i = 0; i < n; i++) {
      char c;
      scanf(" %c", &c);
      
      if (!result.empty() && comb[c - 'A'][result.back() - 'A'] != ' ') {
        result.back() = comb[c - 'A'][result.back() - 'A'];
        //printf("%c %u\n", c, result.size());
        continue;
      }
      
      bool has_opposite = false;
      for (size_t j = 0; j < result.size(); j++) {
        if (op[result[j] - 'A'][c - 'A'] != ' ') {
          has_opposite = true;
          break;
        }
      }
      
      if (has_opposite) {
        result.clear();
      }
      else {
        result.push_back(c);
      }
      
      //printf("%c %u\n", c, result.size());
    }
    
    printf("Case #%d: [", ti + 1);
    for (size_t i = 0; i < result.size(); i++) {
      if (i > 0) {
        printf(", ");
      }
      printf("%c", result[i]);
    }
    printf("]\n");
  }

  return 0;
}
