/*
 * Bidhan Roy
 * University of Dhaka
 */

using namespace std;

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <ctime>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define rep(i,n) for(__typeof(n) i=0; i<(n); i++)
#define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)
#define inf (1<<30)
#define eps 1e-9
#define pb push_back
#define ins insert
#define mp make_pair
#define sz(x) ((int)x.size())
#define clr clear()
#define all(x) x.begin(),x.end()
#define xx first
#define yy second
#define sqr(x) ((x)*(x))
#define mem(x,val) memset((x),(val),sizeof(x));
#define read(x) freopen(x,"r",stdin);
#define rite(x) freopen(x,"w",stdout);

typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef map<int,st> mis;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

#define mx 10

char brd[mx][mx];

bool row(char ch){
    rep(i,4){
        int cnt=0;
        rep(j,4) cnt+=(brd[i][j]==ch || brd[i][j]=='T');
        if(cnt==4) return true;
    }
    return false;
}

bool col(char ch){
    rep(j,4){
        int cnt=0;
        rep(i,4) cnt+=(brd[i][j]==ch || brd[i][j]=='T');
        if(cnt==4) return true;
    }
    return false;
}

bool dia(char ch){
    int cnt=0;
    rep(i,4) cnt+=(brd[i][i]==ch || brd[i][i]=='T');
    if(cnt==4) return true;
    int j=3;
    cnt=0;
    rep(i,4) {
        cnt+=(brd[i][j]==ch || brd[i][j]=='T');
        j--;
    }
    if(cnt==4) return true;
    return false;
}

int main(){
    read("Ain.txt");
    rite("Aout.txt");
    //ios_base::sync_with_stdio(0);
    int test,kas=0;
    cin>>test;
    while(test--){
        rep(i,4) cin>>brd[i];
        printf("Case #%d: ",++kas);
        if(row('X') || col('X') || dia('X')) puts("X won");
        else if(row('O') || col('O') || dia('O')) puts("O won");
        else {
            int e=0;
            rep(i,4) rep(j,4) e+=(brd[i][j]=='.');
            if(e) puts("Game has not completed");
            else puts("Draw");
        }
    }
    return 0;
}
