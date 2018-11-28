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

        int x, s, r, t, n, m[1000][3];
        cin>>x>>s>>r>>t>>n;

        int i, l=0;
        for(i=0;i<n;++i) {
            cin>>m[i][0]>>m[i][1]>>m[i][2];
            l+=m[i][1]-m[i][0];
        }
        m[n][0]=0;m[n][1]=x-l;m[n][2]=0;
        ++n;
        for(i=0;i<n-1;++i)
            if(m[i][2]>m[i+1][2]){

                l=m[i][0];
                m[i][0]=m[i+1][0];
                m[i+1][0]=l;

                l=m[i][1];
                m[i][1]=m[i+1][1];
                m[i+1][1]=l;

                l=m[i][2];
                m[i][2]=m[i+1][2];
                m[i+1][2]=l;

                if(i) i-=2;

            }

        double res=0, tmp;

        for(i=0;i<n;++i){
            if(res>=t) res+=(m[i][1]-(double)m[i][0])/(m[i][2]+s);
            else{
                tmp=(m[i][1]-(double)m[i][0])/(m[i][2]+r);
                if(tmp+res<=t) res+=tmp;
                else{
                    tmp=t-res;
                    res=t;
                    res+=(m[i][1]-(double)m[i][0]-tmp*(m[i][2]+r))/(m[i][2]+s);
                }
            }
        }

        printf("Case #%d: %.8lf\n", ii, res);

    }
	return 0;
}
