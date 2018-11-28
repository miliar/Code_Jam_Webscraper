#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <bitset>
#include <algorithm>
#include <functional>
using namespace std;

#define INF (1LL<<31)-1
#define PI 2*acos(0.0)
#define FOR(i,n) for(int i = 0;i<n;++i)
#define setbit(a,b) a|=(1<<b)
#define S1(a) scanf("%d",&a)
#define S2(a,b) scanf("%d %d",&a,&b)
#define S3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define C1(a) __builtin_popcount(a)
#define gcd(a,b) __gcd(a,b)
#define ALL(a) (a.begin(),a.end())

typedef long long LL;
typedef vector<string> vs;
typedef vector<int> vi;

int main(){


    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    int t;
    scanf("%d",&t);

    for(int ca = 1;ca<=t;++ca){

        int N,L,H;
        scanf("%d %d %d",&N,&L,&H);
        int array[ 105 ];
        bool played[ 10000 ] = {false};
        for(int i = 0;i<N;++i){
                scanf("%d",&array[i]);
                played[ array[i] ] = true;
        }

        bool done = 0;
        int res = -1;
        for(int j = L;j<=H;++j){

            done = true;
            for(int i = 0;i<N;++i)if( (array[i] % j != 0) && (j % array[i] != 0) ){done = false;break;}
            if( done ){res = j;break;}

        }
        printf("Case #%d: ",ca);
        if( res == -1 )puts("NO");
        else printf("%d\n",res);

    }

    return 0;
}
