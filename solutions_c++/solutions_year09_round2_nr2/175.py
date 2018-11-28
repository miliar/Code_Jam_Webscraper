#include <algorithm>
#include <cassert>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> vi;

void ln() {
  putchar('\n');
}

void calc(char* s) {
  vi v;
  for (int i = 0; s[i] != '\0'; i++)
    v.push_back(s[i] - '0');

  vi w;
  for (int i = v.size()-1; i >= 0; i--) {
    if (!w.empty() && v[i] < w.back()) {
      for (int j = 0; j < i; j++)
        printf("%d", v[j]);

      w.push_back(v[i]);
      sort(w.begin(), w.end());
      for (int j = 0; j < (int)w.size(); j++) {
        if (v[i] < w[j]) {
          printf("%d", w[j]);
          w.erase(w.begin()+j);
          break;
        }
      }

      for (int j = 0; j < (int)w.size(); j++)
        printf("%d", w[j]);
      ln();
      return;
    }
    else {
      w.push_back(v[i]);
      sort(w.begin(), w.end());
    }
  }

  sort(v.begin(), v.end());
  for (int i = 0; i < (int)v.size(); i++) {
    if (v[i] > 0) {
      printf("%d", v[i]);
      v.erase(v.begin()+i);
      break;
    }
  }

  putchar('0');
  for (int i = 0; i < (int)v.size(); i++) {
    printf("%d", v[i]);
  }
  ln();
  // assert(false);
}

int main() {
  int ncases;
  scanf("%d", &ncases);
  for (int cc = 0; cc < ncases; cc++) {
    char s[1000];
    scanf("%s", s);

    printf("Case #%d: ", cc+1);
    calc(s);
  }
}
