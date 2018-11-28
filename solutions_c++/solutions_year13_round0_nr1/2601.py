#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define X first
#define Y second

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename T> T abs(T a) { return a < 0 ? -a : a; }
template<typename T> T sqr(T a) { return a*a; }

const int INF = (int)1e9;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 20;
const int n = 4;

const int dx[] = {0, 1, 1,  1};
const int dy[] = {1, 0, 1, -1};

char f[N][N];

int main(){
    #ifdef ssu1
        freopen("input.txt", "rt", stdin);
        //freopen("output.txt", "wt", stdout);
    #endif

    int tests;
    cin >> tests;
    
    forn(test, tests){
        gets(f[0]);
        forn(i, n)
            gets(f[i]);
            
        bool hasEmpty = false;
        bool xWon = false;
        bool oWon = false;
         
        forn(i, n)
            forn(j, n){
                if(f[i][j] == '.')
                    hasEmpty = true;
                    
                forn(k, 4){
                    bool hasX = false;
                    bool hasO = false;
                    bool hasE = false;
                    
                    pt cur(i, j);
                    forn(q, 4){
                        if( ! (0 <= cur.X && cur.X < n && 0 <= cur.Y && cur.Y < n)){
                            hasE = true;
                            break;
                        }    
                        
                        if(f[cur.X][cur.Y] == 'X')
                            hasX = true;
                        if(f[cur.X][cur.Y] == 'O')
                            hasO = true;
                        if(f[cur.X][cur.Y] == '.')
                            hasE = true;
                            
                        cur.X += dx[k];
                        cur.Y += dy[k];
                    }
                    
                    if(hasE)
                        continue;
                    if(hasX && !hasO){
                        xWon = true;
                        break;
                    }
                    if(hasO && !hasX){
                        oWon = true;
                        break;
                    }
                }
                    
            }
            
        printf("Case #%d: ", test + 1);
            
        if(xWon){
            puts("X won");
            continue;
        }
        
        if(oWon){
            puts("O won");
            continue;
        }
        
        puts(hasEmpty ? "Game has not completed" : "Draw");
    }
    
    return 0;
}
