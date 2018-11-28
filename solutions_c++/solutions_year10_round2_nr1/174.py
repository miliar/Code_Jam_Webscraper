#include <iostream>
#include <map>

using namespace std;

string S;
int cnt;

class node {
public:
  map<string, node *> sons;

  node() {
    ++cnt;
  }
  void insert(int pos) {
    if (pos >= S.length()) {
      return;
    }
    int e = pos;
    while (e < S.length() && S[e] != '/') {
      ++e;
    }
    string tmp(S.begin() + pos, S.begin() + e);
    if (sons.find(tmp) == sons.end()) {
      sons[tmp] = new node();
    }
    sons[tmp]->insert(e + 1);
  }
};

int i, j, k;
int nTests, test;
node *root;
int N, M;

int main() {
  scanf("%d", &nTests);
  for (test = 1; test <= nTests; ++test) {
    root = new node();
    scanf("%d %d", &N, &M);
    for (i = 1; i <= N; ++i) {
      cin >> S;
      root->insert(1);
    }
    cnt = 0;
    for (i = 1; i <= M; ++i) {
      cin >> S;
      root->insert(1);
    }
    printf("Case #%d: %d\n",test,cnt);
  }
  return 0;
}
