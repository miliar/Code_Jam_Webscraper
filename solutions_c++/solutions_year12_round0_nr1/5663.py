#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <cmath>
#include <sstream>
#include <utility>
#include <cctype>
#include <numeric>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <limits>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <functional>
#include <inttypes.h>
#include <fstream>
using namespace std;

void fill()
{
    freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    vector<string> a,b;
    string ABC = "",s;
    for( char c = 'a';c < 'z'+1; c++)
        ABC+=c;

    map<char,char> m;

    for( int i = 0; i < 3; ++ i )
    {
        getline(cin,s);
        a.push_back(s);
    }
    for( int i = 0; i < 3; ++ i )
    {
        getline(cin,s);
        b.push_back(s);
    }
    for( int i = 0;i < 3; ++ i )
        for( int j = 0; j < a[i].size(); ++ j )
            m[a[i][j]] = b[i][j];
    string M = "";
    m['z'] = 'q';
    m['q'] = 'z';
    cout << m.size() << endl;
    for( int i = 0; i < ABC.size(); ++ i )
        M += m[ABC[i]];

    cout << ABC << endl;
    cout << M << endl;

    set<char> all;
    for( int i = 0; i < M.size(); ++ i )
        all.insert(M[i]);
    cout << all.size() << endl;
}
#define incontainer(c,x) ((c).find(x)!=(c).end())
template<class T> string tostring(T x) {ostringstream sout;sout<<x;return sout.str();}
template<class T> int toint( T s ) {int v;istringstream sin( tostring(s) );sin>>v;return v;}
const string ABC = "abcdefghijklmnopqrstuvwxyz";
int main()
{
    set<char> all;
    for( int i = 0; i < ABC.size(); ++ i )
        all.insert(ABC[i]);

    freopen("a.input","r",stdin);
    freopen("a.output","w",stdout);
    string B = "yhesocvxduiglbkrztnwjpfmaq";

    string s;
    getline(cin,s);

    //fill();
    int n = toint(s);
    for( int i = 0; i < n; ++ i )
    {
        getline(cin,s);
        cout << "Case #" <<(i+1)<<": ";
        for( int j = 0; j < s.size(); ++ j )
        {
            if( !incontainer(all,s[j]) )
                cout << s[j];
            else
                cout << B[s[j]-'a'];
        }
        cout << endl;
    }
    return 0;
}
