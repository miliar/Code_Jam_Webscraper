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
double dp[1010];

double go( int n )
    {
    double& sol = dp[n];
    if ( sol != -1 ) return sol;
    if ( n <= 1 ) { sol = 0; return sol; }

    

    }

int main()
    {

    int TC;
    gets(a);
    sscanf(a,"%d",&TC);
    //cout << TC << endl;
    FOR(i,0,1010)
        dp[i] = -1;

    for( int i = 0; i < 1010; ++i ) 
        go( i );

    FOR(tc, 0, TC)
        {
        
        double sol = 0;

        int N;
        cin >> N;
        VI x(N);
        FOR(i,0,N) { cin >> x[i]; --x[i];}

        int fp = 0;
        FOR(i,0,N)
            if ( i == x[i] ) 
                ++fp;
        sol = N - fp;
        printf("Case #%d: %.6lf\n",tc+1,sol);
        }
    //system("pause");
    return 0;
    }
