#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <math.h>
#include <set>
#include <queue>
#include <string>
#include <string.h>
#include <algorithm>
#include <map>
#include <iomanip>
using namespace std;

const int mod = 100003;


int sols[] = { 1 , 2 , 3 , 5 , 8 , 14 , 24 , 43 , 77 , 140 , 256 , 472 , 874 , 1628 , 3045 , 5719 , 10780 , 20388 , 38674 , 73562 , 140268 , 268066 , 513350 , 984911 , 984911 };

int dp[1000];

int f( int n , int k ){

    for( int i = 0; i < k; ++i ) dp[i] = 0;
    dp[k] = dp[k+1] = 1;

    for( int i = k+2; i <= n; ++i ){
        dp[i] = 0;
        for( int j = 1; j <= k; ++j )
            dp[i] = (dp[i]+dp[i-j])%mod;
    }
    return dp[n];
}

int main(){
    freopen("Ulaz.txt","r",stdin);
    freopen("Izlaz2.txt","w",stdout);
    int tests;
    scanf("%d",&tests);

    for( int t = 1; t <= tests; ++t ){
        int n;
        cin >> n;
        n--;

        int sol = 0;
        for( int i = 2; i <= n + 1; ++i )sol = (sol+f( n , i ))%mod;
        printf("Case #%d: %d\n",t,(sol+1)%mod);

    }

    return 0;
}
