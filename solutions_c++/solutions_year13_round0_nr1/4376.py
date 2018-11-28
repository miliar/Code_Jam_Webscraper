#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <cassert>
#include <complex>
#include <memory>
#include <limits>

using namespace std;

#define P1(pair) pair.first
#define P2(pait) pair.second

typedef long long ll;
typedef long double ld;
typedef size_t ss;
typedef stringstream SS;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define DBG(x) cout<<x<<endl
#define SSMAX ((ss)(-1))
#define ARR2D(jump, bigj, smallj) (((jump)*(bigj) + (smallj)))
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((a).size())
#define SIZEI(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
#define ZERO(x) memset(x,0,sizeof(x))
#define SETFLTSCI \
    cout.setf(ios::scientific, ios::floatfield);
#define SETFLTPREC(n) \
    cout.setf(ios::fixed, ios::floatfield); \
    cout.precision(n);
#define UNSETFLTPREC \
    cout.unsetf(ios::floatfield);
#define GCJREDR(problem,other) \
    freopen(problem "-" other ".in","r",stdin); \
    freopen(problem "-" other ".out","w",stdout);
char game[4][4];
bool Xwin=false;
bool Owin=false;

void print(){
    for (int i=0;i<4;i++){
        for (int j=0;j<4;j++){
            cout<<game[i][j];
        }
        cout<<endl;
    }
}
void check(char sym){
    for (int i=0;i<4;i++){
        if (game[i][0]==sym &&
             game[i][1]==sym &&
             game[i][2]==sym &&
              game[i][3]==sym) {
            if (sym=='X') Xwin=true; else Owin=true;
            return;
        }
        if (game[0][i]==sym &&
            game[1][i]==sym &&
             game[2][i]==sym &&
                game[3][i]==sym) {
            if (sym=='X') Xwin=true; else Owin=true;
            return;
        }
    }
    if (game[0][0]==sym &&
            game[1][1]==sym &&
            game[2][2]==sym &&
            game[3][3]==sym) {
        if (sym=='X') Xwin=true; else Owin=true;
        return;
    }
    if (game[0][3]==sym &&
            game[1][2]==sym &&
            game[2][1]==sym &&
            game[3][0]==sym) {
        if (sym=='X') Xwin=true; else Owin=true;
        return;
    }

}

int main()
{
    GCJREDR("A","large");
    int T,P=1;
    for (cin>>T;P<=T;P++){
        bool full=true;
        int tx=-1,ty=-1;
        for (int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin>>game[i][j];
                if (game[i][j]=='T'){
                    tx=j;
                    ty=i;
                } else if (game[i][j]=='.') {
                    full=false;
                }
            }
        }
        if (ty!=-1)
            game[ty][tx]='X';
        Xwin=false;
        Owin=false;
        check('X');
        if (Xwin && Owin){
            cout<<"Case #"<<P<<": "<< "Draw"<<endl;continue;
        } if (Xwin) {
            cout<<"Case #"<<P<<": "<< "X won"<<endl;continue;
        } if (Owin) {
            cout<<"Case #"<<P<<": "<< "O won"<<endl;continue;
        }
        if (ty!=-1)
           game[ty][tx]='O';
        Xwin=false;
        Owin=false;

        check('O');
        if (Xwin && Owin){
            cout<<"Case #"<<P<<": "<< "Draw"<<endl;continue;
        } if (Xwin) {
            cout<<"Case #"<<P<<": "<< "X won"<<endl;continue;
        } if (Owin) {
            cout<<"Case #"<<P<<": "<< "O won"<<endl;continue;
        } if (full) {
            cout<<"Case #"<<P<<": "<< "Draw"<<endl;continue;
        } else {
            cout<<"Case #"<<P<<": "<<"Game has not completed" <<endl;
        }

        //cout<<"Case #"<<P<<": "<< <<endl;
    }

    return 0;
}

