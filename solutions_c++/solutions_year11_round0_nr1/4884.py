#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
using namespace std ;

#define FOREACH(it,c) for( __typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++) 
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) FOR(i,0,(n)-1)
#define DEP(i,n) DOW(i,(n)-1,0)
#define all(a) (a).begin() , (a).end()

typedef vector<int> VI ;
typedef vector<string> VS ;
template<class T> inline int size(const T&c) { return c.size(); }  


int abs(int a){
    if (a >= 0) return a; else return -a;
}

int max2 (int a, int b) {
    if (a > b) return a; else return b;
}

int min2 (int a, int b) {
    if (a < b) return a; else return b;
}

int ntest , ans , n;
int Pos[110][2];
int res[110][2];

int main () 
{

    {
        string s;
        getline(cin,s);
        istringstream sin(s);
        sin >> ntest;
    }
    
    int test = 0, maxm = 101;

    
    while (test < ntest) {
          test++;
          
          string s;
          getline(cin,s);
          REP(i,size(s)) {
              if (s[i] == 'O') s[i] = '0';
              if (s[i] == 'B') s[i] = '1';
          }
    
          istringstream sin(s);
          
          sin >> n;
          REP(i,n) {
              sin >> Pos[i][0] >> Pos[i][1];
          }
          
          //init
          int now = 1;          
          
          // tinh 0                 
          for(int i=1;i <= 100; i++) {
             if (i <= Pos[0][1]+1) res[i][0] = Pos[0][1]; 
             else res[i][0] = i;
//             cout << res[i][0] << endl;
          }
           
           
          FOR(k,1,n-1) {
              int pre = 1 - now;
              
              if (Pos[k][0] == Pos[k-1][0]){                            
                   for(int i = 1; i <= 100; i++ ) {                               
                       res[i][now] = 1000000000;        
                       for(int j = 1; j <= 100; j++ ){
                           res[i][now] = min2(res[i][now],res[j][pre] + max2((abs(Pos[k][1] - Pos[k-1][1]) + 1), abs(i-j)));
                       }
                   }
              } else {
                   FOR(i,1,100) {
                       res[i][now] = 1000000000;        
                       FOR(j,1,100)
                           res[i][now] = min2(res[i][now],res[j][pre] + max2(abs(Pos[k][1] - j) + 1, abs(i-Pos[k-1][1])));
                   }                     
              }
              
              now = pre;     
          }
          
          ans = 1000000000;
          FOR(i,1,100) {
              if (res[i][1-now] < ans) ans =  res[i][1-now];
          }
          cout << "Case #" << test<< ": " << ans << endl;
    }

    return 0;
}
