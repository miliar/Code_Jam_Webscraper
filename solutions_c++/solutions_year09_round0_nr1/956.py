
#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
using namespace std;

#define MAX 26
struct trie {   
  trie * next[MAX];
  int val;

  trie() { val = 0; memset(next, 0, MAX * sizeof(trie *)); }
  ~trie() { for(int i=0;i<MAX;i++) if(next[i]) delete next[i]; }
};

//insere caso a palavra nao exista, retorna o numero de ocorrências
int trie_insert(trie * t, const char *s) {   
  while(*s) {
    if(!t->next[*s-'a']) t->next[*s-'a'] = new trie();
    t = t->next[*s-'a'];
    s++;
  }
  return ++t->val;
}

int trie_search(trie *t, const char *s) {
  while(*s) {
    if(!t->next[*s-'a']) return 0;
    t = t->next[*s-'a'];
    s++;
  }
  return t->val;
}

trie t;
int L, D, N;
string words[5000];

unsigned int calculate(string pattern, trie * node, int idx = 0)
{
  int ways = 0;

  while (node && pattern[idx] != '(' && idx < pattern.size())
    node = node->next[pattern[idx++] - 'a'];

  if (node == NULL)
    return 0;

  if (idx == pattern.size())
    return 1;

  int closing_idx = idx;
  while (pattern[closing_idx++] != ')');

  //cout << "range: " << pattern.substr(idx, closing_idx - idx) << endl;
  for (idx++; pattern[idx] != ')'; idx++)
    ways += calculate(pattern, node->next[pattern[idx] - 'a'], closing_idx);

  return ways;
}

int main()
{
  string pattern;

  cin >> L >> D >> N;

  for (int i = 0; i < D; i++)
  {
    cin >> words[i];
    trie_insert(&t, words[i].c_str());
  }

  sort(words, words + D);
  // 5000 log 5000

  for (int i = 0; i < N; i++)
  {
    cin >> pattern;
    printf("Case #%d: %u\n", i+1, calculate(pattern, &t));
  }

  return 0;
}
