#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <stack>
#include <string>

using namespace std;

class tree {
public:
  tree(double p): prob(p), feature("*"), yes(NULL), no(NULL) {}
  tree(double p, const string &f, tree *Y, tree *N)
    : prob(p), feature(f), yes(Y), no(N) {}

  double prob;
  string feature;
  tree *yes, *no;
};

int findTreeEnd(const string &s, int i) {
  stack<int> paren;
  do {
    if (s[i] == '(') paren.push(i);
    else if (s[i] == ')') paren.pop();
  } while (++i < s.size() && !paren.empty());
  return i;
}

tree *buildTree(const string &def) {
  string::size_type pos = def.find("("), bpos = def.find_last_of(")");
  if (pos == string::npos || bpos == string::npos) return NULL;
  string sub = def.substr(pos + 1, bpos - pos - 1);

  int i = 0, j;
  for (i = 0; i < sub.size() && (sub[i] == ' ' || sub[i] == '\n'); ++i)
    continue;
  for (j = i;
       j < sub.size() && (sub[j] != ' ' && sub[j] != '\n' && sub[j] != ')');
       ++j)
    continue; 

  double prob;
  sscanf(sub.substr(i, j - i).c_str(), "%lf", &prob);
  sub = sub.substr(j);

  string::size_type open = sub.find("(");
  if (open == string::npos) return new tree(prob);

  char buf[64];
  sscanf(sub.substr(0, open).c_str(), "%s", buf);
  int close = findTreeEnd(sub, open);
  string::size_type open2 = sub.find("(", close);
  int close2 = findTreeEnd(sub, open2);
  string left = sub.substr(open, close - open);
  string right = sub.substr(open2, close2 - open2);
  //  printf("TREE:%s\nFEAT: %s\nLEFT: %s\nRIGHT: %s\n\n",
  //       def.c_str(), buf, left.c_str(), right.c_str());
  return new tree(prob, string(buf), buildTree(left), buildTree(right));
}

int main() {
  int T, L, A, N;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d\n", &L);
    string def;
    for (int i = 0; i < L; ++i) {
      char buf[256];
      fgets(buf, 128, stdin);
      if (buf[strlen(buf) - 1] == '\n') buf[strlen(buf) - 1] = 0;
      def += string(buf);
    }
    tree *root = buildTree(def);
    printf("Case #%d:\n", t);
    scanf("%d\n", &A);
    for (int a = 0; a < A; ++a) {
      char animal[64];
      scanf("%s %d", &animal, &N);
      set<string> features;
      for (int i = 0; i < N; ++i) {
        char buf[64];
        scanf(" %s", buf);
        features.insert(string(buf));
      }
      tree *curr = root;
      double p = 1.0;
      while (curr != NULL) {
        p *= curr->prob;
        if (features.find(curr->feature) == features.end())
          curr = curr->no;
        else
          curr = curr->yes;
      }
      printf("%.7lf\n", p);
    }
  }

  return 0;
}
