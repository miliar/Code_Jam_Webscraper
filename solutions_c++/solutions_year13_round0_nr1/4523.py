//#pragma comment(linker, "/STACK:32777216")
#include <iostream> 
#include <vector>
#include <set>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>
#include <map>
#include <queue>
#include <memory.h>
#include <fstream>
using namespace std;

#define FOR(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define RFOR(i,a,b) for(int (i)=(a)-1;(i)>=(b);--(i))
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define PII pair<int,int>
#define CLEAR(a) memset((a),0,sizeof((a)))
#define X first
#define Y second
#define sz(a) (int)(a).size()

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> VI;

const double pi=3.141592653589793;
const int INF=1000000000;
const ll mod=1000000007;


int main(){
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
   int t;
   cin >> t;
   int k , x , y;
   FOR(tt,0,t){
              string s[4];
              FOR(i,0,4)
              cin >> s[i];
              cout << "Case #" << tt + 1 << ": ";
              FOR(i,0,4){
                         int x = 0;
                         int y = 0;
                         FOR(j,0,4){
                                    if (s[i][j] == 'X' || s[i][j] == 'T')
                                    ++x;
                                     if (s[i][j] == 'O' || s[i][j] == 'T')
                                    ++y;          
                         }
                         if (x == 4){
                               cout << "X won\n";
                              goto ex; 
                         }          
                         if (y == 4){
                               cout << "O won\n";
                              goto ex; 
                         }
              }
              FOR(j,0,4){
                         int x = 0;
                         int y = 0;
                         FOR(i,0,4){
                                    if (s[i][j] == 'X' || s[i][j] == 'T')
                                    ++x;
                                     if (s[i][j] == 'O' || s[i][j] == 'T')
                                    ++y;          
                         }
                         if (x == 4){
                               cout << "X won\n";
                              goto ex; 
                         }          
                         if (y == 4){
                               cout << "O won\n";
                              goto ex; 
                         }
              }
              
              
             x = 0;
            y = 0;
              FOR(i,0,4){
                        if (s[i][i] == 'X' || s[i][i] == 'T')
                        ++x;
                         if (s[i][i] == 'O' || s[i][i] == 'T')
                        ++y;  
                        }        
             if (x == 4){
                   cout << "X won\n";
                  goto ex; 
             }          
             if (y == 4){
                   cout << "O won\n";
                  goto ex; 
             }
          
          
          x = 0;
          y = 0;
              FOR(i,0,4){
                        if (s[i][3 - i] == 'X' || s[i][3 - i] == 'T')
                        ++x;
                         if (s[i][3 - i] == 'O' || s[i][3 - i] == 'T')
                        ++y;  
                        }        
             if (x == 4){
                   cout << "X won\n";
                  goto ex; 
             }          
             if (y == 4){
                   cout << "O won\n";
                  goto ex; 
             }
          
          k = 0;
          FOR(i,0,4)
          FOR(j,0,4)
                    if (s[i][j] == '.') 
                    ++k;
          if (k == 0)
          cout << "Draw\n";
          else cout << "Game has not completed\n";
          ex:    
          int a;
   }
    //system("pause");
	return 0;
}
