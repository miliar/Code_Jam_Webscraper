/*
TASK:  
ALGO:
LANG: C++
USER: smilitude
DATE: 2012-04-14 Sat 05:51 PM    
*/

#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<cassert>
#include<climits>
using namespace std;

#define REP(i,n) for(int i=0, _e(n); i<_e; i++)
#define FOR(i,a,b) for(int i(a), _e(b); i<=_e; i++)
#define FORD(i,a,b) for(int i(a), _e(b); i>=_e; i--) 
#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define SET(t,v) memset((t), (v), sizeof(t))
#define ALL(x) x.begin(), x.end()
#define UNIQUE(c) (c).resize( unique( ALL(c) ) - (c).begin() )

#define sz size()
#define pb push_back
#define VI vector<int>
#define VS vector<string>

typedef long long LL;
typedef long double LD;
typedef pair<int,int> pii;

#define D(x) if(1) cout << __LINE__ <<" "<< #x " = " << (x) << endl;
#define D2(x,y) if(1) cout << __LINE__ <<" "<< #x " = " << (x) \
    <<", " << #y " = " << (y) << endl;

string a[] = {
    "ejp mysljylc kd kxveddknmc re jsicpdrysi", 
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", 
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

string b[] = {
    "our language is impossible to understand",
    "there are twenty six factorial possibilities", 
    "so it is okay if you want to just give up" 
};

int main() {
    int t, ncase = 0;
    char line[505];

    char map[500];
    REP(i,3) REP(j,a[i].sz) map[ a[i][j] ] = b[i][j];
        
//    FOR(i,'a', 'z') if( !map[i] ) cout << char(i) << endl;
    map['q'] = 'z'; 
    map['z'] = 'q';

    cin >> t;
    gets( line );
    while( t-- ) {
        gets( line );
        int len = strlen( line );
        REP(i,len) line[i] = map[ line[i] ];
        printf("Case #%d: %s\n", ++ncase, line);
    }

    return 0;
}

