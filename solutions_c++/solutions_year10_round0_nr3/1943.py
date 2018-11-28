#include <iostream>
#include <fstream>
#include <cstdlib>
#include <math.h>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;

typedef long long ll;

int r,m,n;
int sz[1005];
ll dp[1005][2];

ll jmp[1005][2];

int main(){
    freopen("Ulaz.txt","r",stdin);
    freopen("Izlaz.txt","w",stdout);
    int tests;
    scanf("%d",&tests);

    for( int t = 1; t <= tests; ++t ){

        memset( dp , -1, sizeof(dp));

        scanf("%d%d%d",&r,&m,&n);
        for( int i = 0; i < n; ++i ) scanf("%d",&sz[i]);

        for( int i = 0; i < n; ++i ){
            int j;
            ll sum=0;
            for( j = i; sum + sz[j] <= m; j = (j+1)%n ){
                sum += sz[j];
                if( j == (i-1+n)%n ) break;
            }
            jmp[i][0] = j;
            jmp[i][1] = sum;
        }



        int now = 0;
        ll earn = 0;

        for( int i = 1; i <= r; ++i ){

            if( dp[now][0] != -1 && i + (i-dp[now][0]) < r ){
                int diff = i - dp[now][0];
                ll cost = earn - dp[now][1];

                int left = r - i + 1;
                int times = left / diff;


                i += times * diff;
                earn += times * cost;
                --i;

                continue;
            }

            dp[now][0] = i;
            dp[now][1] = earn;

            earn += jmp[now][1];
            now = jmp[now][0];
        }

        cout<<"Case #"<<t<<": "<<earn<<endl;
    }


    return 0;
}
