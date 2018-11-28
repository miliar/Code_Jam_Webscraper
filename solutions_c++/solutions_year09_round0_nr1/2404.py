#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

bool possible(string s, string p) {
  bool res=true, trobat=false,dins=false;
  int c=0;
  for(int i=0;i<p.size();++i){
    if (p[i]=='('){
      trobat=false;
      dins = true;
    }else if (p[i]==')'){
      if(trobat==false) return false;
      dins=false;
      ++c;
    }else{
      if (dins==true){
        if (s[c]==p[i]) trobat=true;      
      }else{
        if (s[c]!=p[i]) return false;
        ++c;
      }
    }
  }
  if(c!=s.size()) return false;
  return true;
}

int main(){
  int l, d, n,res;
  map<string,int> m;
  vector<string> v;
  string s;
  cin >> l >> d>> n;
  for(int i=0; i < d; ++i){
    cin >> s;
    v.push_back(s);
  }
  for(int i=0;i<n;++i){
    cin>>s;
    res=0;
    for(int j=0; j<v.size(); ++j){
      if (possible(v[j],s)==true){
      ++res;
      }
    }
    cout << "Case #" << i+1 << ": "<<res <<endl;
  }
}
