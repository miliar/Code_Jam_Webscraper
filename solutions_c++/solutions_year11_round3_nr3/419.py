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

int main()
    {
    int TC;
    cin >> TC;
    FOR(tc, 0, TC)
        {
        long long N, L, H;
        cin >> N >> L >> H;
        vector<long long> a(N);
        FOR(i,0,N) cin >> a[i];
        int sol = H + 1;
        FOR( i , L , H + 1 ) 
            {
            bool ok = 1;
            FOR(j,0,N)
                if( i % a[j] != 0 && a[j] % i != 0 ) 
                    ok = 0;
            if ( ok )
                sol = min( sol, i );
            }
        if ( sol == H + 1 ) printf("Case #%d: NO\n",tc+1);
        else printf("Case #%d: %d\n",tc+1,sol);
        }
    //system("pause");
    return 0;
    }
