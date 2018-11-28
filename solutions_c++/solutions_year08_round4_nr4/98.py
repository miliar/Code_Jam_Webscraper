#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int p[5];

string perm(string const& s, int k)
{
    string rv;
    int t = s.size() / k;
    for( int i = 0; i != t; ++i )
    {
        for( int j = 0; j != k; ++j )
            rv += s[k*i+p[j]];
    }

    return rv;
}

int f(string const& s)
{
    int rv = 1;
    for( int i = 1; i != s.size(); ++i )
        rv += (s[i] != s[i-1]);
    return rv;
}

int main()
{
    int N;
    cin >> N;
    for( int c = 1; c <= N; ++c )
    {
        int k;
        string s;
        cin >> k >> s;
        for( int i = 0; i != k; ++i )
            p[i] = i;

        int rv = 1<<29;
        do
        {
            rv = min(rv, f(perm(s, k)));
        } while( next_permutation(p, p+k) );

        cout << "Case #" << c << ": " << rv << endl;
    }

    return 0;
}
