#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <utility>
#include <deque>

using namespace std;

typedef pair<char, char> Pair;

int main() {
  setvbuf(stdin, NULL, _IOFBF, 10000);
  setvbuf(stdout, NULL, _IOFBF, 10000);

  int n_cases;
  scanf("%d", &n_cases);

  map<Pair, char> mmap;
  set<Pair> sset;
  char seq[128];
  deque<char> deq;
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    mmap.clear();
    sset.clear();
    
    int c;
    scanf("%d", &c);
    for (int i = 0; i < c; ++i) {
      char str[8];
      scanf("%s", str);
      sort(str, str+2);
      mmap[Pair(str[0], str[1])] = str[2];
    }

    int d;
    scanf("%d", &d);
    for (int i = 0; i < d; ++i) {
      char str[8];
      scanf("%s", str);
      sort(str, str+2);
      sset.insert(Pair(str[0], str[1]));
    }

    int n;
    scanf("%d", &n);
    scanf("%s", seq);
    deq.push_back(seq[0]);
    for (int i = 1; i < n; ++i) {
      char prev = -1;
      if (deq.size() > 0) prev = deq.back();
      char curr = seq[i];
      deq.push_back(curr);
      Pair p;
      if (prev < curr) p = Pair(prev, curr);
      else p = Pair(curr, prev);

      // Combine
      if (mmap.find(p) != mmap.end()) {
        char ch = mmap[p];
        //printf("Combine: %c %c -> %c\n", curr, prev, ch);
        deq.pop_back();
        deq.pop_back();
        deq.push_back(ch);
      } else {
        char top = deq.back();
        
        if (deq.size() > 1) {
          for (deque<char>::iterator it = deq.begin();
               it != deq.end()-1; ++it) {
            char ch = *it;
            Pair p;
            if (top < ch) p = Pair(top, ch);
            else p = Pair(ch, top);
            
            if (sset.find(p) != sset.end()) {
              //printf("Clear: %c %c\n", ch, top);
              deq.clear();
              break;
            }
          }
        }
      }

    }

    printf("Case #%d: [", ctr+1);
    bool printed = false;
    while (deq.size() > 0) {
      if (printed) printf(", ");
      printf("%c", deq.front());
      printed = true;
      deq.pop_front();
    }
    printf("]\n");
  }
  
  return 0;
}
