#include<iostream>
#include<string>

using namespace std;

const string t="yhesocvxduiglbkrztnwjpfmaq"; 

string convert(const string & s){
  string res=s;
  for(int i=0;i<int(s.size());++i){
    if(s[i]==' ') continue;
    res[i]=t[s[i]-'a'];
  }
  return res;
}

int main(){
  int T;
  cin >> T;
  cin.ignore();
  for(int i=1;i<=T;++i){
    string s;
    getline(cin, s);
    cout << "Case #" << i << ": " << convert(s) << endl;
  }
}
