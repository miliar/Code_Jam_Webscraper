#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <fstream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <iomanip>
using namespace std;

/* GCJ template part 02 -- Common macro definitions */
#define FOR(i, a, b)    for(int i = int(a); i < int(b); ++i)
#define REP(i, n)       FOR(i, 0, n)
#define FORE(i, a, b)   for(int i = int(a); i <= int(b); ++i)
#define REPE(i, n)      FORE(i, 0, n)
#define FORD(i, a, b)   for(int i = int(b) - 1; i >= int(a); --i)
#define REPD(i, n)      FORD(i, 0, n)
#define FORDE(i, a, b)  for(int i = int(b); i >= int(a); --i)
#define REPDE(i, n)     FORDE(i, 0, n)
#define IT(c)           __typeof((c).begin())
#define FORIT(i, c)     for(IT(c) i = (c).begin(); i != (c).end(); ++i)
#define SZ(c)           (int((c).size()))
#define ALL(c)          (c).begin(), (c).end()
#define SET(m, v)       memset((m), (v), sizeof(m))
#define REVERSE(c)      reverse(ALL(c))
#define SORT(c)         sort(ALL(c))
#define UNIQ(c)         SORT(c), (c).erase(unique(ALL(c)), (c).end())
#define PB              push_back
#define MP              make_pair
#define BIT(x)          (1<<(x))
#define MAPRET(m, x)    { IT(m) _ = m.find(x); if(_ != m.end()) return _->second; }

/* GCJ template part 03 -- Common type definitions */
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<VI> VVI;
typedef vector<VLL> VVLL;
typedef vector<VS> VVS;
typedef vector<VD> VVD;

// Tests if string a starts with string b
inline bool startswith(const string &a, const string &b) {
    return a.size() >= b.size() && a.compare(0, b.size(), b) == 0;
}

// Tests if string a end with string b
inline bool endswith(const string &a, const string &b) {
    return a.size() >= b.size() && a.compare(a.size() - b.size(), b.size(), b) == 0;
}

ULL L, t, N, C;
ULL tabA[1000];
ULL bestrep;

ULL minf(ULL a, ULL b){if (a<b)return a;return b;}

bool recu(int a, ULL time, int b)
{
     //cout << "recu " << a <<" "<<time<<" " << b<<endl;
      //we travel from a to a+1
      if (a == N)
      {
        if (bestrep == 0) bestrep = time;
        bestrep = minf(bestrep, time);
        return true;
      }
      ULL timeToGetNext = tabA[a%C];
      
      //on test en y allant comme ça
      recu(a+1, time + timeToGetNext, b);
      
      if (b > 0)
      {
            //on test en construisant un accelerateur     
            if (time >= t)
            {
               recu(a+1, time + timeToGetNext/2, b-1);
            }
            else
            {
                int diff = t - time;
                if (diff < timeToGetNext)
                   recu(a+1, time + diff + (timeToGetNext-diff)/2, b-1);   
            }
      }
      return true;
}

int main()
{
    int T;
    cin >> T;

    FORE(i, 1, T)
    {
        cin >> L >> t >> N >> C;
        
        FORE(j, 0, C-1)
        {
                cin >> tabA[j];
                tabA[j]*=2;
        }
        bestrep = 0;
        recu(0,0,L);
         cout<<"Case #"<<i<<": "<<bestrep<<endl;               
    }
    return 0;
}
