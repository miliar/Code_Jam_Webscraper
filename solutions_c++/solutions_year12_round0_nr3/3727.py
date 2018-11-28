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

string tostr(int x)
{
    ostringstream oo;
    oo << x;
    return oo.str();
}

int main()
{
    int t,a,b;
    scanf("%d",&t);
    REP(_,t)
    {
        scanf("%d %d",&a,&b);
        set<pair<int,int> > r;
        FOR(i,a,b)
        {
            string ii = tostr(i);

            REP(j,ii.size())
            {
                int xx = 0;
                REP(k,ii.size()) xx = xx * 10 + ii[(j+k)%ii.size()] - '0';
                if (xx > i && xx <= b)
                {
                    r.insert(pair<int,int>{i,xx});;
                }
            }

        }
        printf("Case #%d: %d\n",_+1,r.size());
    }
    return 0;
}
