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

char a[10000];


int main()
    {

    int TC;
    gets(a);
    sscanf(a,"%d",&TC);

    FOR(tc, 0, TC)
        {
        
        int N;
        cin >> N;
        VI x(N);
        int sum = 0; int sol = 0;
        FOR(i,0,N) { cin >> x[i]; sum ^= x[i]; sol += x[i]; }

        sort( x.begin(), x.end() );

        if ( sum != 0 )
            printf("Case #%d: NO\n",tc+1);
        else
            printf("Case #%d: %d\n",tc+1,sol-x[0]);
        }
    //system("pause");
    return 0;
    }
