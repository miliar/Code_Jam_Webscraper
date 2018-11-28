#include <algorithm>
#include <cassert>
#include <cstdio>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

#define PROBLEM_ID "A"

const int ALPHABET = 26;

struct TrieNode {
  int index;
  int next[ALPHABET];
  int word_index;

  TrieNode() {
    index = -1;
    for (int i = 0; i < ALPHABET; ++i) {
      next[i] = -1;
    }
    word_index = -1;
  }
};

void AddNode(vector<TrieNode>* trie) {
  trie->push_back(TrieNode());
  trie->back().index = trie->size() - 1;
}

int GetCode(char c) {
  return c - 'a';
}

void BuildTrie(const vector<string>& words, vector<TrieNode>* trie) {
  AddNode(trie);
  for (int i = 0; i < words.size(); ++i) {
    int index = 0;
    for (int j = 0; j < words[i].length(); ++j) {
      int code = GetCode(words[i][j]);
      if (trie->at(index).next[code] == -1) {
        trie->at(index).next[code] = trie->size();
        AddNode(trie);
      }
      index = trie->at(index).next[code];
    }
    trie->at(index).word_index = i;
  }
}

void GetVariants(const string& text, vector<string>* variants) {
  for (int i = 0; i < text.length(); ++i) {
    if (text[i] != '(') {
      variants->push_back(string(1, text[i]));
    } else {
      string cur = "";
      ++i;
      while (text[i] != ')') {
        cur += text[i];
        ++i;
      }
      variants->push_back(cur);
    }
  }
}

void CountVariantsRecursive(const vector<string>& variants, const vector<TrieNode>& trie, int trie_index, int depth, vector<bool>* has_word) {
  if (depth == variants.size()) {
    if (trie[trie_index].word_index != -1) {
      has_word->at(trie[trie_index].word_index) = true;
    }
    return;
  }
  for (int i = 0; i < variants[depth].length(); ++i) {
    int code = GetCode(variants[depth][i]);
    if (trie[trie_index].next[code] != -1) {
      CountVariantsRecursive(variants, trie, trie[trie_index].next[code], depth + 1, has_word);
    }
  }
}

int GetVariantCount(const string& to_test, const vector<TrieNode>& trie, int words_count) {
  vector<string> variants;
  GetVariants(to_test, &variants);
  vector<bool> has_word(words_count);
  CountVariantsRecursive(variants, trie, 0, 0, &has_word);
  int variants_count = 0;
  for (int i = 0; i < words_count; ++i) {
    if (has_word[i]) {
      ++variants_count;
    }
  }
  return variants_count;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int length, word_count, test_count;
  cin >> length >> word_count >> test_count;
  vector<string> words(word_count);
  for (int i = 0; i < word_count; ++i) {
    cin >> words[i];
  }
  vector<TrieNode> trie;
  BuildTrie(words, &trie);
  for (int i = 0; i < test_count; ++i) {
    string to_test;
    cin >> to_test;
    cout << "Case #" << i + 1 << ": " << GetVariantCount(to_test, trie, word_count) << endl;
  }
  return 0;
}
