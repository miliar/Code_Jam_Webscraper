#include <iostream>
using namespace std;

static const char to[] = "abcdefghijklmnopqrstuvwxyz";
static const char from[] = "yhesocvxduiglbkrztnwjpfmaq";

char decode(char c) {
  if ('a' <= c && c <= 'z') return from[c - 'a'];
  else return c;
}
int main(){
  int n;
  cin >> n;
  cin.ignore();
  for (int i=1; i<=n; i++) {
    string s;
    getline(cin, s);
    cout << "Case #" << i << ": ";
    for (int j=0; j<s.size(); j++) {
      cout << decode(s[j]);
    }
    cout << endl;
  }
  return 0;
}
