
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;
#define MAXN 1010

int n;
int N[MAXN];
int f[MAXN][MAXN];
int maxcount[MAXN];
int chose[MAXN];

void pack2(int c)
{
    int origin = c;
    if(c == 1)
        return;
    for( int i = 2; i <= c; i++ )
	{
        int cnt = 0;
        while( ( c % i ) == 0 && c >= i )
            c = c / i, cnt++;
        if ( cnt > f[ c ][ i ] )
            f[ c ][ i ] = cnt;
        if ( cnt > maxcount[ i ] )
            maxcount[i] = cnt, chose[i] = origin;
        if(c == 1)
			return;
    }
}

void pack(int c)
{
    if(c == 1)
        return;
    for(int i = 2; i <= c; i++)
	{
        int cnt = 0;
        while((c % i) == 0 && c >= i)
            c = c / i, cnt++;
        if(cnt > N[i])
            N[i] = cnt;
        if(c == 1)
			return;
    }
}

bool isin(int c)
{
    if(c == 1)
        return true;
    for(int i = 2; i <= c; i++)
	{
        int cnt = 0;
        while((c % i) == 0 && c >= i)
            c = c / i, cnt++;
        if(cnt > N[i])
            return false;
        if(c == 1)
			return true;
    }
    return true;
}
int main()
{
	int t;
    freopen("output", "w", stdout);
    scanf("%d", &t);
	for ( int k = 1; k <= t; ++k )
    {
        scanf("%d", &n);
        memset(f, 0, sizeof(f));
        memset(maxcount, 0, sizeof(maxcount));
        memset(chose, 0, sizeof(chose));
        for(int i = 1; i <= n; i++)
            pack2(i);

        int big = 0, small = 0;
        bool isFirst = true;
        memset(N, 0, sizeof(N));

        for(int i = 1; i <= n; i++)
		{
            if( !maxcount[ i ] )
				continue;
            if( isin( chose[ i ] ) && !isFirst )
				continue;
            isFirst = false, small++;
            pack(chose[i]);
        }

        for(int i = n; i >= 1; i--){
            if(isin(i) && !isFirst)
				continue;
            isFirst = false, small++;
            pack(i);
        }

        isFirst = true;
        memset(N, 0, sizeof(N));
        for(int i = 1; i <= n; i++)
		{
            if(isin(i) && !isFirst)
				continue;
            isFirst = false;
            big++;
            pack(i);
        }


        printf("Case #%d: %d\n", k, big - small);

    }
    return 0;
}


