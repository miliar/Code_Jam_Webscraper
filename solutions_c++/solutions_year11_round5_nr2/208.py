#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define VI vector<int>
#define pb push_back
#define VS vector<string>
#define mp make_pair

VI a;int N;
vector< pair<int, int> > b;

bool ok( int k ) 
    {
    
    int zadnji = 0;
    VI len;
    int last = -1;
    FOR( i, 0, b.size() )
        {
        if ( last != -1 && last + 1 != b[i].first )
            {
            FOR( j, zadnji, len.size() ) 
                if ( len[j] < k ) return false;
            zadnji = len.size();
            }
        if ( b[i].second == (int)(len.size()) - zadnji ) 
            {
            FOR( j, 0 , len.size() )
                ++len[j]; 
            last = b[i].first;
        continue;
            }
        if ( b[i].second < (int)(len.size()) - zadnji )
            {
            int kolko = - b[i].second + (int)(len.size()) - zadnji;
            FOR( j, zadnji, zadnji + kolko ) 
                if ( len[j] < k ) return false;
            zadnji = zadnji + kolko;
            FOR( j, zadnji, len.size() )
                ++len[j];
            last = b[i].first;
        continue;
            }
        if ( b[i].second > (int)(len.size()) -zadnji ) 
            {
            int kolko = + b[i].second - (int)(len.size()) + zadnji;
            FOR( j, zadnji, len.size() ) ++len[j];
            FOR( j, 0, kolko ) 
                len.pb( 1 ) ;
            last = b[i].first;
        continue;
            }
        }
    FOR( j, zadnji, len.size() )
        if ( len[j] < k ) 
            return false;
    return true;
    }

int main()
    {
    int TC;
    cin >> TC;
    FOR(tc, 0, TC)
        {
        cin >> N;
        a.clear();
        b.clear();
        a.resize(N);
        FOR(i,0,N)
            cin >> a[i];

        if ( N == 0 )
            {
            printf("Case #%d: %d\n",tc+1,0);
            continue;
            }
        sort(a.begin(),a.end());
        b.pb(mp(a[0],1));
        FOR( i, 1, a.size() )
            if ( a[i] == a[i-1] )
                ++b.back().second;
            else b.pb(mp(a[i],1));
        
        int mn = 1;
        int mx = N;
        while(mx - mn)
            {
            int mid = (mx+mn+1)/ 2;
            
            if ( ok(mid) )
                mn = mid;
            else mx = mid-1;
            }
        int sol = mx;
        printf("Case #%d: %d\n",tc+1,sol);
        }
    //system("pause");
    return 0;
    }
