#include <iostream>
#include <cstdio>
#include <memory.h>
#include <cstring>
#include <cmath>

#include <vector>
#include <deque>
#include <queue>

#define ABS(a) ((a)<0?-(a):(a))
#define SIGN(a) ((a)<0?-1:((a)>0?1:0))
#define SQR(a) ((a)*(a))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))

#define REP(i, n) for(int i=0; i<(n); ++i)
#define FOR(i, a, b) for(int i=(a); i<(b); ++i)

#define in ({int x;scanf("%d", &x);x;})

#define PI   (3.1415926)
#define INF  (2147483647)
#define INF2 (1073741823)
#define EPS  (0.000001)
#define y1 stupid_cmath

typedef long long LL;

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

    LL prime[1000000], i=0, lp=1, j;
    prime[0]=2;

    for(i=3;i<5000000;i+=2){
        for(j=0;SQR(prime[j])<=i;++j)
            if(i%prime[j]==0) break;
        if(SQR(prime[j])>i) prime[lp++]=i;
    }

    int T;

    cin>>T;
    for(int ii=1;ii<=T;++ii){

        LL N, t;
        cin>>N;
        if(N==1){
            printf("Case #%d: 0\n", ii);
            continue ;
        }
        int res=1;
        for(i=0;SQR(prime[i])<=N;++i){
            t=prime[i];
            for(j=1;t<=N;++j)t*=prime[i];
            res+=j-2;
        }

        printf("Case #%d: %d\n", ii, res);

    }


	return 0;
}
