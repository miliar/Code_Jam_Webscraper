#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>
using namespace std;

int toint(string s) {
   stringstream ss(s);
   int n;
   ss >> n;
   return n;
}

string tostring(int n) {
   stringstream ss;
   ss << n;
   string s;
   ss >> s;
   return s;
}

int main() {
   int t;
   cin >> t;
   for (int tt=1; tt<=t; ++tt) {
      cout << "Case #" << tt << ": ";
      string s;
      cin >> s;
      string s1 = s;
      next_permutation(s.begin(), s.end());
      if (s > s1)
         cout << s << endl;
      else {
         s += "0";
         sort(s.begin(), s.end());
         if (s[0] == '0')
            for (int i=0; i<s.size(); ++i)
               if (s[i] != '0') {
                  swap(s[i], s[0]);
                  break;
               }
         cout << s << endl;
      }
   }
}