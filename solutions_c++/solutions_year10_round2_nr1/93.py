#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <cmath>
#include <vector>

using namespace std;

#define VI vector<int>
#define VS vector<string>
#define pb push_back
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORC(it,kont) for(__typeof((kont).begin()) it=(kont).begin();it!=(kont).end();++it)
#define VVI vector< vector<int> >

int test_cases;

int N, M;

struct node
   {
   string s;
   int razina;
   int tata;
   map<string, int> djeca;
   };

vector<node> drvo;

VS split( string s ) 
   {
   int pocetak = 1;
   int p = 0;
   VS sol;
   for( p = 1 ; p < s.size(); ++p ) 
        {
        if ( s[p] == '/' ) { sol.pb( s.substr(pocetak,p-pocetak)); pocetak = p + 1; }
        }
   sol.pb( s.substr( pocetak, (int)(s.size()) - pocetak ) ) ;
   return sol; 
   }

void insert( VS s ) 
     {
     int p = 0;
     FOR(i,0,s.size() ) 
          {
          if ( drvo[p].djeca.count( s[i] ) ) 
             {
             p = drvo[p].djeca[s[i]];           
             }
          else
             {
             drvo.resize(drvo.size() + 1);
             drvo.back().tata = p ;
             drvo.back().razina = drvo[p].razina + 1;
             drvo.back().s = s[i];
             drvo[p].djeca[s[i]] = (int)(drvo.size()) - 1;
             p = (int)(drvo.size()) - 1;
             }    
          }
     return ;
     }


int main()
    {
    cin >> test_cases;
    for( int test_nmbr = 0; test_nmbr < test_cases; ++test_nmbr ) 
         {
         drvo.clear();
         drvo.resize( 1 ) ;
         drvo[0].razina = 0;
         drvo[0].tata = -1;
         cin >> N >> M;
         FOR( i, 0, N ) 
              {
              string s;
              cin >> s;
              VS a = split ( s ) ;
              //FOR( j,0,a.size() ) cerr << a[j] << " ";
              //cerr << endl;
              insert( a );
              //cerr << "1 " << " " << drvo.size() << endl;
              }
         int a = drvo.size();
         FOR( i,0,M )
              {
              string s;
              cin >> s;
              VS a = split ( s ) ;
              //FOR( j,0,a.size() ) cerr << a[j] << " ";
              //cerr << endl;
              insert( a );
              //cerr << "2 " << " " << drvo.size() << endl;
              }
         int b = drvo.size();
         
         int sol = b - a;
         
         cout << "Case #" << test_nmbr + 1 << ": " << sol << endl;
         }
    //system( "pause" ) ;     
    return 0;
    }
