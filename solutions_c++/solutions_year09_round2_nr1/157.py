#include <cassert>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

void ln() {
  putchar('\n');
}

struct A {
  const char* s;
  int p;
  A(const char* s) : s(s), p(0) {}
  void skip() {
    while (isspace(s[p])) p++;
  }
  char next() {
    skip();
    return s[p++];
  }
  char peek() {
    skip();
    return s[p];
  }
  double read_double() {
    char t[100] = {};
    int n = 0;
    skip();
    while (isdigit(s[p]) || s[p] == '.')
      t[n++] = s[p++];
    double d;
    sscanf(t, "%lf", &d);
    return d;
  }
  string read_attr() {
    char t[100] = {};
    int n = 0;
    skip();
    while (isalpha(s[p]))
      t[n++] = s[p++];
    return string(t);
  }
};

struct Tree {
  bool isleaf;
  string attr;
  double d;
  Tree* left;
  Tree* right;
  Tree() {
    isleaf = true;
    left = right = NULL;
  }
};

Tree* pa(A& a) {
  assert(a.next() == '(');

  Tree* t = new Tree();
  t->d = a.read_double();
  // printf("d:%.2lf\n", t->d);

  if (a.peek() == ')')
    t->isleaf = true;
  else {
    t->isleaf = false;
    t->attr = a.read_attr();
    // printf("attr:%s\n", t->attr.c_str());
    t->left = pa(a);
    t->right = pa(a);
  }

  assert(a.next() == ')');
  return t;
}

Tree* parse(string& text) {
  A a(text.c_str());
  return pa(a);
}

double calc(vector<string>& attrs, Tree* root) {
  double p = 1;
  Tree* t = root;
  while (t != NULL) {
    p *= t->d;
    if (t->isleaf) break;

    bool have = false;
    for (int i = 0; i < (int)attrs.size(); i++) {
      if (attrs[i] == t->attr) {
        // printf("have %s\n", t->attr.c_str());
        have = true;
        break;
      }
    }
    if (have)
      t = t->left;
    else
      t = t->right;
  }
  return p;
}

int main() {
  char s[1000];
  gets(s);
  int ncases = atoi(s);
  for (int cc = 0; cc < ncases; cc++) {
    gets(s);
    int n = atoi(s);
    string text;
    for (int i = 0; i < n; i++) {
      gets(s);
      text = text + s;
    }
    // printf("text:%s\n", text.c_str());

    gets(s);
    int m = atoi(s);

    Tree* root = parse(text);

    printf("Case #%d:\n", cc+1);
    for (int i = 0; i < m; i++) {
      gets(s);
      stringstream ss(s);
      string t;
      ss >> t; // animal name
      // printf("name:%s\n", t.c_str());
      int cnt;
      ss >> cnt;
      vector<string> attrs;
      for (int j = 0; j < cnt; j++) {
        string a;
        ss >> a;
        attrs.push_back(a);
      }

      printf("%.7lf\n", calc(attrs, root));
    }
  }
}

