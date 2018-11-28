// ============================================================================
//   [ Filename    ]  pcsmall.cpp
//   [ Description ]  
//   [ Created     ]  西元2010年06月05日 22時50分37秒 CST
//   [ Author      ]  Jiunru Yang, yangjiunru[at]gmail.com, LaDS3, GIEE, NTU
// ============================================================================

#include <iostream>
#include <vector>

using namespace std;

class Sol
{
public:
   void read()
   {
      _c.clear();
      _c.resize(110, vector<bool>(110, false));
      int r;
      cin >> r;
      for (int i = 0; i < r; ++i) {
         int x1, y1, x2, y2;
         cin >> x1 >> y1 >> x2 >> y2;
         for (int x = x1-1; x < x2; ++x)
            for (int y = y1-1; y < y2; ++y)
               _c[x][y] = true;
      }
   }
   bool check()
   {
      bool r = true;
      for (int i = 0; i < _c.size(); ++i)
         for (int j = 0; j < _c[i].size(); ++j)
            if (_c[i][j]) {
               r = false;
               break;
            }
      return r;
   }
   void step()
   {
      _nc.clear();
      _nc.resize(110, vector<bool>(110, false));
      _nc[0][0] = false;
      for (int i = 1; i < 110; ++i) {
         if (_c[0][i-1] == false)
            _nc[0][i] = false;
         else
            _nc[0][i] = _c[0][i];
         if (_c[i-1][0] == false)
            _nc[i][0] = false;
         else
            _nc[i][0] = _c[i][0];
      }
      for (int i = 1; i < 110; ++i)
         for (int j = 1; j < 110; ++j) {
            if (_c[i-1][j] == false && _c[i][j-1] == false)
               _nc[i][j] = false;
            else if (_c[i-1][j] == true && _c[i][j-1] == true)
               _nc[i][j] = true;
            else
               _nc[i][j] = _c[i][j];
         }
      _c = _nc;
   }
   void solve(int caseNo)
   {
      read();
      int ans = 0;
      while (!check()) {
         ++ans;
         step();
      }
      cout << "Case #" << caseNo << ": " << ans << endl;
   }
   vector<vector<bool> > _c;
   vector<vector<bool> > _nc;
};

int main()
{
   int T;
   cin >> T;
   for (int t =1 ;t  <= T; ++t) {
      Sol s;
      s.solve(t);
   }
   return 0;
}
