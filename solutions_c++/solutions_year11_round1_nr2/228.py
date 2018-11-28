#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <list>

using namespace std;

struct String {
  int places[26]; // Bit vector
  int lets;
  string str;
  int idx;
  String() : lets(0) {
    memset(places, 0, sizeof(places));
  }
};

typedef map<int, list<String> > Dict;

int main() {
  setvbuf(stdin, NULL, _IOFBF, 10000);
  setvbuf(stdout, NULL, _IOFBF, 10000);

  Dict dict;
  char seq[32];
  int n_cases;
  scanf("%d", &n_cases);
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    printf("Case #%d:", ctr+1);
    dict.clear();
    int n;
    int m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; ++i) {
      scanf("%s", seq);
      string str(seq);
      String s;
      s.str = str;
      s.idx = i;
      for (int j = 0; j < str.size(); ++j) {
        int ch = str[j] - 'a';
        if (s.places[ch] == 0) ++s.lets;
        s.places[ch] |= 1 << j;
      }
      dict[str.size()].push_back(s);
    }
    for (int i = 0; i < m; ++i) {
      scanf("%s", seq);
      int mmax = -1;
      String best;
      // Brute force. Oh yeah.
      for (Dict::iterator it = dict.begin();
           it != dict.end(); ++it) {
        list<String>& lst = it->second;
        for (list<String>::iterator it2 = lst.begin();
             it2 != lst.end(); ++it2) {
          list<String> cands = it->second;
          int points = 0;
          String word = *it2;
          for (int j = 0; j < 26; ++j) {
            int ch = seq[j]-'a';
            bool valid = false;
            for (list<String>::iterator it3 = cands.begin();
                 it3 != cands.end(); ++it3) {
              if (it3->places[ch] != 0) {
                //printf("For word: %s Valid: %c Because: %s\n", word.str.c_str(), ch+'a', it3->str.c_str());
                valid = true;
                break;
              }
            }
            if (!valid) continue;
            if (word.places[ch] != 0) {
              --word.lets;
              if (word.lets == 0) {
                // Success.
                break;
              }
              for (list<String>::iterator it3 = cands.begin();
                   it3 != cands.end(); ++it3) {
                if (it3->places[ch] != word.places[ch]) {
                  it3 = cands.erase(it3);
                  --it3;
                }
              }
            } else {
              for (list<String>::iterator it3  = cands.begin();
                   it3 != cands.end(); ++it3) {
                if (it3->places[ch] != 0) {
                  it3 = cands.erase(it3);
                  --it3;
                }
              }
              ++points;
            }
          }
          if (points > mmax || points == mmax && best.idx > word.idx) {
            mmax = points;
            best = word;
          }
        }
      }
      printf(" %s", best.str.c_str());
    }
    putchar('\n');
  }
  
  return 0;
}
