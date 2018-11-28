#include <iostream>
#include <string>
#include <cctype>
#include <set>
using namespace std;

struct decision {
public:
  double weight;
  string feature;
  decision *yes, *no;
  decision() : weight(0), feature(""), yes(NULL), no(NULL) {}
  ~decision() {
    if( yes != NULL ) delete yes;
    if( no  != NULL ) delete no;
  }
};

decision* makeTree()
{
  decision *p = new decision();
  char     c;
  cin >> p->weight >> c;
  //cout << p->weight << endl;
  if( c != ')' ) {
    string str = "";
    while( isalpha(c) ) {
      //cout << c ;
      str += c;
      cin >> c;
    }
    p->feature = str;
    //cout << str << endl;
    p->yes = makeTree();
    cin >> c; //'('
    p->no  = makeTree();
    cin >> c; //')'
  }
  return p;
}

double rating(set<string>& feature, decision* root)
{
  //cout << root->weight << endl;
  if( root->feature == "" ) return root->weight;
  set<string>::iterator p = feature.find(root->feature);
  if( p != feature.end() ) {
    return rating(feature, root->yes) * root->weight;
  } else {
    return rating(feature, root->no) * root->weight;
  }
}

void decide()
{
  decision* root;
  int L;
  char c;
  cin >> L >> c; // c == '('
  root = makeTree();
  int A;
  cin >> A;
  for( int i = 0 ; i < A ; ++i ) {
    string str;
    set<string> feature;
    cin >> str; // Animal name;
    int n;
    cin >> n;
    for( int j = 0 ; j < n ; ++j ) {
      cin >> str;
      feature.insert(str);
    }
    double rate = rating(feature, root);
    printf("%9.7f\n", rate);
  }
}

int main(void)
{
  int N;
  cin >> N;
  for( int i = 1 ; i <= N ; ++i ) {
    cout << "Case #" << i << ":\n";
    decide();
  }
  return 0;
}
