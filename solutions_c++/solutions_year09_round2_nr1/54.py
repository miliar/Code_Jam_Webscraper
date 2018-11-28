#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

struct Tree {
  Tree *tyes,*tno;
  string feature;
  double weight;
  Tree(){
		tyes=tno=NULL;
		feature="";
		weight=-1e10;
	}
};

void build(Tree *cur, istringstream &iss) {
  for (string s; iss >> s;) {
    if (s=="(") {
      iss >> (cur->weight);
    }
    else if (s==")") {
      return;
    }
    else {
      cur->feature=s;
      cur->tyes=new Tree;
      build(cur->tyes,iss);
      cur->tno=new Tree;
      build(cur->tno,iss);
    }
  }
}

int main() {
  cout.setf(ios::fixed);
  cout.precision(7);
  int N;
  cin >> N;
  for (int iN=0; iN<N; ++iN) {
    int L;
    cin >> L;
    string stree="",s;
    getline(cin,s);
    for (int i=0; i<L; ++i) {
      getline(cin,s);
      stree+=" "+s;
    }
    for (int i=0; i<stree.size(); ++i) {
      if (stree[i]=='(') {
        stree.insert(i+1," ");
        ++i;
      }
      else if (stree[i]==')') {
        stree.insert(i," ");
        ++i;
      }
    }
    Tree *root=new Tree;
    istringstream iss(stree);
    build(root,iss);
    int A;
    cin >> A;
    cout << "Case #" << iN+1 << ":" << endl;
    for (int i=0; i<A; ++i) {
      cin >> s;
      set<string> F;
      int f;
      cin >> f;
      for (int j=0; j<f; ++j) {
        cin >> s;
        F.insert(s);
      }
      double p=1.0;
      Tree *cur=root;
      for (bool done=0; !done;) {
        p*=cur->weight;
        if (cur->tyes==NULL) done=1;
        else {
          if (F.count(cur->feature)) cur=cur->tyes;
          else cur=cur->tno;
        }
      }
      cout << p << endl;
    }
  }
}
