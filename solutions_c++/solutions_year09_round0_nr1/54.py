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


vector<vector<int> > split(string pattern) {
  vector<vector<int> > groups;

  int itr = 0;
  int pattern_length = pattern.length();

  while (itr < pattern_length) {
    vector<int> group;
    if (isalpha(pattern[itr])) {
      group.push_back(pattern[itr++] - 'a');
    } else {
      while (pattern[++itr] != ')') {
        group.push_back(pattern[itr] - 'a');
      }
      itr++;
    }
    groups.push_back(group);
  }

  return groups;
}

const int TRIE_SIZE = 6000 * 16;
const int ALPHABET_SIZE = 26;

int word_length;
int dict_size;
int queries;

int next[TRIE_SIZE][ALPHABET_SIZE];
int cnt[TRIE_SIZE];
int depth[TRIE_SIZE];
int trie_size;

int main() {
  ifstream input("test.in");
  ofstream output("test.out");

  input >> word_length >> dict_size >> queries;

  while (dict_size--) {
    string word;
    input >> word;

    int node = 0;
    for (int i = 0; i < word_length; i++) {
      int letter = word[i] - 'a';
      if (!next[node][letter]) {
        next[node][letter] = ++trie_size;
        depth[trie_size] = depth[node] + 1;
      }
      node = next[node][letter];
    }
    cnt[node]++;
  }

  int test_case = 0;
  while (queries--) {
    string pattern;
    input >> pattern;
    vector<vector<int> > groups = split(pattern);
    
    queue<int> prefs;
    prefs.push(0);
    for (int i = 0; i < word_length; i++) {
      while (!prefs.empty()) {
        if (depth[prefs.front()] == i) {
          int node = prefs.front();
          prefs.pop();
          for (int j = 0; j < groups[i].size(); j++) {
            int letter = groups[i][j];
            if (next[node][letter]) {
              prefs.push(next[node][letter]);
            }
          }
        } else {
          break;
        }
      }
    }
      

    __int64 total = 0;
    while (!prefs.empty()) {
      int node = prefs.front();
      total += cnt[node];
      prefs.pop();
    }
      
    output << "Case #" << ++test_case << ": " << total << endl;
  }

  input.close();
  output.close();

  return 0;
}