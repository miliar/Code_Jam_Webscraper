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
    int NN;
    cin>>NN;
    for(int ii=1;ii<=NN;++ii){

        LL N, P, G;
        cin>>N>>P>>G;

        if(G==0 && P!=0 || G==100 && P!=100) printf("Case #%d: Broken\n", ii);
        else {
            LL a=100, b=P;
            while(a) a^=b^=a^=b%=a;
            if(N<100/b) printf("Case #%d: Broken\n", ii);
            else printf("Case #%d: Possible\n", ii);
        }

    }
	return 0;
}
