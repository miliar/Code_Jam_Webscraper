#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <functional>
#include <algorithm>

using namespace std;

int calc( char* s, int* p, int k )
{
    char buf[10000];
    int n = strlen( s );
    for (int i = 0; i < n; i += k)
    {
        for (int j = 0; j < k; j++)
        {
            buf[i+p[j]] = s[i+j];
        }
    }
    buf[n] = 0;
    //printf( "%s\n", buf );

    int c = 1;
    for (int i = 1; i < n; i++)
    {
        if (buf[i] != buf[i-1]) c++;
    }
    return c;
}

int main( void )
{
    int TC;
    scanf( "%d", &TC );

    for (int tc = 0; tc < TC; tc++)
    {
        int k;
        scanf( "%d", &k );
        char buf[10000];
        gets( buf );
        gets( buf );
        int n = strlen( buf )-1;
        if (buf[n] == '\n') buf[n] = 0;

        int p[10];
        for (int i = 0; i < k; i++)
            p[i] = i;

        int res = 1000000000;
        do {
            int c = calc( buf, p, k );
            if (c < res) res = c;
        } while (next_permutation( p, p + k ));

        cout << "Case #" << (tc+1) << ": " << res << endl;
    }
}
