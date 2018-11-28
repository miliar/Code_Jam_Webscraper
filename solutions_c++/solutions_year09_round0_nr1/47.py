#include<iostream>
#include<vector>
using namespace std;

struct Tree{
  int val;
  Tree *p[26];

  Tree(){
    val = -1;
    for(int i = 0; i < 26; i++) p[i] = NULL;
  }
};

void Insert( Tree* tree, string s ){
  Tree *P = tree;
  for(int i = 0; i < s.size(); i++){
    int k = s[i] - 'a';
    if( P->p[k] == NULL ) P->p[k] = new Tree();
    P = P->p[k];
  }
  P->val = 1;  
}

int ans;
int Search(int depth, vector<string> &cell, Tree *P){
  if( cell.size() == depth ){
    if( P->val == 1 ) ans++;
    return 1;
  }

  for(int i = 0; i < cell[depth].size(); i++){
    char ch = cell[depth][i];
    if( P->p[ch - 'a'] ){
      Search(depth + 1, cell, P->p[ch - 'a']);
    }    
  }
  return 0;
}

int main(){
  int L, D, N;
  cin >> L >> D >> N;

  Tree* root = new Tree();  
  for(int i = 0; i < D; i++){
    string str;
    cin >> str;
    Insert(root, str );
  }

  for(int step = 0; step < N; step++){
    string str;
    cin >> str;

    int p = 0;
    vector<string> cell(L);
    
    for(int i = 0; i < str.size(); i++){
      if( str[i] == '(' ) {
        string t;
        while( str[++i] != ')' ) t += str[i];
        cell[p++] += t;
      } else {
        cell[p++] += str[i];
      }
    }

    ans = 0;
    Search(0, cell, root);
    printf("Case #%d: %d\n", step + 1, ans);
  }
}
