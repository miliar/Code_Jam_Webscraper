#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>

using namespace std;

char buf[256];
string istr(int i) {sprintf(buf,"%d",i); return buf;}
string dstr(double d) {sprintf(buf,"%f",d); return buf;}
int ival(string i) {return atoi(i.c_str());}
double dval(string d) {return(double)atof(d.c_str());}

struct tree {
  double weight;
  string feature;
  tree *left, *right;
};

void clean(tree *t) {
  if (t->left) clean(t->left);
  if (t->right) clean(t->right);
  delete t;
}

int eat_white(int i, string &t) {
  while (i < t.size() && (t[i] == ' ' || t[i] == '\n')) ++i;
  return i;  
}

tree* build_tree(int i, string t) {
  string left, right, w;
  i = eat_white(i,t);
  i++;  // eat (
  i = eat_white(i,t);

  while (('0' <= t[i] && t[i] <= '9') || t[i] == '.') {
    w += t[i++];
  }
  i = eat_white(i,t);

  tree *R = new tree();

  R->left = R->right = NULL;
  R->weight = dval(w);
  R->feature = "";
  
  if (t[i] != ')') {
    while ('a' <= t[i] && t[i] <= 'z') {
      R->feature += t[i++];
    }
    i = eat_white(i,t);
    int b = 0;
    do {
      if (t[i] == '(') b++;
      if (t[i] == ')') b--;
      left += t[i++];
    } while (b);
    i = eat_white(i,t);
    do {
      if (t[i] == '(') b++;
      if (t[i] == ')') b--;
      right += t[i++];
    } while (b);
    R->left = build_tree(0, left);
    R->right = build_tree(0, right);
  }
  return R;
}

void printtree(tree *R) {
  if (R) {
    cout << "(" << R->weight;
    if (R->feature.size()) {
      cout << "[" << R->feature;
      printtree(R->left);
      printtree(R->right);
      cout << "])";
    }
  }
}

vector<string> stoken(string data, string space) {
  vector<string> ret;
  string t="";
  data+=space[0];
  for(int i=0;i<data.length();i++) {
    if(space.find(data[i],0)==string::npos)t+=data[i];
    else if(t.size()!=0){ret.push_back(t); t="";}
  }
  return ret;
}

double decide(double p, tree *R, set<string> &f) {
  if (R == NULL) return p;
  p *= R->weight;
  if (R->feature.size()) {
    if (f.count(R->feature)) {
      return decide(p, R->left, f);
    } else {
      return decide(p, R->right, f);
    }
  } else return p;
}

int main() {

  int N, L, A;
  scanf("%d\n", &N);
  for (int T = 1; T <= N; ++T) {
    scanf("%d\n", &L);
    string t = "";
    for (int i = 0; i < L; ++i) {
      string s;
      getline(cin, s);
      t += s;
    }
    tree *R = build_tree(0, t);
   
    scanf("%d\n", &A);
    printf("Case #%d:\n", T);
    for (int i = 0; i < A; ++i) {
      string s;
      getline(cin, s);
      vector<string> v = stoken(s, " \n0123456789");
      set<string> f;
      for (int i = 1; i < v.size(); ++i) {
        f.insert(v[i]);
      }
      double p = decide(1.0, R, f);
      printf("%0.7lf\n", p);
    }
    clean(R);
  }

  return 0;
}

