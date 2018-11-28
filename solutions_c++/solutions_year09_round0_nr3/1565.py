#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

string line;
char const* p = "welcome to code jam";
int const M = 10000;

bool seen[1000][50];
int mem[1000][50];

int solve(int i, int j)
{
    if( seen[i][j] )
        return mem[i][j];
    seen[i][j] = true;
    int& rv = mem[i][j];

    if( i == line.size() )
    {
//        cout << "Done " << j << endl;
        rv = (p[j] == NULL);
    }
    else
    {
        rv = 0;
        if( p[j] == NULL )
            rv += 1 + solve(i + 1, 0);
        if( line[i] == p[j] )
            rv += solve(i + 1, j + 1);
        if( p[j] != NULL )
            rv += solve(i + 1, j);
        rv %= M;
    }

    return rv;
}

int main()
{
    int n;
    getline(cin, line);
    n = atoi(line.c_str());

    for( int C = 1; C <= n; ++C )
    {
        memset(seen, 0, sizeof(seen));

        getline(cin, line);
        printf("Case #%d: %04d\n", C, solve(0, 0));
    }

    return 0;
}
