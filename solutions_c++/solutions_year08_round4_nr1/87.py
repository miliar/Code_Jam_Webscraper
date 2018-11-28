#include<algorithm>
#include<sstream>
#include<string>
#include<vector>
#include<iostream>
#include<cstdio>
using namespace std;

#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
typedef long long ll;

int n, m, v;
int cache[10010][2];
int child[10010][2];
int current_gate[10010];
int changable[10010];

const int inf = 987654321;

int gateResult(int gate, int a, int b)
{
    if(gate) return a && b ? 1 : 0;
    return a || b ? 1 : 0;
}

int go(int here, int desired)
{
    int& ret = cache[here][desired];
    if(ret != -1) return ret;
    ret = inf;
    REP(gate_at_here,2)
    {
        if(!changable[here] && gate_at_here != current_gate[here]) continue;
        int add = 0;
        if(gate_at_here != current_gate[here]) ++add;
        REP(left,2) REP(right,2)
        {
            int res = gateResult(gate_at_here, left, right);
            if(res != desired) continue;
            int cand = add + go(here*2, left) + go(here*2+1, right);
            ret <?= cand;
        }
        
    }
    return ret;
}

int main()
{
    int cases;
    cin >> cases;
    REP(cc,cases)
    {
        CLEAR(cache,-1);
        CLEAR(child,-1);
        cin >> m >> v;
        int internal = (m-1)/2;
        int external = m - internal;
        CLEAR(current_gate,-1);
        CLEAR(changable,-1);
        FOR(i,1,internal+1)
        {
            cin >> current_gate[i] >> changable[i];
        }
        FOR(i,internal+1,m+1)
        {
            int state;
            cin >> state;
            cache[i][state] = 0;
            cache[i][1-state] = inf;
        }
        int ret = go(1, v);
        printf("Case #%d: ", cc+1);
        if(ret >= inf)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ret);
    
}

