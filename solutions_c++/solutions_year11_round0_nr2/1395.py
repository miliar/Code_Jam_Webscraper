#include <map>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
string solve() {
  int C, O, N;
  string out = "";
  cin >> C;
  char a, b, c;
  map< char, map<char, char> > combine;
  map< char, map<char, bool> > opposed;
  while (C--) {
    cin >> a >> b >> c;
    combine[a][b] = combine[b][a] = c;
  }
  cin >> O;
  while (O--) {
    cin >> a >> b;
    opposed[a][b] = opposed[b][a] = true;
  }
  cin >> N;
  while (N--) {
    cin >> a;
    if (out.size() && combine.count(out[out.size() - 1]) && 
        combine[out[out.size() - 1]].count(a)) {
       out[out.size() - 1] = combine[out[out.size() - 1]][a];
    } else {
       int op = 0;
       for (int i = 0; i < out.size(); i++) {
         if (opposed.count(out[i]) && opposed[out[i]].count(a)) {
           out = "";
           op = 1;
           break;
         }
       }
       if (!op) {
         out += a;
       }
    }
  }
  if (out.size() == 0) {
    return "[]";
  }
  if (out.size() == 1) {
    string outp = "[";
    outp += out;
    outp += "]";
    return outp;
  }
  string outp = "[";
  outp += out[0];
  for (int i = 1; i < out.size(); i++) {
    outp += ", ";
    outp += out[i];
  }
  return outp + "]";
}
int main() {
  int T, i = 0;
  cin >> T;
  while (i++ < T) {
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}

