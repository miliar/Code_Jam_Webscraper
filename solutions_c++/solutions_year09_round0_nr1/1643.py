#include <stdio.h>
#include <string.h>
#include <vector>
#include <string>

using namespace std;

typedef struct node Node;
struct node {
    node(void);
    Node* next[26];
};

struct word {
  word(int length) {
    letters.resize(length);
    for (int offset = 0; offset < length; offset++) {
      char next = getchar();
      if (next == '(') {
        for (next = getchar(); next != ')'; next=getchar()) {
          letters[offset].push_back(next);
        }
      } else {
        letters[offset].push_back(next);
      }
    }
    getchar();
  }

  int count(Node* trie, int offset=0) {
    if (offset >= letters.size()) {
      return 1;
    }
    string& current_letter = letters[offset];
    int total = 0;
    for (unsigned int i = 0; i < current_letter.size(); i++) {
      int letter = current_letter[i] - 'a';
      if (trie->next[letter]) {
        total += count(trie->next[letter], offset + 1);
      }
    }
    return total;
  }

  vector<string> letters;
};

node::node(void) {
  memset(next, NULL, sizeof(next));
}

void read_word(int num_letters, Node* trie);

int main(int argc, char** argv) {
  int n,l,d;
  scanf("%d %d %d", &l, &d, &n);
  getchar();
  Node* root = new Node;
  for (int i = 0; i < d; i++) {
    read_word(l, root);
  }
  for (int i = 0; i < n; i++) {
    word word(l);
    printf("Case #%d: %d\n", i+1, word.count(root));
  }
  return 0;
}

void read_word(int num_letters, Node* trie) {
  if (num_letters == 0) {
    getchar();
    return;
  }
  char next = getchar();
  next -= 'a';
  if (!trie->next[next]) {
    trie->next[next] = new Node;
  }
  read_word(num_letters - 1, trie->next[next]);
}
