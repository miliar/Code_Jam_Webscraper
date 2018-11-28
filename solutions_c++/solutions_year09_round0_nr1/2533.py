#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
ifstream fin("1A-small.in");
ofstream fout("1A-small.out");

struct node;

/** Linked list node. */
typedef struct node {
  int level;
	struct node *next[26];
} node_t;

node_t *trie = new node_t;

bool in_trie(string x) {
  node_t *curnode = trie;
  for (int i=0; i<x.length(); i++) {
    if (curnode->next[x[i] - 'a'] == 0x0)
      return false;
    curnode = curnode->next[x[i] - 'a'];
  }
  return true;
}    
int main() {
    int len, words, cases;
    string winput;
    vector<string> anstrack;
    trie->level = 0;
    fin >> len >> words >> cases;
    for (int q=0;q<26;q++) {
      trie->next[q] = 0x0;
    }
    for (int i=0;i<words;i++) {
      node_t *curnode = trie;
      fin >> winput;
      for (int j=0;j<winput.length();j++) {
        if (curnode->next[winput[j] - 'a'] == 0x0) {
          curnode->next[winput[j] - 'a'] = new node_t;
          curnode->next[winput[j] - 'a']->level = j+1;
          for (int q=0;q<26;q++) {
            curnode->next[winput[j] - 'a']->next[q] = 0x0;
          }
        }
        curnode = curnode->next[winput[j] - 'a'];
      }
    }
    for (int i=0;i<cases;i++) {
      int parencnt, curwordlen;
      fin >> winput;
      parencnt = 0;
      curwordlen = 0;
      anstrack.clear();
      for (int j=0;j<winput.length();) {
        if (winput[j] == '(') {
          parencnt++;
          j++;
        }
        do {
          if (winput[j] == '(') {
            parencnt++;
          } else if (winput[j] == ')') {
            parencnt--;
          } else {
            if (curwordlen == 0) {
              string construct = "";
              construct += winput[j];
              if (in_trie(construct)) {
                anstrack.push_back(construct);
              }
            } else {
              for (int k=0; k<anstrack.size(); k++) {
                if (anstrack[k].length() == curwordlen) {
                  string construct = anstrack[k];
                  construct += winput[j];
                  if (in_trie(construct)) {
                    anstrack.push_back(construct);
                  }
                }
              }
            }
          }
          j++;
        } while (parencnt > 0);
        for (int k=0; k<anstrack.size(); k++) {
          if (anstrack[k].length() <= curwordlen) {
            anstrack.erase(anstrack.begin() + k);
            k--;
          }
        }
        curwordlen++;
    }
      fout << "Case #" << i+1 << ": " << anstrack.size() << endl;
    }
    return 0;
}

