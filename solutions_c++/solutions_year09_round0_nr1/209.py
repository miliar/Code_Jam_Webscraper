#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

void ln() {
  putchar('\n');
}

const int N = 20;

class Trie {
public:
  Trie* cs[26];
  Trie() {
    for (int i = 0; i < 26; i++)
      cs[i] = NULL;
  }
  void add(char* s) {
    if (*s == '\0') return;

    int x = *s - 'a';
    if (cs[x] == NULL)
      cs[x] = new Trie();

    cs[x]->add(s+1);
  }
  bool contain(char* s) {
    if (*s == '\0') return true;

    int x = *s - 'a';
    if (cs[x] == NULL) return false;
    return cs[x]->contain(s+1);
  }

};

const int L = 15;

int calc_1(int p, char s[], int len, vector<char> tab[], Trie* trie) {
  if (p == len) {
    return 1;

    s[p] = '\0';
    // printf("s:%s %d\n", s, trie->contain(s));
    return trie->contain(s);
  }

  int sum = 0;
  const vector<char>& v = tab[p];
  for (int i = 0; i < (int)v.size(); i++) {
    s[p] = v[i];
    s[p+1] = '\0';
    if (trie->contain(s))
      sum += calc_1(p+1, s, len, tab, trie);
  }
  return sum;
}

int calc(int len, vector<char> tab[], Trie* trie) {
  char s[100];
  return calc_1(0, s, len, tab, trie);
}

int main() {
  int len;
  int n;
  int ncases;
  scanf("%d %d %d", &len, &n, &ncases);

  Trie* root = new Trie();
  char s[1000];
  vector<char*> words;
  for (int i = 0; i < n; i++) {
    scanf("%s", s);
    assert((int)strlen(s) == len);
    char* t = new char[len+1];
    strcpy(t, s);
    words.push_back(t);

    root->add(s);
  }

  for (int cc = 0; cc < ncases; cc++) {
    scanf("%s", s);
//    printf(">> %s\n", s);

    vector<char> tab[L];
    int p = 0;
    int m = 0;
    while (s[p] != '\0') {
      if (s[p] == '(') {
        p++;
        while (s[p] != ')') {
          tab[m].push_back(s[p]);
          p++;
        }
        assert(s[p] == ')');
        m++;
        p++;
      }
      else {
        tab[m].push_back(s[p]);
        m++;
        p++;
      }
    }

    assert(m == len);
    printf("Case #%d: %d\n", cc+1, calc(len, tab, root));
  }
}

