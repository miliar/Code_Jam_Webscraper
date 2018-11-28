#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

string frase = "welcome to code jam";

int main() {
   int n;
   cin >> n;
   string s;
   getline(cin, s);
   for (int t=1; t<=n; ++t) {
      cout << "Case #" << t << ": ";
      getline(cin, s);
      vector<vector<int> > v(19, vector<int>(s.size(), 0));
      v[0][0] = (s[0] == 'w');
      int ws = v[0][0];
      for (int j=1; j<s.size(); ++j)
         if (s[j] == 'w')
            v[0][j] = ++ws;
         else
            v[0][j] = v[0][j-1];
      for (int i=1; i<19; ++i) {
         for (int j=i; j<s.size(); ++j) {
            if (s[j] == frase[i] and v[i-1][j] != 0)
               v[i][j] = (v[i][j-1] + v[i-1][j])%10000;
            else
               v[i][j] = v[i][j-1];
         }
      }
//       for (int i=0; i<19; ++i) {
//          for (int j=0; j<s.size(); ++j)
//             cout << v[i][j] << ' ';
//          cout << endl;
//       }
      cout << setfill('0') << setw(4) << v[18][s.size()-1] << endl;
   }
}
