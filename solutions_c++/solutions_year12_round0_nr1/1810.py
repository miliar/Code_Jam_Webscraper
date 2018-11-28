#include <cstdio>
#include <cstring>
#include <iostream>
#include <sstream>
using namespace std;

string s;

void read()
{
    getline ( cin , s );
}

char match ( char ch )
{
    if ( ch == 'o' ) return 'k';
    if ( ch == 'e' ) return 'o';
    if ( ch == 'j' ) return 'u';
    if ( ch == 'p' ) return 'r';
    if ( ch == 'm' ) return 'l';
    if ( ch == 'y' ) return 'a';
    if ( ch == 's' ) return 'n';
    if ( ch == 'l' ) return 'g';
    if ( ch == 'c' ) return 'e';
    if ( ch == 'k' ) return 'i';
    if ( ch == 'd' ) return 's';
    if ( ch == 'x' ) return 'm';
    if ( ch == 'v' ) return 'p';
    if ( ch == 'n' ) return 'b';
    if ( ch == 'r' ) return 't';
    if ( ch == 'i' ) return 'd';
    if ( ch == 'a' ) return 'y';
    if ( ch == 'b' ) return 'h';
    if ( ch == 'g' ) return 'v';
    if ( ch == 'h' ) return 'x';
    if ( ch == 'w' ) return 'f';
    if ( ch == 'z' ) return 'q';
    if ( ch == 'f' ) return 'c';
    if ( ch == 'q' ) return 'z';
    if ( ch == 't' ) return 'w';
    if ( ch == 'u' ) return 'j';
    return ch;
}

void solve ( int test )
{
    string res;

    int i;
    for (i = 0; i < (int)s.length(); ++i)
    {
        res.push_back ( match ( s[i] ) );
    }
    cout << "Case #" << test << ": " << res << endl;
}


int main()
{
    int t;
    cin >> t;
    getchar();

    for (int i = 1; i <= t; ++i)
    {
        read();
        solve ( i );
    }

    return 0;
}
