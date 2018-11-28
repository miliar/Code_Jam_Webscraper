#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
  
  freopen("AA.in", "r", stdin);
  freopen("AA.out", "w", stdout);
  
  char c[27];
  c[0] = 'y';
  c[1] = 'h';
  c[2] = 'e';
  c[3] = 's';
  c[4] = 'o';
  c[5] = 'c';
  c[6] = 'v';
  c[7] = 'x';
  c[8] = 'd';
  c[9] = 'u';
  c[10] = 'i';
  c[11] = 'g';
  c[12] = 'l';
  c[13] = 'b';
  c[14] = 'k';
  c[15] = 'r';
  c[16] = 'z';
  c[17] = 't';
  c[18] = 'n';
  c[19] = 'w';
  c[20] = 'j';
  c[21] = 'p';
  c[22] = 'f';
  c[23] = 'm';
  c[24] = 'a';
  c[25] = 'q';

  int n;
  string s;
  scanf("%d\n", &n);
  for (int i = 0; i < n; i++){
    getline(cin, s);
    
    cout << "Case #" << i + 1 << ": ";
    for (int j = 0; j < s.length(); j++){
      if (s[j] != ' ') cout << c[s[j] - 'a'];
      else cout << ' ';
    }
    cout << "\n";
  }
  
  return 0;
}