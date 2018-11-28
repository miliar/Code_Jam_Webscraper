//0x
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
using namespace std;

#define CLR(a, n) memset((a), n, sizeof(a))
#define arlen(x) sizeof x / sizeof x[0]
#define len(a)  int((a).size())
#define all(x) (x).begin(), (x).end()
#define rall(c) (c).rbegin(), (c).rend()
#define has(s, val) (find(all(s), val)!=(s).end())
#define EXIST(s,e)  ((s).find(e)!=(s).end())
#define REMOVE(c,val) (c).erase(remove((c).begin(),(c).end(),(val)),(c).end())
#define rep(i,n)  REP(i,0,n)
#define REP(i,a,b) for(int i=(a);i<(b);++i)
#define SORT(c) sort(all(c))
#define pb push_back
#define mp make_pair
const int INF=1<<29;
const double EPS=1e-9;
typedef std::vector<int> VI;
typedef std::vector<VI> VVI;
typedef std::vector<string> VS;
typedef long long ll;

typedef pair<int,int> ii;
#define cons(x,y) make_pair((x),(y))
#define car(x) ((x).first)
#define cdr(x) ((x).second)
#define caar(x) (x).first.first
#define cdar(x) (x).first.second
#define cadr(x) (x).second.first
#define cddr(x) (x).second.second

//BEGINCUT
// (yas/expand-link "topcoder")
// (yas/expand-link "timer")
// (yas/expand-link "math")
// (yas/expand-link "tco2")
// (yas/expand-link "split")
// (yas/expand-link "join")
// (yas/expand-link "bigint")
// (yas/expand-link "pair_opr")
// (yas/expand-link "conversion")
// (yas/expand-link "myalgorithm")
#include <cout.hpp>
//ENDCUT

int dx[] = {1, 1, 0};
int dy[] = {0, 1, 1};


int T;
//NODEBUG
int main() {
    cin >> T;
    int r,c;
    rep(t, T){
        cin >> r >> c;
        vector<vector<char> > board(r, vector<char>(c));
        
        int blues=0;
        rep(i, r){
            rep(j, c){
                cin >> board[i][j];
                if(board[i][j]=='#') blues++;
            }
        }
        
        // => board
        bool impos=true;
        if(blues>0 && blues%2!=0) goto end;
        if(blues==0){
            impos=false;
            goto end;
        }
        

        //greedy
        rep(i, r){
            rep(j, c){
                if(board[i][j]=='#'){
                    // => i | j
                    bool ok=true;
                    rep(k, 3){
                        // => i+dy[k] | j+dx[k] | r | c
                        if(i+dy[k] >= r || j+dx[k] >= c || board[i+dy[k]][j+dx[k]]!='#'){
                            ok=false;
                            break;
                        }
                    }
                    
                    if(ok){
                        board[i][j]='/';
                        board[i][j+1]='\\';
                        board[i+1][j]='\\';
                        board[i+1][j+1]='/';
                    }

                    // => board
                }
            }
        }
        
        impos=false;
        rep(i, r){
            rep(j, c){
                if(board[i][j]=='#'){
                    impos=true;
                    break;
                }
            }
        }
        
      end:;
        
        printf("Case #%d: \n", t+1);
        if(impos){
            puts("Impossible");
        }else{
            rep(i, r){
                rep(j, c){
                    cout << board[i][j];
                }
                cout << endl;
            }
        }
    }
    return 0;
}
