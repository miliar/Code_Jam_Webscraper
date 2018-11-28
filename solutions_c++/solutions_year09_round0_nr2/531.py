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

int moves[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int w,h;
VVI vis; 
VS sol; 
char mark;

bool ok( int x, int y)
{
 if ( x < 0 || x >= h ) return 0;
 if ( y < 0 || y >= w ) return 0;
 return 1;     
}

bool sink ( int x, int y ) 
{
 bool ok2 = 1;
 FOR(k,0,4)
    {
    int nx = x + moves[k][0],ny = y + moves[k][1] ; 
    if ( ok( nx, ny ) && vis[nx][ny] < vis[x][y] ) ok2 = 0;       
    }     
 return ok2;
}

char go ( int x, int y ) 
   {
   if ( sol[x][y] != ' ' ) return sol[x][y]; 
  // cout << x << " " << y << endl;
   if ( sink( x, y ) ) { sol[x][y] = mark; ++mark; return sol[x][y]; } 
   
   int visina = vis[x][y]; int smjer = -1;
   FOR(k,0,4)
    {
    int nx = x + moves[k][0],ny = y + moves[k][1] ; 
    if ( ok( nx, ny ) && vis[nx][ny] < visina ) { smjer = k; visina = vis[nx][ny]; } 
    }    
  // cout << visina << " " << smjer << endl;
   sol[x][y] = go( x + moves[smjer][0], y + moves[smjer][1] ) ;
   return sol[x][y];
   }


int main()
    {
    int TC;
    cin >> TC;
    FOR( tc, 0 , TC )
       {
       vis.clear(); sol.clear();
       cin >> h >> w; vis.resize( h ) ;
       int bla;
       FOR( i, 0 , h ) FOR( j, 0 , w ) { cin >> bla; vis[i].pb( bla ) ; } 
       
       sol.resize( h ) ; 
       FOR( i, 0, h ) sol[i] = string( w, ' ' ) ; 
       
       mark = 'a';
       
       FOR( i, 0 ,h ) FOR( j,0 ,w ) go ( i, j ) ;
       
       cout << "Case #" << tc + 1<< ":"<< endl;      
       FOR( i, 0, h )
         FOR( j, 0 , w )
           {
           if ( j == w-1) cout << sol[i][j] << endl;
           else cout << sol[i][j]<< " ";      
           }
       }      
    //system("pause");
    return 0;
    }
