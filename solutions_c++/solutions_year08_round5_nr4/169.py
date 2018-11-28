#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VInt;

#define FOR(i, a, b) for(i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define SIZE(a) int((a).size())
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair

#define MOD 10007

int M[MOD];
int H,W,R;
vector<PII> p;

void init(){
    int i;
    M[0]=1;
    for (i=1;i<MOD;i++)
        M[i]=(M[i-1]*i)%MOD;
}

int gC(int n,int m){
    int i,U,D;
	if (n>=MOD || m>=MOD){
		return gC(n/MOD,m/MOD)*gC(n%MOD,m%MOD)%MOD;
	}
	U=M[n];
    if (n<m) return 0;
	D=(M[m]*M[n-m])%MOD;
    for (i=0;i<MOD;i++)
        if (i*D%MOD==U) return i;
    return 0;
}

int count(int dx,int dy){
    int m,n,dif;
    if ((dx+dy)%3) return 0;
    m=(dx+dy)/3;
    dif=dx-dy;
    n=m+dif;
    if (n%2) return 0;
    n/=2;
    if (n<0 || n>m) return 0;
    return gC(m,n);
}

int getNum(int k){
    int i,c,res;
    vector<PII> T;
    T.clear();
    c=2;
    T.PB(MP(1,1));
    for (i=0;i<R;i++){
        if ((1<<i)&k){
            T.PB(p[i]);
            c++;
        }
    }
    T.PB(MP(H,W));
    res=1;
    for (i=0;i<c-1;i++){
        res=(res*count(T[i+1].first-T[i].first,T[i+1].second-T[i].second))%MOD;
    }
    if (c&1) return -res;
    else return res;
}

void solve(int cas){
    int i,k,r,c,res;
    p.clear();
    scanf("%d%d%d",&H,&W,&R);
    for (i=0;i<R;i++){
        scanf("%d%d",&r,&c);
        p.PB(MP(r,c));
    }
    res=0;
    sort(ALL(p));
	RFOR(k,(1<<R),0){
        res+=getNum(k);
        res%=MOD;
    }
    if (res<0) res+=MOD;
    printf("Case #%d: %d\n",cas,res);
}


int main(){
    int t,cas;
    scanf("%d",&t);
    init();
    for (cas=1;cas<=t;cas++)
        solve(cas);
    return 0;
}
