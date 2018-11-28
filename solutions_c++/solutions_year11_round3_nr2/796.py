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

    int T,ca = 0;
    scanf("%d",&T);
    while(T--){

        int L,t,N,C;
        scanf("%d %d %d %d",&L,&t,&N,&C);
        int A[ 1010 ];
        --N;
        for(int i = 0;i<C;++i)scanf("%d",&A[i]);
        vector< int >points;
        int totalTime = 0;

        for(int i = 0;i<=N;++i){
            points.push_back( A[ i % C ] );
            totalTime += A[ i % C ];
        }

        vector< int >pointsLeft;
        int elapsed = 0;
        int ended = 0;
        while( t>0 && ended <= N ){

            t -= 2 * points[ ended ];
            ended++;

        }
        if( t < 0 ){

            t *= -1;
            pointsLeft.push_back(  t/2 );

        }
        for(int i = ended;i<=N;++i)pointsLeft.push_back( points[i] );
        sort( pointsLeft.rbegin(),pointsLeft.rend());

        int saved = 0;
        for(int i = 0;i < min( (int)pointsLeft.size() , L );++i){
            saved += pointsLeft[i];
        }
        printf("Case #%d: %d\n",++ca,( totalTime - saved ) * 2 + saved );

    }
    return 0;
}
