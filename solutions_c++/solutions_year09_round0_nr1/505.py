#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <cstdlib>
#include <set>
#include <map>

#define VI vector<int>
#define VS vector<string>
#define VVI vector< VI > 
#define pb push_back
#define mp make_pair
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORC(it,kont) for(__typeof((kont).begin()) it = (kont).begin(); it != (kont).end(); ++it )

using namespace std;

VS dict;
int a[15][26];
int main()
    {
    int TC;
    int L;
    int D;
    cin >> L >> D >> TC;
    string s;
    FOR(i,0,D) { cin >> s; dict.pb( s );  }  
    FOR( tc, 0 , TC )
       {
       string p;
       cin >> p;
       
       VS b;
       while( p.size() > 0 && p.find( ')' ) != p.size() ) 
          {
          if ( p[0] != '(' ) 
             {  
             string bla; 
             bla += p[0]; 
             b.pb( bla ) ; 
             p = p.substr( 1 ) ;
             } 
          else 
               { 
               string bla = string( p.begin() + 1, p.begin() + p.find(')') ); 
             //  cout << bla << endl;
               b.pb( bla ) ; 
               p = string( p.begin() + p.find(')') + 1, p.end());  
     //          cout << p << endl;
               } 
          }
     //  cout << "ovdje" << endl;
       while( p.size() > 0 ) 
          {
          string bla; bla += p[0]; b.pb( bla ) ; p = p.substr( 1 ) ;
          }
     //  cout << "ovdje" << endl;
       memset( a, 0 , sizeof( a ) );
       FOR( i , 0 , b.size()) 
          {
          FOR( j, 0 , b[i].size()) 
              a[i][b[i][j] - 'a'] = 1;
          }
       int sol = 0;
       FOR( i,0 ,dict.size() ) 
          {
          bool ok = 1;
          FOR( j, 0, dict[i].size()) 
             if ( a[j][dict[i][j] - 'a']  == 0 ) ok = 0;
          sol += ok;     
          }
       
       cout << "Case #" << tc + 1<< ": "<< sol << endl;      
       }      
    //system("pause");
    return 0;
    }
