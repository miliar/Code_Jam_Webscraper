#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cassert>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <sstream>
#include <queue>
#include <stack>
using namespace std;

#define FOR(i,a,b) for(int i = (a),_n=(b);i<=_n;i++)
#define REP(i,n) for(int i = 0,_n=(n);i<_n;i++)
#define _m(a,b) memset(a,b,sizeof(a))

#define debug(x) cout << #x << " = " << x << endl;
#define debug2(x,y) cout << #x << "[" <<  y << "] = " << x[y] << endl;

vector<string> split( const string& s, const string& delim =" " ) {
    vector<string> res;
    string t;
    for ( int i = 0 ; i != s.size() ; i++ ) {
        if ( delim.find( s[i] ) != string::npos ) {
            if ( !t.empty() ) {
                res.push_back( t );
                t = "";
            }
        } else {
            t += s[i];
        }
    }
    if ( !t.empty() ) {
        res.push_back(t);
    }
    return res;
}

vector<int> splitInt( const string& s, const string& delim =" " ) {
    vector<string> tok = split( s, delim );
    vector<int> res;
    for ( int i = 0 ; i != tok.size(); i++ )
        res.push_back( atoi( tok[i].c_str() ) );
    return res;
}

#define ARRSIZE(x) (sizeof(x)/sizeof(x[0]))

template<typename T> void print( T a ) {
    cerr << a;
}
static void print( long long a ) {
    cerr << a << "L";
}
static void print( string a ) {
    cerr << '"' << a << '"';
}
template<typename T> void print( vector<T> a ) {
    cerr << "{";
    for ( int i = 0 ; i != a.size() ; i++ ) {
        if ( i != 0 ) cerr << ", ";
        print( a[i] );
    }
    cerr << "}" << endl;
}

char input[][100] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

char output[][100] = {"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"};

int main()
{
    char mapping[256]={0};
    REP(i,3)
        REP(j,strlen(input[i]))
        {
            if (mapping[input[i][j]]!=0) assert(mapping[input[i][j]] == output[i][j]);
            mapping[input[i][j]] = output[i][j];
        }

    mapping['z'] = 'q';
    mapping['q'] = 'z';

    /*
    FOR(i,'a','z')
    {
        printf("%c %c\n",i,mapping[i]);
    }
    */
    int t;
    char s[200];
    scanf("%d",&t);
    gets(s);
    REP(_,t)
    {
        gets(s);
        REP(i,strlen(s)) s[i] = mapping[s[i]];
        printf("Case #%d: %s\n",_+1,s);
    }
    return 0;
}
