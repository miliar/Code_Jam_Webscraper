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
	int N;
	cin>>N;
	for(int ii=1;ii<=N;++ii){
        int k;
        cin>>k;
        int o=1, b=1, a, to=0, tb=0, t=0;
        char c;
        for(int j=0;j<k;++j){
            cin>>c>>a;
            if(c=='O'){
                to+=ABS(a-o);
                to=MAX(to, t);
                ++to;
                o=a;
                t=MAX(t, to);
            }else{
                tb+=ABS(a-b);
                tb=MAX(tb, t);
                ++tb;
                b=a;
                t=MAX(t, tb);
            }
        }
        printf("Case #%d: %d\n", ii, t);
	}
	return 0;
}
