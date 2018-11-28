#include <iostream>
#include <set>
#include <vector>

using namespace std;
typedef multiset<int> IntSet;
typedef vector<int> IntVect;

const char nl = '\n';

inline int read_time()
{
   char ch;
   int h, m;
   cin >> h >> ch >> m;
   return 60*h + m;
}

int main()
{
   int N, T, NA, NB;

   cin >> N;
   for ( int m = 1; m <= N; m++ ) {
      IntSet AS, BS;
      cin >> T >> NA >> NB;
      IntVect AT(NA), BT(NB);
      for ( int i = 0; i < NA; i++ ) {
         AS.insert(read_time());
         AT[i] = read_time();
      }
      for ( int i = 0; i < NB; i++ ) {
         BS.insert(read_time());
         BT[i] = read_time();
      }
      for ( int i = 0; i < NA; i++ ) {
         IntSet::iterator it = BS.lower_bound(AT[i] + T);
         if ( it != BS.end() )
            BS.erase(it);
      }
      for ( int i = 0; i < NB; i++ ) {
         IntSet::iterator it = AS.lower_bound(BT[i] + T);
         if ( it != AS.end() )
            AS.erase(it);
      }
      cout << "Case #" << m << ": " << AS.size() << ' ' << BS.size() << nl;
   }
   return 0;
}
