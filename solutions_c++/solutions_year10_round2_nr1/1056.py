#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

struct N {
  string dirname;
  N* child[128];
  N(string d):dirname(d){ memset(child, 0, sizeof(child)); }
  N(){ memset(child, 0, sizeof(child)); }
  ~N(){
    for(int i = 0; i < 128; i++)
      if(child[i] != NULL) child[i]->~N();
    delete this;
  }
};

N* root;

vector<string> token(string path){
  vector<string> ret;
  for(int i = 0; i < path.length(); ){
    int t = path.find('/', i+1);
    if(t == (int)string::npos){
      t = path.length();
    }
    string dir = path.substr(i+1, t - i - 1);
    ret.push_back(dir);
    i = t;
  }
  return ret;
}

int insert(string path){
  int ret = 0;
  N* dirp = root;
  vector<string> tok = token(path);
  for(int i = 0; i < tok.size(); i++){
    int j;
    for(j = 0; j < 128; j++){
      if(dirp->child[j] == NULL) break;
      if(dirp->child[j]->dirname == tok[i]) break;
    }
    if(dirp->child[j] == NULL){
      ret++;
      dirp->child[j] = new N(tok[i]);
    }
    dirp = dirp->child[j];
  }
  return ret;
}

int main(){

  int T;
  cin >> T;
  for(int t = 1; t <= T; t++){
    root = new N;
    int NN, M;
    cin >> NN >> M;
    string path;
    for(int i = 0; i < NN; i++){
      cin >> path;
      insert(path);
    }
    int ans = 0;
    for(int i = 0; i < M; i++){
      cin >> path;
      ans += insert(path);
    }
    cout << "Case #" << t << ": " << ans << endl;
  }

  return 0;
}
