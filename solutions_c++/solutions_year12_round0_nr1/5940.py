#include <iostream>
#include <string>

using namespace std;

int main() {
  char from[27] = "abcdefghijklmnopqrstuvwxyz";
  char to[27]   = "yhesocvxduiglbkrztnwjpfmaq";
  char line[150];
  int testcases;

  cin >> testcases;
  cin.get();
  for (int i = 0; i < testcases; i++) {
    cin.getline(line, 120);
    cout << "Case #" << i + 1 << ": ";
    for (int j = 0; line[j] != '\0'; j++) {
     if (line[j] == ' ') {
       cout << line[j];
       continue;
     }
     cout << to[line[j] - 'a'];
    }
    cout << endl;
  }
  
  return 0;
}