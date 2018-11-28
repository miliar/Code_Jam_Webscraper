// =====================================================================================
//   [ Filename    ]  pa.cpp
//   [ Description ]  
//   [ Created     ]  09/13/2009 05:02:29 PM CST
//   [ Author      ]  Jiunru Yang , yangjiunru [at] gmail.com, NTUEE
// =====================================================================================

#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;

void solve(int caseNo)
{
   string instr;
   cin >> instr;
   unsigned i;
   map<char,unsigned> mm;
   unsigned base = 2;
   
   cout << "Case #" << caseNo << ": ";
   for (i = 1; i < instr.length(); ++i) {
      if (instr[i] != instr[0])
         break;
   }

   if (i == instr.length()) { // All '1'
      unsigned ans = 1u;
      ans = (ans << instr.length());
      --ans;
      cout << ans << endl;
      return;
   }

   // At least two kinds
   mm[instr[0]] = 1;
   mm[instr[i]] = 0;
   for (; i < instr.length(); ++i) {
      if (mm.find(instr[i]) == mm.end()) {
         mm[instr[i]] = base++;
      }
   }

   unsigned ans = 0;
   for (i = 0; i < instr.length(); ++i) {
      ans = ans * base;
      ans += mm[instr[i]];
   }
   cout << ans << endl;
}

int main()
{
   int T;
   cin >> T;
   for (int t = 1; t <= T; ++t)
      solve(t);
   return 0;
}
