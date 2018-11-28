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
        int n, m;
        cin >> n >> m;
        VS a(n);
        FOR(i,0,n)
            cin >> a[i];
        
        FOR(i,1,n)
            FOR(j,1,m)
                {
                if( a[i][j] == '#' && a[i][j-1] == '#' && a[i-1][j] == '#' && a[i-1][j-1] == '#' )
                    {
                    a[i][j] = '/'; a[i][j-1] = '\\';a[i-1][j] = '\\';a[i-1][j-1]= '/';
                    }
                }
        bool ok = 0;
        FOR(i,0,n)
            FOR(j,0,m)
                if( a[i][j] == '#' ) ok = 1;
        if ( ok ) {
        printf("Case #%d:\nImpossible\n",tc+1);
        }
        else
        {
        printf("Case #%d:\n",tc+1);
        FOR(i,0,n)
            cout << a[i] << endl;
        }
        }
    //system("pause");
    return 0;
    }
