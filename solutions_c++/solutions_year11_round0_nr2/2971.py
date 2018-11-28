#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

struct Combine {
  char e1,e2,to;

  int value() const {
    if(e1 > e2){
      return e1 * 256 + e2;
    } else {
      return e2 * 256 + e1;
    }
  }

  bool operator <(const Combine &a) const {
    return this->value() > a.value();
  }
};

struct Oppose {
  char e1, e2;

  int value() const {
    if(e1 > e2){
      return e1 * 256 + e2;
    } else {
      return e2 * 256 + e1;
    }
  }

  bool operator <(const Oppose &a) const {
    return this->value() > a.value();
  }
};

void solve(int casenum, vector<Combine> &cs, vector<Oppose> &os, string &s){
  set<Combine> stCombine;
  set<Oppose> stOppose;

  for(int i = 0; i < cs.size(); i++){
    stCombine.insert(cs[i]);
  }

  for(int i = 0; i < os.size(); i++){
    stOppose.insert(os[i]);
  }

  vector<char> ret;

  for(int i = 0; i < s.size(); i++){
    bool pass = false;
    if(ret.size() > 0){
      Combine search;
      search.e1 = ret.back();
      search.e2 = s[i];
      set<Combine>::iterator it = stCombine.find(search);
      if(it != stCombine.end()){
        ret.pop_back();
        ret.push_back(it->to);
        pass = true;
      }
    }
    if(!pass){
      for(int l = 0; l < ret.size(); l++){
        Oppose search;
        search.e1 = ret[l];
        search.e2 = s[i];
        set<Oppose>::iterator it = stOppose.find(search);
        if(it != stOppose.end()){
          ret.clear();
          pass = true;
          break;
        }
      }
    }

    if(!pass){
      ret.push_back(s[i]);
    }
  }

  cout << "Case #" << (casenum+1) << ": [";
  for(int i = 0; i < ret.size(); i++){
    cout << ret[i];
    if(i < ret.size() - 1){
      cout << ", ";
    }
  }
  cout << "]" << endl;
    
}

int main(){
  int t;
  cin >> t;
  for(int i = 0; i < t; i++){
    vector<Combine> cs;
    vector<Oppose> os;
    
    int c;
    cin >> c;
    for(int l = 0; l < c; l++){
      Combine comb;
      cin >> comb.e1;
      cin >> comb.e2;
      cin >> comb.to;
      cs.push_back(comb);
    }
     
    int d;
    cin >> d;
    for(int l = 0; l < d; l++){
      Oppose oppose;
      cin >> oppose.e1;
      cin >> oppose.e2;
      os.push_back(oppose);
    }
      
    int n;
    cin >> n;
    string s;
    cin >> s;

    solve(i, cs, os, s);
  }
}
