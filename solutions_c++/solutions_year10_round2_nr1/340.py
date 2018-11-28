#include <iostream>
#include <set>
#include <vector>
using namespace std;

set<string> a, b;

vector<string> parse(string s)
{
    vector<string> v;
    string sa = "";
    sa += s[0];
    for ( int i = 1; i < s.size(); ++i )
    {
        if ( s[i] == '/' ) v.push_back( sa );
        sa += s[i];
    }
    v.push_back( sa );
    return v;
}

int main()
{
    int t; cin >> t;
    for (int caso = 0; caso < t; ++caso)
    {
        a.clear();
        b.clear();
        
        int n, m;
        cin >> n >> m;
        vector<string> d1(n);
        for (int i = 0; i < n; ++i)
            cin >> d1[i];
        vector<string> d2(m);
        for (int i = 0; i < m; ++i)
            cin >> d2[i];
        
        for ( int i = 0; i < d1.size(); ++i )
        {
            vector<string> v = parse( d1[i] );
            for (int j = 0; j < v.size(); ++j)
                a.insert( v[j] );
        }
        for ( int i = 0; i < d2.size(); ++i )
        {
            vector<string> v = parse( d2[i] );
            for (int j = 0; j < v.size(); ++j)
                b.insert( v[j] );
        }
        
        int resp = 0;
        for ( set<string>::iterator it = b.begin(); it != b.end(); ++it )
        {
            if ( a.count( *it ) != 1 ) ++resp;
        }
        
        cout << "Case #" << caso+1 << ": " << resp << endl;
    }
}
