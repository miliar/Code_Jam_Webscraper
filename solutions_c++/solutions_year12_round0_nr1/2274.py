#include <iostream>
#include <map>
#include <string>
using namespace std;

string o, t;

int main(){
  o = "abcdefghijklmnopqrstuvwxyz ";
  t = "ynficwlbkuomxsevzpdrjgthaq ";
  int n; cin>>n;
  string str;
  getline(cin, str);
  for (int i = 0; i < n; ++i){
    getline(cin, str);
    cout<<"Case #"<<i+1<<": ";
    for (int j = 0; j < str.length(); ++j){
      unsigned pos = t.find_first_of(str[j]);
      cout<<o[pos];
    }
    cout<<endl;
  }
} 
