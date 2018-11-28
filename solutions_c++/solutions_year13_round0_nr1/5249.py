#include<cstdio>
#include<iostream>
#include<cassert>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<list>
#include<queue>
#include<set>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) __typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define MP make_pair
#define PB push_back
#define ST first
#define ND second

const int BSIZE = 5;
const int MAXT = 1010;
char board[BSIZE][BSIZE];

bool is_ok(int play, char t){
    if (play == 0){
        return t == 'T' || t == 'X';
    }
    return t == 'T' || t == 'O';
}

void readb(){
    REP(i,4){
        REP(j,4){
            cin>>board[i][j];
        }
    }
}

int check(){
    //czy x wygral
    REP(player,2){
        REP(i,4){
            bool w = true;
            REP(j,4){
                w = w && is_ok(player, board[i][j]);
            }
            if (w){
                return player+1;
            }
        }
        REP(i,4){
            bool w = true;
            REP(j,4){
                w = w && is_ok(player, board[j][i]);
            }
            if (w){
                return player+1;
            }
        }
        bool w = true;
        REP(i,4){
            w = w && is_ok(player,board[i][i]);
        }
        if (w) {
            return player+1;
        }
        w = true;
        REP(i,4){
            w = w && is_ok(player,board[3-i][i]);
        }
        if (w) {
            return player+1;
        }
    }
    //czy skonczona
    int cnt = 0;
    REP(i,4){
        REP(j,4){
            if (board[i][j] == '.') cnt++;
        }
    }
    if (cnt == 0) return 0;
    return -1;
}

int main(){
    int t;
    string st;
    cin>>t;
    REP(i,t){
        readb();
        int cs = check();
        if (cs == -1){
            cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
        }
        if (cs == 0){
            cout<<"Case #"<<i+1<<": Draw"<<endl;
        }
        if (cs == 1){
            cout<<"Case #"<<i+1<<": X won"<<endl;
        }
        if (cs == 2)
            cout<<"Case #"<<i+1<<": O won"<<endl;
    }
}

