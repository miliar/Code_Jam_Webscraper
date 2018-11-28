// =====================================================================================
//   [ Filename    ]  pc.cpp
//   [ Description ]  
//   [ Created     ]  09/13/2009 05:48:25 PM CST
//   [ Author      ]  Jiunru Yang , yangjiunru [at] gmail.com, NTUEE
// =====================================================================================

#include <iostream>
#include <map>
#include <vector>

using namespace std;

class Solver
{
   public:

      void read()
      {
         cin >> P >> Q;
         toRelease.resize(Q);
         for (unsigned i = 0; i < Q; ++i)
            cin >> toRelease[i];
      }

      unsigned cal(unsigned st, unsigned ed)
      {
         typeof(cache.begin()) it = cache.find(make_pair(st,ed));
         if (it != cache.end())
            return it->second;
         unsigned ret = ed - st;
         bool nbet = true;
         for (unsigned i = 0; i < toRelease.size(); ++i) {
            unsigned tr = toRelease[i];
            if (tr >= st && tr <= ed) {
               nbet = false;
               break;
            }
         }
         if (nbet) {
            ret = 0;
            cache[make_pair(st,ed)] = ret;
            return ret;
         }

         unsigned mn = ~0u;

         for (unsigned i = 0; i < toRelease.size(); ++i) {
            unsigned tr = toRelease[i];
            if (tr < st || tr > ed) continue;
            unsigned rf, rs;
            if (tr == st)
               rf = 0;
            else
               rf = cal(st, tr-1);

            if (tr == ed)
               rs = 0;
            else
               rs = cal(tr+1, ed);

            if (rf + rs < mn)
               mn = rf + rs;
         }

         ret += mn;
         cache[make_pair(st,ed)] = ret;
         return ret;
      }

      void solve(int caseNo)
      {
         read();
         cout << "Case #" << caseNo << ": " << cal(1, P) << endl;
      }


      unsigned P, Q;
      vector<unsigned> toRelease;
      map<pair<unsigned,unsigned>,unsigned> cache;
};

int main()
{
   int T;
   cin >> T;
   for (int t = 1; t <= T; ++t) {
      Solver s;
      s.solve(t);
   }
   return 0;
}
