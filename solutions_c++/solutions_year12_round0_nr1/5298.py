#include <iostream>
#include <string>
using namespace std;

char tchar(char x) {
  switch(x) {
    case 'a': return 'y';
    case 'b': return 'h';
    case 'c': return 'e';
    case 'd': return 's';
    case 'e': return 'o';
    case 'f': return 'c';
    case 'g': return 'v';
    case 'h': return 'x';
    case 'i': return 'd';
    case 'j': return 'u';
    case 'k': return 'i';
    case 'l': return 'g';
    case 'm': return 'l';
    case 'n': return 'b';
    case 'o': return 'k';
    case 'p': return 'r';
    case 'r': return 't';
    case 's': return 'n';
    case 't': return 'w';
    case 'u': return 'j';
    case 'v': return 'p';
    case 'w': return 'f';
    case 'q': return 'z'; 
    case 'x': return 'm';
    case 'y': return 'a';
    case 'z': return 'q';
    case ' ': return ' ';
    default: return '\n';
  }
}

string transform(string p) {
  for (int i = 0; i < p.size(); ++i) {
    p[i] = tchar(p[i]);
  }
  return p;
}

int main() {
    int t;
    cin >> t;
    string s;
    getline(cin, s);
    for (int i = 1; i <= t; ++i) {
	getline(cin, s);
	cout << "Case #" << i << ": ";
	cout << transform(s) << endl;
    }
}
