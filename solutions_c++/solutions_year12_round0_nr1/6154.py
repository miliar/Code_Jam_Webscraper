#include <iostream>
using namespace std;
int main(){
  string s;
  int N;

  cin >> N;

  for(int j = 0 ; j < N+1 ; j++){
    getline(cin, s);
    string ans = "";

    for(int i = 0 ; i < s.size() ; i++){
      if(s[i] == 'a') ans += 'y';
      if(s[i] == 'b') ans += 'h';
      if(s[i] == 'c') ans += 'e';
      if(s[i] == 'd') ans += 's';
      if(s[i] == 'e') ans += 'o';
      if(s[i] == 'f') ans += 'c';
      if(s[i] == 'g') ans += 'v';
      if(s[i] == 'h') ans += 'x';
      if(s[i] == 'i') ans += 'd';
      if(s[i] == 'j') ans += 'u';
      if(s[i] == 'k') ans += 'i';
      if(s[i] == 'l') ans += 'g';
      if(s[i] == 'm') ans += 'l';
      if(s[i] == 'n') ans += 'b';
      if(s[i] == 'o') ans += 'k';
      if(s[i] == 'p') ans += 'r';
      if(s[i] == 'q') ans += 'z';
      if(s[i] == 'r') ans += 't';
      if(s[i] == 's') ans += 'n';
      if(s[i] == 't') ans += 'w';
      if(s[i] == 'u') ans += 'j';
      if(s[i] == 'v') ans += 'p';
      if(s[i] == 'w') ans += 'f';
      if(s[i] == 'x') ans += 'm';
      if(s[i] == 'y') ans += 'a';
      if(s[i] == 'z') ans += 'q';
      if(s[i] == ' ') ans += ' ';
    }
    if(j == 0) continue;
    cout <<"Case #" << j << ": " << ans << endl;
  }
  return 0;
}
