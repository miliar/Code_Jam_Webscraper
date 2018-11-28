#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <cstdlib>
#include <string>
#include <sstream>

using namespace std;

#define VS vector<string>
#define VI vector<int>
#define VVI vector< VI >
#define pb push_back
#define mp make_pair
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORC(it,kont) for(__typeof((kont).begin()) it = (kont).begin(); it!=(kont).end(); ++it)

char buff[20000];

int test( VS s, char c )
    {
    int ok = 0;
    FOR( i, 0, 4 )
        {
        int cnt = 0;
        FOR( j, 0, 4 )
            if( s[i][j] == c || s[i][j] == 'T' )
                ++cnt;
        if( cnt == 4 )
            ok = 1;
        }
    FOR( i, 0, 4 )
        {
        int cnt = 0;
        FOR( j, 0, 4 )
            if( s[j][i] == c || s[j][i] == 'T' )
                ++cnt;
        if( cnt == 4 )
            ok = 1;
        }
    int cnt = 0;
    FOR( i, 0, 4 )
        if( s[i][i] == c || s[i][i] == 'T' )
            ++cnt;
    if( cnt == 4 )
        ok = 1;
    cnt = 0;
    FOR( i, 0, 4 )
        if( s[i][3-i] == c || s[i][3-i] == 'T' )
            ++cnt;
    if( cnt == 4 )
        ok = 1;
    return ok;
    }

int main()
    {
    int T;
    gets(buff);
    sscanf(buff,"%d",&T);

    FOR( t, 0, T )
        {
        VS s(4);
        FOR( i, 0, 4 ) cin >> s[i];

        if( test( s, 'X' ) ) 
            {
            printf("Case #%d: X won\n",t+1);
            continue;
            }
        if( test( s, 'O' ) ) 
            {
            printf("Case #%d: O won\n",t+1);
            continue;
            }
        int tmp = 0;
        FOR( i, 0, 4 ) FOR( j, 0, 4 ) tmp += (s[i][j] =='.');
        if ( tmp == 0 )
            {
            printf("Case #%d: Draw\n",t+1);
            continue;
            }
        printf("Case #%d: Game has not completed\n",t+1);
        
        }
    return 0;
    }
