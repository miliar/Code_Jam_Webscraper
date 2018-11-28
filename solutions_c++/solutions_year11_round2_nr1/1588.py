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

struct {
       double nbWin,nbG;
       double OWP, OOWP, RPI;
       char tab[100];
       } team[100];
int mint[100];

int main()
{
    int T;
    cin >> T;

    FORE(i, 1, T)
    {
        int N;              
        cin >> N;
        
        REP(j, N)
        {
            team[j].nbWin = 0;
            team[j].nbG = 0;
            team[j].OWP = 0;
            team[j].OOWP = 0;
            team[j].RPI = 0;
            
            REP(k, N)
            {
               char c;
               cin >> c;
               team[j].tab[k] = c;
               if (c != '.')
               {
                     if (c == '1')
                         team[j].nbWin++;
                     team[j].nbG++;
               }
            }
            //on calcule déjà le premier membre
            team[j].RPI = 0.25 * (team[j].nbWin / team[j].nbG);
//            cout<<"team "<<j<<" wp:"<<(team[j].nbWin / team[j].nbG)<<endl;
            
            //ensuite 
            REP(k, N)
            {
                 if (team[j].tab[k] != '.')
                 {
                    //une equipe avec WP déjà calculé ?
                    if (k < j)
                    {
                        //on récupère son opp winning pourcentage  
                        //on l'ajoute chez nous
                        double oppWP = team[k].nbWin;
                        if (team[j].tab[k] == '0')
                            oppWP -= 1;
                         oppWP /=  (team[k].nbG - 1);
                         team[j].OWP += oppWP;
                         
                         //on ajoute le notre au sien 
                         double myoppWP = team[j].nbWin;
                        if (team[j].tab[k] == '1')
                            myoppWP -= 1;
                        myoppWP /= (team[j].nbG - 1);

                        team[k].OWP += myoppWP;                         
                     }
               }
          }
        }
        
        //on reparcourt toutes les équipes pour compter la moyenne et l'ajouter
        REP(j, N)
        {
               team[j].OWP /= team[j].nbG;
               team[j].RPI += 0.5*team[j].OWP;
               
//            cout<<"team "<<j<<" wp:"<<(team[j].OWP)<<endl;
               //ensuite 
            REP(k, N)
            {
                 if (team[j].tab[k] != '.')
                 {
                    //une equipe avec WP déjà calculé ?
                    if (k < j)
                    {
                          team[j].OOWP += team[k].OWP;
                          team[k].OOWP += team[j].OWP;
                    }
                 }
            }
        }

        cout<<"Case #"<<i<<": "<<endl;               
        //on reparcourt toutes les équipes pour compter la moyenne et l'ajouter
        REP(j, N)
        {
               team[j].OOWP /= team[j].nbG;
               team[j].RPI += 0.25*team[j].OOWP;
           // cout<<"team "<<j<<" oowp:"<<(team[j].OOWP)<<endl;
                cout<<std::setprecision(10)<<team[j].RPI<<endl;
        }
    }
    return 0;
}
