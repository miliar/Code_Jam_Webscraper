// ============================================================================
//   [ Filename    ]  main.cpp
//   [ Description ]  
//   [ Created     ]  西元2010年06月05日 22時26分42秒 CST
//   [ Author      ]  Jiunru Yang, yangjiunru[at]gmail.com, LaDS3, GIEE, NTU
// ============================================================================

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

class Sol
{
   public:
   void read()
   {
      cin >> _p;
      _m.resize(1 << _p);
      for (int i = 0; i < (1 << _p); ++i)
         cin >> _m[i];
      for (int i = 0; i < _p; ++i) {
         _price.push_back(vector<int>((1 << (_p - i - 1)), 0));
         for (int j = 0; j < _price[i].size(); ++j)
            cin >> _price[i][j];
      }
   }
   void formulate(ostream& os)
   {
      os << "min: 0";
      for (int i = 0; i < _p; ++i) {
         for (int j = 0; j < _price[i].size(); ++j) {
            if (_price[i][j] == 0) continue;
            if (_price[i][j] > 0)
               os << " + ";
            os << _price[i][j];
            os << " v_" << i << "_" << j;
         }
      }
      os << ";\n";
      int cnt = 0;
      for (int i = 0; i < (1 << _p); ++i) {
         os << "r" << (cnt++) << ": 0";
         for (int j = 0; j < _p; ++j) {
            os << "+v_" << j << "_" << (i >> (j+1));
         }
         os << " >= " << (_p - _m[i]) << ";\n";
      }
      for (int i = 0; i < _p; ++i)
         for (int j = 0; j < _price[i].size(); ++j)
            os << "bin v_" << i << "_" << j << ";\n";
   }
   void solve(int caseNo)
   {
      read();
      ofstream os("tmp.lp", ios::out);
      formulate(os);
      os.close();
      cout << "Case #" << caseNo << ": " << lp() << endl;
   }
   int lp()
   {
      system("lp_solve -wfmps tmp.mps -parse_only < tmp.lp");
      system("cbc tmp.mps -solve -solution tmp.model >/dev/null");
      ifstream infile("tmp.model", ios::in);
      string a;
      infile >> a;
      infile >> a;
      infile >> a;
      infile >> a;
      int r;
      infile >> r;
      return r;
   }
   int _p;
   vector<int> _m;
   vector<vector<int> > _price;
};

int main()
{
   int T;
   cin >> T;
   for (int t = 1; t <= T; ++t) {
      Sol s;
      s.solve(t);
   }
   return 0;
}
