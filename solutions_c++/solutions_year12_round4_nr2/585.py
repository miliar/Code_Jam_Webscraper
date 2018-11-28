#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<time.h>
#include<assert.h>

#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

#define FOR(i,n) for(int i=0;i<(n);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define CLR(a,x) memset(a,(x),sizeof(a))

typedef long long LL;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;

vector<pii> sq;
int N,W,L;

const double eps = 0.000000001;

pdd ans[1005];

inline bool eql(double a, double b){
    return fabs(a-b)<eps;
}

inline void Update(double& ret, double val){
    if(ret<0.0) ret = val;
    else ret = min(ret, val);
}

inline bool interSect(int j, double x, double y, double r){
    double xj = ans[j].first, yj = ans[j].second, rj = sq[j].first;

    return !( (fabs(xj-x)+eps>r+rj) || (fabs(yj-y)+eps>r+rj) );
}

bool canBePlaced(LL x2, int i, double y){
    double x = double(x2)/2.0;

    if(x<0.0 || y<0.0) return false;
    if(x>double(W) || y>double(L)) return false;

    FOR(j,i){
        if(interSect(j,x,y,sq[i].first))
            return false;
    }

    return true;
}

double F(LL x2, int i){
    double ret = -1.0;

    FOR(j,i){
        double candidates[] = {ans[j].second-sq[j].first, ans[j].second, ans[j].second+sq[j].first};
        double delta[] = {0.0, -sq[i].first, sq[i].first};

        FOR(k,3){
            FOR(a,3){
                if(canBePlaced(x2,i,candidates[k]+delta[a])){
                    Update(ret, candidates[k]+delta[a]);
                }
            }
        }
    }

    return ret;
}

pdd findPos(int i){
    LL lo = 0, hi = W*2LL;

    double tmp = F(0.0, i);

    if( !eql(tmp,-1.) ){
        return pdd(0.0, tmp);
    }

    while(hi-lo>1){
        LL mid=(hi+lo)>>1;

        if(!eql(F(mid,i),-1)){
            hi = mid;
        }else{
            lo = mid;
        }
    }

    return pdd(double(hi)/2.,F(hi,i));
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B_large.out","w",stdout);

 //   freopen("test.in","r",stdin);
  //  freopen("test.out","w",stdout);

    int T; scanf("%d",&T);

    REP(t,1,T){
        scanf("%d%d%d",&N,&W,&L);

        sq.clear();

        FOR(i,N){
            int r; scanf("%d",&r);
            sq.push_back(pii(r,i));
        }

        sort(sq.begin(),sq.end());
        reverse(sq.begin(),sq.end());

        ans[0] = pdd(0.,0.);

        FOR(i,N)if(i){
            pdd pos = findPos(i);
            ans[i] = pos;
        }

        pdd realAns[1005];

        FOR(i,N){
            realAns[sq[i].second] = ans[i];
        }

        printf("Case #%d:",t);
        FOR(i,N)
            printf(" %.1lf %.1lf",realAns[i].first,realAns[i].second);

        puts("");
    }

    return 0;
}
