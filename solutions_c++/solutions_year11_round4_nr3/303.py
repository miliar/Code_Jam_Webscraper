#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <cstdlib>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define VI vector<int>
#define pb push_back
#define VS vector<string>

#define MAX 10000000

int a[MAX];
vector<int> p;

int N;

void sito()
    {
    for( long long i = 2; i < MAX; ++i )
        {
        if ( a[i] == 0 )
        {
        p.pb( i );
        for( long long j = i*i; j < MAX; j+=i ) 
            a[j] = i;
        }
        }
    }


int main()
    {
    memset( a, 0, sizeof(a));
    sito();
    int TC;
    cin >> TC;
    FOR(tc, 0, TC)
        {
        cin >> N;
        long long sol = 1;
        
        FOR( i, 2, N+1) 
            if( a[i] == 0 )
                {
                --sol;
                int y = i;
                while( y <= N )
                    {
                    ++sol;
                    y*= i;
                    }
                }

        if ( N == 1 ) printf( "Case #%d: 0\n",tc+1);
        else printf("Case #%d: %d\n",tc+1,sol);
        }
    //system("pause");
    return 0;
    }
