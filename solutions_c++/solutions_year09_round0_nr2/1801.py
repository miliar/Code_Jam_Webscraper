#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define S(X) ((int)(X).size())
#define FOR(I, N) for (int I=0; I<(int)N;++I)
#define FORI(N) FOR(i,N)
#define FORJ(N) FOR(j,N)
#define FORK(N) FOR(k,N)
#define FORN(NN) FOR(n, NN)
#define LOOP(N) FOR(__i__, N)

typedef long long LL;
typedef unsigned long long ULL;

const double eps = 1e-11;
const double pi=acos(-1.0);

template<class T> T gcd(T a, T b){ if (a<0) return gcd(-a,b); if (b<0)return gcd(a, -b); return (b==0)?a:gcd(b, a%b);}
int countbit(int n){return (n==0)?0:(1+countbit(n&(n-1)));}
int lowbit(int n){return (n^(n-1))&n;}
template<class T> string toString(T integer) { ostringstream os; os << integer; return os.str();}

#define foreach(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define P(a,b) make_pair((a),(b))
template<typename T, typename U> U cast(T arg){
    ostringstream oss;
    oss << arg;
    istringstream iss(oss.str());
    U rv;
    iss >> rv;
    return rv;
}

int arr[102][102];
int dir[102][102];
int rdir[102][102];
char mark[102][102];

int D[4][2] = {
    {0, -1},
    {-1, 0},
    {1, 0},
    {0, 1}
};

void flood(int x, int y, char c){
    if (mark[y][x] > 0)
        return;
    mark[y][x] = c;
    int dd;

    if (dir[y][x] >= 0) {
        dd = dir[y][x];
        flood(x + D[dd][0], y + D[dd][1], c);
    } 
        for (int i = 0; i < 4; ++ i){
            if (dir[y+D[i][1]][x+D[i][0]] == 3 - i){
                flood(x+D[i][0], y+D[i][1], c);
            }
        }
   
}

int main(int argc, char* argv[])
{
    freopen("B-large.in", "r", stdin);
     
    int T, H, W;
    cin >> T;
    
    FORN(T){
        cin >> H >> W;
        FORJ(H)FORK(W) mark[j+1][k+1] = -1, dir[j+1][k+1]=-1;
        FORI(W+2) arr[0][i] = 10000, dir[0][i]=-1, mark[0][i]= 1 ;
        FORI(H+2) arr[i][0] = 10000, dir[i][0]=-1, mark[i][0]= 1;
        FORI(W+2) arr[H+1][i] = 10000, dir[H+1][i]=-1, mark[H+1][i]= 1;
        FORI(H+2) arr[i][W+1] = 10000, dir[i][W+1]=-1, mark[i][W+1]= 1;
                         
      
        FORJ(H){
            FORK(W){
                int n;
                cin >> n;
                arr[j + 1][k + 1] = n;
            }
        }
        // 0 north, 1 west, 2 east, 3 south

        FORJ(H){
            FORK(W){
                int y = j + 1;
                int x = k + 1;
                int min = arr[y][x];
                int direction = -1;  
                for (int ii = 0; ii < 4; ++ ii){
                    if (arr[y + D[ii][1]][x + D[ii][0]] < min){
                        min = arr[y + D[ii][1]][x + D[ii][0]];
                        direction = ii; 
                    }
                }
                dir[y][x] = direction;
                //rdir[y + D[direction][1]][x + D[direction][0]] = 3 - direction;
                 
            }
        }
        
        char c = 'a';

        FORJ(H){
            FORK(W){
                int y = j + 1;
                int x = k + 1;
                if (mark[y][x] > 0)
                    continue;
                flood(x, y, c);
                c ++;
            }
        }

        printf("Case #%d:\n", n + 1);

        FORJ(H){
            FORK(W){
                cout << mark[j + 1][k + 1];
                if (k != W -1)
                    cout << ' ';
            }
            cout << '\n';
        }

    }

    return 0;
}
