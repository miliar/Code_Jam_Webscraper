#include <iostream>
#include <string>
using namespace std;

char data[26];

int main(){
  string s, t;
  while(getline(cin, s)){
    getline(cin, t);
    for(int i = 0; i < s.length(); ++i)
      if(s[i] >= 'a' and s[i] <= 'z')
        data[s[i]-'a'] = t[i];
  }
  for(int i = 0; i < 26; ++i) cout << "'" << data[i] << "', ";
  cout << endl;
}
