// =====================================================================================
//   [ Filename    ]  main.cpp
//   [ Description ]  Welcome to code jam
//   [ Created     ]  09/03/09 10:56:56 CST
//   [ Author      ]  Jiunru Yang , yangjiunru [at] gmail.com, NTUEE
// =====================================================================================

#include <iostream>
#include <vector>

using namespace std;

string getStr()
{
   string ret;
   char c;
   do {
      scanf("%c", &c);
   } while (c == '\n' || c == '\r');
   do {
      ret += c;
      if (scanf("%c", &c) != 1)
         break;
   } while (c != '\n' && c != '\r');
   return ret;
}

void run(unsigned caseNo)
{
   string strIn = getStr();
   string tar = "welcome to code jam";
   vector<vector<unsigned> > dp;
   dp.resize(strIn.length() + 1);
   for (unsigned i = 0; i < dp.size(); ++i) {
      dp[i].resize(19, 0);
   }
   dp[0][0] = 1;
   unsigned ans = 0;
   for (unsigned pos = 0; pos < strIn.length(); ++pos) {
      for (unsigned i = 1; i <= 18; ++i) {
         if (strIn[pos] != tar[i-1])
            continue;
         for (unsigned pp = 0; pp <= pos; ++pp)
            dp[pos+1][i] += dp[pp][i-1];
         dp[pos+1][i] %= 10000;
      }
      ans += dp[pos+1][18];
      ans %= 10000;
   }
   cout << "Case #" << caseNo << ": ";
   if (ans < 1000)
      cout << '0';
   if (ans < 100)
      cout << '0';
   if (ans < 10)
      cout << '0';
   cout << ans << endl;
}

int main()
{
   unsigned T;
   cin >> T;
   for (unsigned i = 1; i <= T; ++i)
      run(i);
   return 0;
}
