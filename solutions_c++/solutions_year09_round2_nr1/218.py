#include <iostream>
#include <string>
#include <set>

using namespace std;

struct tree {
  double p;
  tree *left, *right;
  string f;

  tree() : p(1), left(0), right(0) {}

  ~tree() {
    if(left) delete left;
    if(right) delete right;
  }

};

istream& operator>>(istream& S, tree& T) {
  if(T.left) delete T.left;
  if(T.right) delete T.right;
  T.left = T.right = 0;
  char c;
  S >> c;
  //std::cerr << c;
  S >> T.p;
  //std::cerr << T.p;
  S >> c;
  //if(c == ')') std::cerr << c;
  //std::cerr << c <<"\n";
  if(c == ')') return S;
  S.putback(c);
  S >> T.f;
  //std::cerr << T.f << ' ';
  T.left = new tree;
  T.right = new tree;
  S >> *T.left >> *T.right;
  S >> c;
  //std::cerr << c;
  //assert(c == ')');
  return S;
}

tree root;

double cute(const set<string>& fe, const tree * r = &root) {
  double p = 1;
  for(;r;) {
    //cerr << "*" << r->p;
    p *= r->p;
    if(!r->left) break;
    if(fe.count(r->f)) r = r->left;
    else r = r->right;
  }
  //std::cerr << '\n';
  return p;
}

int main() {
  int Tnum;
  cin >> Tnum;
  cout.precision(7);
  cout << fixed;
  for(int tcase=1;tcase<=Tnum;tcase++) {
    cout << "Case #" << tcase << ":\n";
    int lines;
    cin >> lines >> root;
    //std::cerr << "Tree read!:" << root.p << '\n';
    int wcount;
    cin >> wcount;
    for(int i=0;i<wcount;i++) {
      string tmp;
      int fsize;
      cin >> tmp >> fsize;
      set<string> feature;
      for(int j=0;j<fsize;j++){
	cin >> tmp;
	feature.insert(tmp);
      }
      //std::cerr << root.p << '\n';
      cout << cute(feature) << '\n';
    }
  }
  return 0;
}
