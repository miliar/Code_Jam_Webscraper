#include <iostream>
#include <set>
#include <sstream>
#include <cstdio>
#include <cstdlib>

using namespace std;

struct Node {
  double weight;
  string feature;
  Node *yes;
  Node *no;

  Node() : weight(0), feature(""), yes(0), no() {}
  ~Node() { if (yes) delete yes; if (no) delete no; }
};

// called on parens
Node *parse(string s) {

  Node *node = new Node();

  // check if more
  int count = 0;
  for (int i = 0; i < s.length(); i++) {
    if (s[i] == '(') count++;
  }

  // get rid of parens and spaces
  s = s.substr(1, s.length() - 2);
  if (isspace(s[0])) s = s.substr(1);
  if (isspace(s[s.length() - 1])) s = s.substr(0, s.length()-1);

 
  if (count == 1) {
    istringstream iss(s);
    iss >> node->weight;
  } else {

    while (isspace(s[0])) s = s.substr(1);
    while (isspace(s[s.length() - 1])) s = s.substr(0, s.length()-1);

    string a;
    string b;
    string c;
    string d;

    int i = 0;
    while (!isspace(s[i])) i++;
    a = s.substr(0, i);
    while (isspace(s[i])) i++;
    s = s.substr(i);

    i = 0;
    while (!isspace(s[i])) i++;
    b = s.substr(0, i);
    while (isspace(s[i])) i++;
    s = s.substr(i);

    i = 0;
    int level = 0;
    while (true) {
      if (s[i] == '(') level++;
      if (s[i] == ')') level--;
      if (level == 0 && isspace(s[i])) break;
      i++;
    }
    c = s.substr(0, i);
    while (isspace(s[i])) i++;
    s = s.substr(i);

    d = s;

    node->weight = atof(a.c_str());
    node->feature = b;
    node->yes = parse(c);
    node->no = parse(d);
  }

  return node;
}

double Evaluate(Node *tree, set<string> &features) {
  if (tree->yes) {
    double rem = 0;
    if (features.find(tree->feature) == features.end()) {
      rem = Evaluate(tree->no, features);
    } else {
      rem = Evaluate(tree->yes, features);
    }
    return tree->weight * rem;
  } 
  return tree->weight;
}

int main() {
  string t;
  int N;
  getline(cin, t);
  N = atoi(t.c_str());
  for (int caseno = 1; caseno <= N; caseno++) {
    cout << "Case #" << caseno << ":" << endl;

    int L;
    getline(cin, t);
    L = atoi(t.c_str());
    string s;
    for (int i = 0; i < L; i++) {
      getline(cin, t);
      s += t;
    }

    Node *tree = parse(s);
    
    int A;
    getline(cin, t);
    A = atoi(t.c_str());
    for (int i = 0; i < A; i++) {
      getline(cin, t);
      istringstream iss(t);
      string name;
      set<string> features;
      int n;
      iss >> name;
      iss >> n;
      for (int j = 0; j < n; j++) {
	iss >> t;
	features.insert(t);
      }
      printf("%.7lf\n", Evaluate(tree, features));
    }
    
    delete tree;
  }
}
