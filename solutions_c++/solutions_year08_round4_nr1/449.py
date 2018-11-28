#pragma comment(linker, "/STACK:134217728")

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define sqr(a) ((a)*(a))
#define det2(a,b,c,d) ((a)*(d) - (b)*(c))

int INF = 20000;

int n, nin, nout, G[11000], C[11000], L[11000];
int memo[11000][2];

int f(int v, int val)
{
    if ( memo[v][val] != -1 )
        return memo[v][val];
    int &res = memo[v][val], l=2*v, r=l+1;
    if ( v > nin )
    {
        if ( val == L[v] )
            res = 0;
        else
            res = INF;
        return res;
    }
    else
    {
        res = INF;
        if ( G[v] == 1 ) // and
        {
            if ( val == 0 )
                res = min(res, min(f(l,0), f(r,0)));
            else
                res = min(res, f(l,1) + f(r,1));
        }
        else
        {
            if ( val == 0 )
                res = min(res, f(l,0) + f(r,0));
            else
                res = min(res, min(f(l,1),f(r,1)));
        }

        if ( C[v] == 1 )
        {
            if ( G[v] == 0 )
            {
                if ( val == 0 )
                    res = min(res, 1+min(f(l,0), f(r,0)));
                else
                    res = min(res, 1+f(l,1) + f(r,1));
            }
            else
            {
                if ( val == 0 )
                    res = min(res, 1+f(l,0) + f(r,0));
                else
                    res = min(res, 1+min(f(l,1),f(r,1)));
            }
        }

        return res;
    }

    return res;
}

int main()
{
    int i, j, V;
    int TST, cas;
    
    scanf( "%d", &TST );
    for ( cas = 1 ; cas <= TST ; cas++ )
    {
        scanf( "%d%d", &n, &V );
        nin = (n-1)/2;
        nout = n - nin;
        for ( i = 1 ; i <= n ; i++ )
        {
            if ( i <= nin )
                scanf( "%d%d", &G[i], &C[i] );
            else
                scanf( "%d", &L[i] );
        }

        printf( "Case #%d: ", cas );
        memset(memo,-1,sizeof(memo));
        int res = f(1,V);
        if ( res < INF )
            printf( "%d\n", res );
        else
            printf( "IMPOSSIBLE\n" );
    }


    return 0;
}
