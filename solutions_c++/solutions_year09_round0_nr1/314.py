// =====================================================================================
//   [ Filename    ]  main.cpp
//   [ Description ]  Alien Language
//   [ Created     ]  09/03/09 12:17:06 CST
//   [ Author      ]  Jiunru Yang , yangjiunru [at] gmail.com, NTUEE
// =====================================================================================

#include <iostream>
#include <string>
#include <vector>
#include <cassert>

using namespace std;

class MyStr
{
   public:
      MyStr(const string& s): _s(s), _p(0) { }
      string get() {
         string ret;
         if (_s[_p] != '(') {
            ret += _s[_p++];
            return ret;
         }
         ++_p;
         while (_s[_p] != ')')
            ret += _s[_p++];
         ++_p;
         return ret;
      }
   private:
      string _s;
      unsigned _p;
};

bool check(string d, string r)
{
   MyStr mystr(r);
   for (unsigned i = 0, n = d.length(); i < n; ++i) {
      string s = mystr.get();
      if (s.find(d[i]) == string::npos)
         return false;
   }
   return true;
}

int main()
{
   int L, D, N;
   cin >> L >> D >> N;
   vector<string> dict(D);
   for (int i = 0; i < D; ++i) {
      cin >> dict[i];
      assert(dict[i].length() == L);
   }
   for (int i = 0; i < N; ++i) {
      int ans = 0;
      string r;
      cin >> r;
      for (int j = 0; j < D; ++j)
         if (check(dict[j], r))
            ++ans;
      cout << "Case #" << (i+1) << ": ";
      cout << ans << endl;
   }
   return 0;
}
