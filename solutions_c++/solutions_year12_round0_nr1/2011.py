#include <iostream>
#include <string>
using namespace std;

//                abcdefghijklmnopqrstuvwxyz 
const string M = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
  int tcas;
  cin >> tcas;
  string line;
  getline(cin, line);
  for (int cas = 1; cas <= tcas; ++cas) {
    cout << "Case #" << cas << ": ";
    getline(cin, line);
    int n = line.size();
    for (int i = 0; i < n; ++i) {
      if ('a' <= line[i] and line[i] <= 'z') cout << M[line[i] - 'a'];
      else cout << line[i];
    }
    cout << endl;
  }
}
