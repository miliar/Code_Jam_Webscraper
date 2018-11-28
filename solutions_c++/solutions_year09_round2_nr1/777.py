#include<iostream>
#include<vector>
#include<iomanip>
#include<sstream>
using namespace std;

struct Node{
  double weight;
  string feature;
  Node* left;
  Node* right;

  Node(){
    weight = 0;
    feature = "";
    left = NULL;
    right = NULL;
  }
  
};

bool isLeaf(const string& s, int start){
  int count = 0;
  for(int i = start; i < s.size(); i++){
    if( s[i] == '(' ) count++;
    if( s[i] == ')' ) count--;
    if( count >= 2 ) return false;
    if( count == 0 ) return true;
  }
  cout << "errer" << endl;
  return false;
}

void BuildTree(Node *node, string s, int& p){
  while( isspace(s[p]) ) p++;
//   cout << s.substr( p ) << endl;
  if( isLeaf(s, p) ){
//     cout << "leaf" << endl;
    stringstream ss( s.substr(p + 1) );
    ss >> (node->weight) >> ws;

    while( s[p] != ')' ) p++;
    p++;
    
  } else {
//     cout << "node" << endl;
    stringstream ss( s.substr(p + 1) );
    ss >> (node->weight) >> ws;
    ss >> (node->feature) >> ws;
    
    node->left = new Node;
    node->right = new Node;

    p++; // '('
    while( s[p] != '(' ) p++;
    
    BuildTree(node->left, s, p);
    BuildTree(node->right, s, p);

    while( s[p] != ')' ) p++;
    p++;
  }
}

void CleanTree( Node* p, int depth = 0){
//   for(int i = 0; i < depth; i++) cout << "  ";
  if( p->left ){
//     cout << "(" << p -> weight << " " << p -> feature << endl;
    
    CleanTree( p -> left, depth + 1 );
    CleanTree( p -> right, depth + 1 );

//     for(int i = 0; i < depth; i++) cout << "  ";
//     cout << ")" << endl;
  } else {
//     cout << "(" << p->weight << ")" << endl;
    free( p );
  }
  return;
}

double Solve(Node* node, vector<string>& vs, double p){
  if( node->left ) { // goto subtree

    if( find(vs.begin(), vs.end(), node->feature ) != vs.end() ) {
      return Solve(node->left, vs, p * node->weight);
    } else {
      return Solve(node->right, vs, p * node->weight);
    }    
  } else { // leaf
    return p * node->weight;
  }

  cout << "errer" << endl;
  return -1;
}

int main(){
  int T;
  cin >> T;
  for(int tno = 0; tno < T; tno++){
    printf("Case #%d:\n", tno + 1);

    int L;
    cin >> L >> ws;
    string str;
    for(int l = 0; l < L; l++){
      string line;
      getline(cin, line);
      str += line;
    }

    Node *root = new Node();
    int temp = 0;
    BuildTree(root, str, temp);
    
    int A; cin >> A;
    
    for(int a = 0; a < A; a++){
      string name; cin >> name;
      int K; cin >> K;
      vector<string> vs;
      for(int k = 0; k < K; k++){
        string feat; cin >> feat;
        vs.push_back( feat );
      }

      double ans = Solve(root, vs, 1);
      printf("%.7f\n", ans);
    }

    CleanTree(root);
  }
}
