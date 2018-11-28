#include<iostream>
#include<fstream>
using namespace std;

int main(){
  char dict[26];
  dict['r'-'a']='q';
  ifstream fin("dic.txt");
  string s1,s2;
  for (int i=0 ;i<4; ++i) {
    fin>>s1>>s2;
    for(int j=0; j<s1.size(); ++j){
      dict[s1[j]-'a']=s2[j];
    }
  }
  int t;
  cin>>t;
  getline(cin,s1);
  for(int ca=1; ca<=t; ++ca) {
    getline(cin, s1);
    cout<<"Case #"<<ca<<": ";
    for(int j=0; j<s1.size(); ++j) {
      if (s1[j] == ' ') {
        cout<<' ';
      }else {
        cout<<dict[s1[j]-'a'];
      }
    }
    cout<<endl;
  }
}
