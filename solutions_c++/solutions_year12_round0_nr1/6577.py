#include<iostream>
#include<map>
#include<string>
using namespace std;

int main(){
  map<char,char> dict;
  map<char,char>::iterator it;
  string s = "abcdefghijklmnopqrstuvwxyz0";
  string y = "yhesocvxduiglbkrztnwjpfmaq0";
  for (int i=0; i<26; i++){
    dict[s[i]]=y[i];
  }
  // for (int i=0; i<26; i++){
  //   cout<<s[i]<<":"<<dict[s[i]]<<endl;
  // }
  int n;
  cin>>n;
  string t;
  getline(cin,t);
  for(int i =0;i<n;i++){
    getline(cin,t);
    //cout<<t<<endl;
    cout<<"Case #"<<i+1<<": ";
    for(int j = 0; j<t.size(); j++){
      it = dict.find(t[j]);
      // cout<<(*it).first;
      if (it == dict.end()){
    	cout<<t[j];
      }
      else{
    	cout<<(*it).second;
      }
    }
    cout<<endl;
  }
  return 0;
}

