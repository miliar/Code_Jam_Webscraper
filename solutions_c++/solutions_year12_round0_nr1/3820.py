#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main() {
  string norm = "yhesocvxduiglbkrztnwjpfmaq ";
  string abc  = "abcdefghijklmnopqrstuvwxyz ";
  //G -> S <=> abc -> norm
  int n;
  string s;
  cin >> n;
  getline(cin,s);
  for (int i=1;i<=n;i++) {
    getline(cin,s);
    string out(s);
//    char out[s.size()];
    for (int j=0;j<s.size();j++) {
      if (s[j] == ' ') out[j] = ' ';
      else out[j] = norm[s[j]-'a'];
    }
    printf("Case #%d: ",i);
    cout << out << endl;
  }
}
