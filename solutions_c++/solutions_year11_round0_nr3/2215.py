#include <iostream>
#include <cstdio>
#include <memory.h>
#include <cstring>
#include <cmath>

#include <vector>
#include <deque>

#define ABS(a) ((a)<0?-(a):(a))
#define SIGN(a) ((a)<0?-1:((a)>0?1:0))
#define SQR(a) ((a)*(a))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))

#define REP(i, n) for(int i=0; i<(n); ++i)
#define FOR(i, a, b) for(int i=(a); i<(b); ++i)

#define in ({int x;scanf("%d", &x);x;})

#define PI (3.1415926)
#define INF (2147483647)
#define EPS (0.000001)
#define y1 stupid_cmath

typedef long long LL;

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int N=in;
	for(int ii=1;ii<=N;++ii){
        int K, s=0, min=1000000000, i, a, r=0;
        cin>>K;
        for(i=0;i<K;++i){
            cin>>a;
            s+=a;
            r^=a;
            min=MIN(min,a);
        }
        if(r) printf("Case #%d: NO\n",ii);
        else printf("Case #%d: %d\n",ii,s-min);
	}
	return 0;
}
