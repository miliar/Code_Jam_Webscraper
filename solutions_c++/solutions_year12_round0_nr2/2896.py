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
#include <numeric>
#include <algorithm>
#include <functional>
using namespace std;

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
typedef vector<int> vi;
const int INF = (1LL<<31)-1;

struct data{

    int val,by3,mod;

};

bool cmp( data a,data b ){

    if( a.by3 == b.by3 ){

        if( a.mod == 0 || b.mod == 0 )
            return a.mod < b.mod;

        return a.mod > b.mod;

    }
    return a.by3 < b.by3;
}

int main(){

    freopen("B.txt","r",stdin);
    freopen("B_Out.txt","w",stdout);
    int t;
    S1(t);

    for(int ca = 1;ca<=t;++ca){

        int N;
        data A[ 105 ];
        S1(N);

        int S,p;
        S2(S,p);

        int m;
        for(int i = 0;i<N;++i){

            S1(m);
            A[i].val = m;
            A[i].by3 = m/3;
            A[i].mod = m%3;

        }
        sort( A,A+N,cmp );

        bool taken[ 105 ] = {false};

        for(int k = 0;k<S;++k){

            for(int i = 0;i<N;++i)if( !taken[i] && A[i].val ){

                int sum = A[i].by3 + ( (A[i].mod > 1)?2:1 );
                if( sum >= p ){
                    taken[i] = true;
                    break;
                }

            }

        }
        for(int i = 0;i<N;++i)if( !taken[i] )
            if( ( A[i].by3 + (int)(A[i].mod > 0) ) >= p )
                taken[i] = true;

        printf("Case #%d: %d\n",ca,accumulate(taken,taken+N,0));

    }

	return 0;

}
