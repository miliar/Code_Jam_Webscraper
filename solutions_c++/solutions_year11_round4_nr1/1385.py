#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include<string.h>
using namespace std;

#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))

#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define V vector
#define FST first
#define SEC second
#define bc __builtin_popcount
typedef V<int> VI;
typedef long long LL;
typedef pair<int, int> PII;
typedef long long LL;

struct E{
    int d, s;
};
E ed[2000];

int fn(E x, E y){
    return x.s<y.s;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("o.txt", "w", stdout);
    int T=SS;
    FOR(tt,1,T+1){
        cout<<"Case #"<<tt<<": ";
        int X, S, R, t, N;
        cin>>X>>S>>R>>t>>N;
        int val = 0;
        REP(i, N){
            int x = SS, y=SS;
            ed[i].d = y-x;
            val+=y-x;
            ed[i].s=S+SS;
        }
        ed[N].d = X-val;
        ed[N].s=S;
        sort(ed, ed+N+1, fn);
        double left = t;
        double ans = 0.0;
//        cout<<left<<" *** ";
       // REP(i, N+1) cout<<ed[i].d<<" "<<ed[i].s<<endl;
        REP(i, N+1){
            if (ed[i].d/(0.0+ed[i].s+R-S)<=left){
                left-=ed[i].d/(0.0+ed[i].s+R-S);
                ans+=ed[i].d/(0.0+ed[i].s+R-S);
            }
            else{
                ans+=left;
                //cout<<"else "<<ans<<endl;
                ed[i].d-=(ed[i].s+R-S)*left;
                ans+=ed[i].d/(double)ed[i].s;
               // cout<<"else "<<ans<<endl;
                left = 0.0;
            }
        }
        printf("%.6lf\n", ans);
    }
    return 0;
}
