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

char tab[50][50];
int R, C;

bool recu(int a, int b)
{
     if (tab[a][b] != '#')
        return true;
     
     tab[a][b] = '/';
     
     if (b >= C)
      {  return false; }
     if (a >= R)
     {return false;}
     if ((tab[a][b+1] != '#') || (tab[a+1][b+1] != '#') || (tab[a+1][b] != '#'))
        {return false;}
        
     tab[a][b+1] = '\\';
     tab[a+1][b+1] = '/';
     tab[a+1][b] = '\\';
     return true;
}

int main()
{
    int T;
    cin >> T;

    FORE(i, 1, T)
    {
        cin >> R >> C;
        
        bool possible = true;
        int nbOpen = 0;
        
        REP(j, R)
            REP(k, C)
               cin >> tab[j][k];

        REP(j, R)
            REP(k, C)
               if (recu(j, k) == false)
                   possible = false;
         cout<<"Case #"<<i<<": "<<endl;               
            if (possible) {
                  REP(j, R)
                  {              
                  REP(k, C)
                  {
                  cout<<tab[j][k];             
                  }
                  cout<<endl;
                  }
                          }else {
            cout<<"Impossible"<<endl;               
                    }                                                     
        }
    return 0;
}
