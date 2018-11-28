#include <iostream>
#include <map>
#include <string>
#include <cstdlib>
#include <memory.h>
#include <algorithm>

using namespace std;

map<string,int> id;

int mem[101][1001];
int q[1001];
int S, Q;
int go(int s, int i)
{
    if( i >= Q )
        return 0;
    if( mem[s][i] != -1 )
        return mem[s][i];
    int& rv = mem[s][i];
    rv = 1<<20;

    int j = i;
    while( j != Q && q[j] != s )
        ++j;

    if( j == Q )
        rv = 0;
    else
    {
        for( int k = 0; k != S; ++k )
            if( k != q[j] )
                rv = min(rv, 1 + go(k, j));
    }

    return rv;
}

void solve(int Case)
{
    id.clear();
    memset(mem, -1, sizeof(mem));

    string line;
    getline(cin, line);
    S = atoi(line.c_str());
    for( int i = 0; i != S; ++i )
    {
        getline(cin, line);
        id[line] = i;
    }

    getline(cin, line);
    Q = atoi(line.c_str());
    for( int i = 0; i != Q; ++i )
    {
        getline(cin, line);
        q[i] = id[line];
    }

    int rv = 1<<29;
    for( int i = 0; i != S; ++i )
        rv = min(rv, go(i, 0));
    cout << "Case #" << Case << ": " << rv << endl;
}

int main()
{
    string line;
    getline(cin, line);
    int N = atoi(line.c_str());
    for( int i = 1; i <= N; ++i )
        solve(i);

    return 0;
}
