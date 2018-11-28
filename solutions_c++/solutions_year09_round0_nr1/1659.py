#include <stdio.h>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int L, D, N;
vector<vector<char> > S;

struct Node {
  bool term;
  Node* c[26];
};
Node* root;

Node nodes[1000000];
int nodex = 0;
Node* NewNode() {
  Node* n = &nodes[nodex++];
  memset(n, 0, sizeof(Node));
  return n;
}

void AddDic(char* s) {
  Node* cn = root;
  while (*s) {
    if (!cn->c[*s-'a']) cn->c[*s-'a'] = NewNode();
    cn = cn->c[*s-'a'];
    s++;
  }
  cn->term = true;
}

int go(Node* n, int l) {
  if (n->term) return 1;
  int R = 0;
  for (int i = 0; i < S[l].size(); i++) {
    int index = S[l][i] - 'a';
    if (n->c[index]) R += go(n->c[index], l+1);
  }
  return R;
}

int main() {
  root = NewNode();
  scanf("%d%d%d", &L, &D, &N);
  S.resize(L);
  for (int i = 0; i < D; i++) {
    char buf[1000];
    scanf("%s", buf);
    AddDic(buf);
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < L; j++) S[j].clear();
    char buf[1000];
    scanf("%s", buf);
    int k = 0;
    bool in_p = false;
    for (int j = 0; j < L; k++) {
      if (buf[k] == '(') in_p = true;
      else if (buf[k] == ')') in_p = false;
      else S[j].push_back(buf[k]);
      if (!in_p) j++;
    }
    for (int j = 0; j < L; j++) {
      sort(S[j].begin(), S[j].end());
      unique(S[j].begin(), S[j].end());
    }

    printf("Case #%d: %d\n", i+1, go(root, 0));
  }
  return 0;
}
