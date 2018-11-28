#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
   int L, D, N;
   cin >> L >> D >> N;
   vector<vector<int> > d(D, vector<int>(L, 0));
   for (int i=0; i<D; ++i) {
      string s;
      cin >> s;
      for (int j=0; j<L; ++j)
         d[i][j] = (1<<(s[j]-'a'));
   }
   for (int t=0; t<N; ++t) {
      cout << "Case #" << t+1 << ": ";
      string s;
      cin >> s;
      vector<int> v(L, 0);
      int pos = 0;
      for (int i=0; i<s.size(); ++i) {
         if (s[i] != '(')
            v[pos] = (1<<(s[i]-'a'));
         else
            while (s[++i] != ')')
               v[pos] |= (1<<(s[i]-'a'));
         ++pos;
      }
      int sol = 0;
      for (int i=0; i<D; ++i) {
         bool bo = true;
         for (int j=0; j<L and bo; ++j)
            if ((d[i][j] & v[j]) == 0)
               bo = false;
         if (bo)
            ++sol;
      }
      cout << sol << endl;
   }
}