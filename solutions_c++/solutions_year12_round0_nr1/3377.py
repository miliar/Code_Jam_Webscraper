#include <iostream>
#include <string>
#include <fstream>
using namespace std;

char _[] = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
  int T; cin >> T >> ws;
  
  for(int testcase=1; testcase<=T; testcase++) {
    string s, t;
    getline(cin, s);
    
    cout << "Case #" << testcase << ": ";
    
    for(int i=0; i<s.size(); i++)
      t += s[i]==' ' ? ' ': _[s[i]-'a'];
    
    cout << t << endl;
  }
  
  return 0;
}
