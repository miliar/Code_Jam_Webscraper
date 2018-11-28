#include <iostream>
#include <cmath>
#include <sstream>
#include <set>

using namespace std;

string int_to_string(int n) {
  stringstream out;
  out << n;
  return out.str();
}

int string_to_int(string s) {
  istringstream buffer(s);
  int value;
  buffer >> value; 
  return value;
}

string rotate(string s) {
  return s[s.size() - 1] + s.substr(0, s.size() - 1);
}

int rotations(int x) {
  return (int) log10(x);
}

int main() {
  int t, a, b, r;
  string rotacionado;
  cin >> t;
  set< pair<int, int> > pares;
  pair<int, int> par;
  for (int i = 0; i < t; i++) {
    cin >> a >> b;
    pares.clear();
    for (int j = a; j <= b; j++) {
      rotacionado = int_to_string(j);
      for (int k = 0; k < rotations(j); k++) {
        rotacionado = rotate(rotacionado);
        r = string_to_int(rotacionado); 
        if (r > j && r <= b) {
          par = make_pair(j, r);
          pares.insert(par);
        }
      }
    }
    cout << "Case #" << i + 1 << ": " << pares.size() << endl;
  }
}
