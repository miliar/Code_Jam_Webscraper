#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>

using namespace std;

string line;

string  words[5001];
string  pats [501];
int     rv   [501];
int     l, d, n;

bool match(int wi, int pi)
{
    int j = 0;
    string const& w = words[wi];
    string const& p = pats[pi];

    for( int i = 0; i != l; ++i )
    {
        if( p[j] == '(' )
        {
            bool ok = false;
            while( p[++j] != ')' )
                ok |= (w[i] == p[j]);

            if( !ok )
                return false;
            ++j;
        }
        else if( w[i] != p[j++] )
            return false;
    }

    return true;
}

int main()
{

    getline(cin, line);
    sscanf(line.c_str(), "%d %d %d", &l, &d, &n);

    for( int i = 0; i != d; ++i )
        getline(cin, words[i]);
    for( int i = 0; i != n; ++i )
        getline(cin, pats[i]);

    for( int i = 0; i != d; ++i )
    for( int j = 0; j != n; ++j )
        if( match(i, j) )
            ++rv[j];

    for( int i = 0; i != n; ++i )
        printf("Case #%d: %d\n", i+1, rv[i]);

    return 0;
}
