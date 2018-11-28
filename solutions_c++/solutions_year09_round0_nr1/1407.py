#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
FILE* fin = freopen("A.in", "r", stdin);
FILE* fout = freopen("A.out", "w", stdout);

struct Node;
struct Node {
  Node *d[26];
  Node() {
    memset(d, 0, sizeof(d));
  }
} trie;

void tAdd(Node* node, char *str) {
  if (!*str) return;
  if (!node->d[*str-'a'])
    node->d[*str-'a'] = new Node();
  tAdd(node->d[*str-'a'], str+1);
}

int tCount(Node* node, char *str) {
  if (!node) return 0;
  if (!*str) return 1;
  if (*str != '(') return tCount(node->d[*str-'a'], str+1);
  char *b = str+2;
  while (*b != ')') b++;
  int n = 0;
  for (str++; str < b; str++)
    n += tCount(node->d[*str-'a'], b+1);
  return n;
}

int L, D, N;

int main() {
  char str[20000];
  scanf("%d%d%d", &L, &D, &N);
  for (int i = 0; i < D; i++) {
    scanf("%s", str);
    tAdd(&trie, str);
  }
  for (int i = 0; i < N; i++) {
    scanf("%s", str);
    printf("Case #%d: %d\n", i+1, tCount(&trie, str));
  }
  fclose(fout);
  cerr << "done\n";
  //while(1);
}
