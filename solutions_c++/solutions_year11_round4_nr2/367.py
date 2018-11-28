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
    int T;
    cin>>T;
    for(int ii=1;ii<=T;++ii){

        int r, c, d;
        cin>>r>>c>>d;
        int i, j, k;
        char mm[999][999];
        for(i=0;i<r;++i) cin>>mm[i];

        k=MIN(r, c);
        double x, y;
        int i1, j1;
        bool f=false;
        for(;k>=3 && !f;--k){
            for(i=0;i+k<=r && !f;++i)
                for(j=0;j+k<=c && !f;++j){
                    x=y=0.0;
                    for(i1=0;i1<k;++i1) for(j1=0;j1<k;++j1){
                        if(i1==0 && j1==0 ||
                           i1==k-1 && j1==0 ||
                           i1==0 && j1==k-1 ||
                           i1==k-1 && j1==k-1) continue;

                        x+=((j+j1+0.5)-(j+k*0.5))*(mm[i+i1][j+j1]-'0'+d);
                        y+=((i+i1+0.5)-(i+k*0.5))*(mm[i+i1][j+j1]-'0'+d);
                    }
                    if(ABS(x)<EPS && ABS(y)<EPS){
                        printf("Case #%d: %d\n", ii, k);
                        f=true;
                    }
                }
        }

        if(!f) printf("Case #%d: IMPOSSIBLE\n", ii);

    }
	return 0;
}
