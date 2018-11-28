#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <cassert>
#include <sstream>

using namespace std;

int N;
string tree;
set<string> features;

struct T {
  double w;
  bool has_sub;
  string feature;
  T* yes;
  T* no;
};

T* root;

void skip(istringstream& s) {
  while (isspace(s.peek())) s.ignore();  
}
void parse(istringstream& s, T* cur) {
  char c;
  skip(s);
  s>>c;
  assert(c == '(');
  s>>cur->w;
  skip(s);
  if (s.peek() == ')') {
    cur->has_sub = false;
    s.ignore();
    return;
  } else {
    s>>cur->feature;
    cur->has_sub = true;
    cur->yes = new T;
    cur->no = new T;
    parse(s, cur->yes);
    parse(s, cur->no);
    skip(s);
    s.ignore();
  }
}

double proba(double p, T* cur) {
  p *= cur->w;
  if (!cur->has_sub) return p;
  if (features.find(cur->feature) != features.end())
    return proba(p, cur->yes);
  else 
    return proba(p, cur->no);
}

int main() {
  cin>>N;
  for (int t = 1 ; t <= N ; t++) {
    int L;
    cin>>L; cin.ignore();
    tree.clear();
    for (int i = 0 ; i < L ; i++) {
      string s;
      getline(cin, s);
      tree += s;
      tree += " ";
    }
    string t2;
    for (int i = 0 ; i < tree.size() ; i++) {
      if (tree[i] == '(' || tree[i] == ')') {
	t2 += " ";
	t2 += tree[i];
	t2 += " ";
      } else t2 += tree[i];
    }
    tree = t2;
    root = new T;
    istringstream iss(tree);
    parse(iss, root);

    int A; cin>>A; cin.ignore();
    cout << "Case #" << t << ":\n";
    for (int i = 0 ; i < A; i++) {
      string s;
      cin>>s;
      features.clear();
      int n; cin>>n;
      for (int j = 0 ; j < n ; j++) {
	cin>>s;
	features.insert(s);
      }
      double p = proba(1., root);
      cout.setf(ios::floatfield, ios::fixed);
      cout.precision(7);
      cout << p << endl;
    }
    
  }



}
