#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <climits>
#include <cctype>
#include <complex>

using namespace std;

#define ull unsigned long long
#define ill long long int
#define pii pair<int,int>
#define pb(x) push_back(x)
#define F(i,a,n) for(i=(a);i<(n);++i)
#define FD(i,a,n) for(i=(a);i>=(n);--i)
#define FE(it,x) for(it=x.begin();it!=x.end();++it)
#define V(x) vector<x>
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define debug(i,sz,x) F(i,0,sz){cout<<x[i]<<" ";}cout<<endl

string s[4];

int fun() {
    int cnto,cntx,cntt,i,j;
    F(i,0,4) {
        cnto=0;cntt=0;cntx=0;
        F(j,0,4) {
            if ( s[i][j] == 'X' ) cntx++;
            if ( s[i][j] == 'O' ) cnto++;
            if ( s[i][j] == 'T' ) cntt++;
        }
        if ( cnto+cntt == 4 ) return 2;
        if ( cntx+cntt == 4 ) return 1;
    }
    F(j,0,4) {
        cnto=0;cntt=0;cntx=0;
        F(i,0,4) {
            if ( s[i][j] == 'X' ) cntx++;
            if ( s[i][j] == 'O' ) cnto++;
            if ( s[i][j] == 'T' ) cntt++;
        }
        if ( cnto+cntt == 4 ) return 2;
        if ( cntx+cntt == 4 ) return 1;
    }
    
    cnto=0;cntt=0;cntx=0;
    F(i,0,4) {
        if ( s[i][i] == 'X' ) cntx++;
        if ( s[i][i] == 'O' ) cnto++;
        if ( s[i][i] == 'T' ) cntt++;
    }
    if ( cnto+cntt == 4 ) return 2;
    if ( cntx+cntt == 4 ) return 1;

    cnto=0;cntt=0;cntx=0;
    F(i,0,4) {
        if ( s[i][3-i] == 'X' ) cntx++;
        if ( s[i][3-i] == 'O' ) cnto++;
        if ( s[i][3-i] == 'T' ) cntt++;
    }
    if ( cnto+cntt == 4 ) return 2;
    if ( cntx+cntt == 4 ) return 1;
    
    F(i,0,4) F(j,0,4) {
        if ( s[i][j] == '.' ) return 4;
    }
    return 3;
}

int main() {
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,T;
    cin >> T;
    F(t,1,T+1) {
        F(i,0,4) cin >> s[i];
        cout << "Case #" << t << ": ";
        switch(fun()) {
            case 1: cout << "X won"; break;
            case 2: cout << "O won"; break;
            case 3: cout << "Draw"; break;
            case 4: cout << "Game has not completed"; break;
        } cout << endl;
    }
}