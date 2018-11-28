#include <iostream>
#include <algorithm>
using namespace std;

string s = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
  int T;
  cin >> T;
  cin.ignore();
  for(int tc = 1; tc <= T; ++tc) {
    string line;
    getline(cin,line);
    cout << "Case #" << tc << ": ";
    for(int i = 0; i < line.size(); ++i) {
      if(line[i] == ' ') cout << ' ';
      else cout << s[line[i]-'a'];
    }
    cout << endl;
  }
  return 0;
}

int main2() {
  int T;
  cin >> T;
  cin.ignore();
  char conv[128];
  fill(conv,conv+128,-1);
  conv['z'] = 'q';
  conv['q'] = 'z';
  while(T--) {
    string line1,line2;
    getline(cin,line1);
    getline(cin,line2);
    for(int i = 0; i < line1.size(); ++i) {
      if(line1[i] == ' ') continue;
      conv[line1[i]] = line2[i];
    }
  }
  for(int i = 'a'; i <= 'z'; ++i) {
    cout << conv[i];
  }
  cout << endl;
  return 0;
}
