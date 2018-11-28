#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

void func(string s1, string s2, map<char,char> & dict, map<char,char> & dict2)
{
  for (int i=0;i<s1.size();i++) {
    dict[s1[i]] = s2[i];
    dict2[s2[i]] = s1[i];
  }
}

int main() {

  string str1   = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  string str2   = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  string str3   = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string streq1 = "our language is impossible to understand";
  string streq2 = "there are twenty six factorial possibilities";
  string streq3 = "so it is okay if you want to just give up";

  map<char,char> dict;
  map<char,char> dict2;

  func(str1,streq1,dict,dict2);
  func(str2,streq2,dict,dict2);
  func(str3,streq3,dict,dict2);

  dict['q'] = 'z';
  dict['z'] = 'q';

  int n; cin >> n;

  string t;
  getline(cin,t);

  for (int i=0;i<n;i++) {
    getline(cin,t);
    cout << "Case #" << i+1 << ": ";
    for (int j=0;j<t.size();j++) {
      cout << dict[t[j]];
    }
    cout << endl;
  }

};
