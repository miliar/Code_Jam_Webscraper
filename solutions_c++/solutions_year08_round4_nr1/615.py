#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <functional>
#include <algorithm>

using namespace std;

vector<int> G;
vector<int> C;
vector<bool> I;
int M, V;

bool comp( int x )
{
    if (x < (M-1)/2)
    {
        bool a = comp( (x+1)*2-1 );
        bool b = comp( (x+1)*2 );
        if (G[x] == 1)
        {
            I[x] = a && b;
        }
        else
        {
            I[x] = a || b;
        }
    }
    return I[x];
}

int solve( int x, int v )
{
    if (I[x] == (v == 1)) return 0;
    if (x >= (M-1)/2) return -1;

    int n1 = (x+1)*2-1;
    int n2 = (x+1)*2;

    if (G[x] == 1)
    {
        if (v == 1)
        {
            int a = solve( n1, 1 );
            int b = solve( n2, 1 );
            if (a == -1 || b == -1)
            {
                if (C[x] == 0) return -1;
                if (a != -1) return a+1;
                if (b != -1) return b+1;
                return -1;
            }
            else
            {
                int r = a + b;
                if (C[x] == 1)
                {
                    int y = 0;
                    if (a == -1) y = b;
                    else if (b == -1) y = a;
                    else y = min( a, b );
                    y++;
                    if (y < r) r = y;
                }
                return r;
            }
        }
        else
        {
            int a = solve( n1, 0 );
            int b = solve( n2, 0 );
            if (a == -1 && b == -1)
            {
                return -1;
            }
            if (a == -1) return b;
            if (b == -1) return a;
            return min( a, b );
        }
    }
    else // OR
    {
        if (v == 1)
        {
            int a = solve( n1, 1 );
            int b = solve( n2, 1 );
            if (a == -1 && b == -1)
            {
                return -1;
            }
            if (a == -1) return b;
            if (b == -1) return a;
            return min( a, b );
        }
        else
        {
            int a = solve( n1, 0 );
            int b = solve( n2, 0 );
            if (a == -1 || b == -1)
            {
                if (C[x] == 0) return -1;
                if (a != -1) return a+1;
                if (b != -1) return b+1;
                return -1;
            }
            else
            {
                int r = a + b;
                if (C[x] == 1)
                {
                    int y = 0;
                    if (a == -1) y = b;
                    else if (b == -1) y = a;
                    else y = min( a, b );
                    y++;
                    if (y < r) r = y;
                }
                return r;
            }
        }
    }
}

int main( void )
{
    int N;
    scanf( "%d", &N );

    for (int tc = 0; tc < N; tc++)
    {
        scanf( "%d%d", &M, &V );

        G.resize( (M-1)/2 );
        C.resize( (M-1)/2 );
        I.resize( M );

        for (int i = 0; i < (M-1)/2; i++)
            scanf( "%d%d", &G[i], &C[i] );

        for (int i = (M-1)/2; i < M; i++)
        {
            int x;
            scanf( "%d", &x );
            I[i] = (x==1);
        }

        comp( 0 );

        int cnt = solve( 0, V );
        if (cnt == -1)
        {
            cout << "Case #" << (tc+1) << ": IMPOSSIBLE" << endl;
        }
        else
        {
            cout << "Case #" << (tc+1) << ": " << cnt << endl;
        }
    }
}
