#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <float.h>

using namespace std;

// prewritten code

#define sz(x) (int)(x).size()
#define all(c) (c).begin(),(c).end()
#define Fill(a,b) memset(&a,b,sizeof(a))
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define pb push_back

#define GDB 1
#define DBG(x) if(GDB){cerr << #x <<" = "<< x << endl;}
#define DBGA(x) if(GDB){cerr << #x <<": "; for (int i=0; i<(int)sizeof(x)/(int)sizeof(x[0]); ++i) cerr<<x[i]<<' '; cerr<<endl;}
#define DBGV(x) if(GDB){cerr << #x <<": "; for (int i=0; i<(int)sz(x); ++i) cerr<<x[i]<<' '; cerr<<endl;}

// real code
string problem_name="c";
void init(){
    freopen( (problem_name+".in").c_str(),"rt",stdin);
    freopen( (problem_name+".out").c_str(),"wt",stdout);
}
#define oo 1000*1000*1000
int p;
vector<int> ll;
long long solve(){
    long long ret=0;
    int i,j;
    int l,r,d;
    //DBGV(ll);
    for(i=0;i<sz(ll);i++){
        r=p+1;
        l=0;
        for(j=0;j<i;j++){
            if(ll[j]<ll[i]&&ll[j]>l) l=ll[j];
            if(ll[j]>ll[i]&&ll[j]<r) r=ll[j];
        }
        d=r-l-2;
        //DBG(d);
        ret+=d;
    }
    return ret;
}
int main(){
    init();
    int i;
    int q;
    int T,tt;
    long long ret,d;
    scanf("%d",&T);
    for(tt=1;tt<=T;tt++){
        scanf("%d %d",&p,&q);
        ll.resize(q);
        ret=oo;
        for(i=0;i<q;i++) scanf("%d",&ll[i]);
        sort(all(ll));
        do{
            d=solve();
            ret=Min(d,ret);
        }while(next_permutation(all(ll)));
        printf("Case #%d: %lld\n",tt,ret);
    }
    return 0;
}
