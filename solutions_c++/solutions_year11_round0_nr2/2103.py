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
	char ss[256][256], c1, c2, c3, r[250];
	bool mm[256][256];
	int i, j, lr;
	for(int ii=1;ii<=N;++ii){
        int C, D, K;
        cin>>C;
        memset(ss,0,sizeof(ss));
        memset(mm,0,sizeof(mm));
        r[0]='\0';
        lr=0;
        for(i=0;i<C;++i){
            cin>>c1>>c2>>c3;
            ss[c1][c2]=c3;
            ss[c2][c1]=c3;
        }
        cin>>D;
        for(i=0;i<D;++i){
            cin>>c1>>c2;
            mm[c1][c2]=true;
            mm[c2][c1]=true;
        }
        cin>>K;
        for(i=0;i<K;++i){
            cin>>c1;
            if(!lr){
                r[lr++]=c1;
                continue;
            }
            if(ss[r[lr-1]][c1]){
                r[lr-1]=ss[r[lr-1]][c1];
                continue;
            }
            for(j=0;j<lr;++j) if(mm[r[j]][c1]) break;
            if(j<lr){
                r[0]='\0';
                lr=0;
                continue;
            }
            r[lr++]=c1;
        }
        r[lr]='\0';
        printf("Case #%d: [",ii);
        for(i=0;i<lr-1;++i) printf("%c, ",r[i]);
        if(lr)printf("%c",r[i]);
        printf("]\n");
	}
	return 0;
}
