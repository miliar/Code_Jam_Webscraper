#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

typedef struct tree {
  double prob;
  string feat;
  struct tree *left;
  struct tree *right;
} Node;

Node mem[10000];
int pointer = 0;

Node *aloca () {
  return &(mem[pointer++]);
}

Node *readTree() {
  Node *root = aloca();
  root->left = NULL;
  root->right = NULL;
  root->feat = "";
  
  char c = getchar();
  while (c != '(')
    c = getchar();
  scanf("%lf", &(root->prob));
  
  //printf ("%lf\n", root->prob);
  c = getchar();
  while (c == ' ' || c == '\n')
    c = getchar();
  if (c == ')') {
    return root;
  }
  ungetc(c, stdin);
  char str[15];
  scanf("%s", str);
  root->feat = string(str);
  
  c = getchar();
  while (c == ' ' || c == '\n')
    c = getchar();
  if (c == ')') {
    return root;
  }
  
  ungetc(c, stdin);
  root->left = readTree();
  
  c = getchar();
  while (c == ' ' || c == '\n')
    c = getchar();
  if (c == ')') {
    return root;
  }
  
  ungetc(c, stdin);
  root->right = readTree();
  
  c = getchar();
  while (c == ' ' || c == '\n')
    c = getchar();
  return root;
}

void printTree (Node *tree) {
  if (tree == NULL)
    return;
  printTree(tree->left);
  printf ("%2f\n", tree->prob);
  printTree(tree->right);
}

int main () {
  int N, A, L;
  Node *tree;
  scanf ("%d", &N);
  
  for (int k = 1; k <= N; k++) {
    scanf ("%d", &L);
    tree = readTree();
    //printTree(tree);
    scanf("%d", &A);
    printf ("Case #%d:\n", k);
    for (int i = 1; i <= A; i++) {
      set<string> table;
      char str[15];
      int n;
      scanf("%s%d", str, &n);
      for (int j = 0; j < n; j++) {
        scanf ("%s", str);
        table.insert(string(str));
      }
      double prob = 1.0;
      for (Node *p = tree; p != NULL; ) {
        prob *= p->prob;
        if (table.find(p->feat) != table.end())
          p = p->left;
        else
          p = p->right;
      }
      printf ("%.7f\n", prob);
    }
  }
  return 0;
}
