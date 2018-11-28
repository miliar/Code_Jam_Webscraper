#include <string>
#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

class TreeRoot {
  public:
    double _treevalue;
    string* _feature;
    TreeRoot* _left;
    TreeRoot* _right;
  TreeRoot ( double treevalue ) {
    _treevalue=treevalue;
    _feature=NULL;
    _left=NULL;
    _right=NULL;
  }

};

TreeRoot* readtree() {
  char feat[50];
  char c;
  double weight;
  cin>>weight;
  TreeRoot* res= new TreeRoot(weight);
  while(1) {
    c=fgetc(stdin);
    if(c==' '||c=='\n'||c=='\r') {
      continue;
    }
    if(c==')') {
      return res;
    } else {
      break;
    }
  }
  feat[0]=c;
  int j=1;
  while(1){
    c=fgetc(stdin);
    if(c=='\n'||c==' '||c=='\t'||c=='\r') {
      break;
    }
    feat[j]=c;
    j++;
  }
  feat[j]='\0';
  res->_feature=new string(feat);
  while((c=fgetc(stdin))!='(');
  res->_left=readtree();
  while((c=fgetc(stdin))!='(');
  res->_right=readtree();
  while((c=fgetc(stdin))!=')');
  return res;
}

double checkprob(TreeRoot* t,set<string> &s) {
  if(!(t->_feature)) return t->_treevalue;

/*
  cout <<"-"<<*(t->_feature)<<"-"<<endl;
*/

  double res=t->_treevalue;
  if(s.find(*(t->_feature))==s.end()) {
    return res*checkprob(t->_right,s);
  } else {
    return res*checkprob(t->_left,s);
  }

}

int ntests;
int nlines;
int nanimals;

int main() {
  cin>>ntests;

  for(int i=0;i<ntests;i++) {
    cin>>nlines;
    while((fgetc(stdin))!='(');
    TreeRoot* tree = readtree();
    cin>>nanimals;
    printf("Case #%d:\n",i+1);
    for(int j=0;j<nanimals;j++) {
      string name;
      int nfeats;
      set<string> feats=set<string>();
      cin >> name;
      cin >> nfeats;
      for(int k=0;k<nfeats;k++) {
        string feat;
        cin>>feat;
        feats.insert(feat);
      }
      double res=checkprob(tree,feats);
      printf("%.07f\n",res);

    }

  }




  return 0;
}



