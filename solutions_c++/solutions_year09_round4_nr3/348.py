// =====================================================================================
//   [ Filename    ]  pcsmall.cpp
//   [ Description ]  
//   [ Created     ]  09/27/2009 12:39:21 AM CST
//   [ Author      ]  Jiunru Yang , yangjiunru [at] gmail.com, NTUEE
// =====================================================================================

#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

class GT
{
public:
   bool okay()
   {
      a.resize(n);
      return rec(0,0);
   }

   bool rec(int pos, int ng)
   {
      if (pos == n)
         return true;
      for (int i = 0; i < ng; ++i) {
         bool ok = true;
         for (int j = 0; j < pos; ++j)
            if (a[j] == i && adj[pos][j] == false)
               ok = false;
         if (!ok)
            continue;
         a[pos] = i;
         if (rec(pos+1, ng))
            return true;
      }
      if (ng < g) {
         a[pos] = ng;
         if (rec(pos+1, ng+1))
            return true;
      }
      return false;
   }

   int n, g;
   bool adj[16][16];
   vector<int> a;
};

class Sol
{
public:
   void read()
   {
      cin >> _n >> _k;
      _price.resize(_n, vector<int>(_k));
      for (int i = 0; i < _n; ++i)
         for (int j = 0; j < _k; ++j)
            cin >> _price[i][j];
      makeAdj();
   }

   void makeAdj()
   {
      _adj.resize(_n, vector<bool>(_k));
      for (int i = 0; i < _n; ++i)
         for (int j = 0; j < _n; ++j) {
            _adj[i][j] = true;
            for (int k = 1; k < _k; ++k) {
               if (_price[i][k-1] == _price[j][k-1])
                  _adj[i][j] = false;
               if (_price[i][k] == _price[j][k])
                  _adj[i][j] = false;
               if (_price[i][k-1] < _price[j][k-1] && _price[i][k] > _price[j][k])
                  _adj[i][j] = false;
               if (_price[i][k-1] > _price[j][k-1] && _price[i][k] < _price[j][k])
                  _adj[i][j] = false;
            }
         }
   }

   void dumpAdj()
   {
      for (int i = 0; i < _n; ++i) {
         for (int j = 0; j < _n; ++j)
            cout << _adj[i][j] << " ";
         cout << endl;
      }
   }

   unsigned ans()
   {
      GT gt;
//      gt.adj = _adj;
      for (int i = 0; i < _n; ++i)
         for (int j = 0; j < _n; ++j)
            gt.adj[i][j] = _adj[i][j];
      gt.n = _n;
      for (gt.g = 1; gt.g <= _n; ++gt.g)
         if (gt.okay())
            return gt.g;
      assert(0);
   }

   int _n, _k;
   vector<vector<int> > _price;
   vector<vector<bool> > _adj;
};

int main()
{
   int T;
   cin >> T;
   for (int t = 1; t <= T; ++t) {
      Sol s;
      s.read();
      //s.dumpAdj();
      cout << "Case #" << t << ": " << s.ans() << endl;
   }
   return 0;
}
