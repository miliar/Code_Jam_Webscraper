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
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second
#define bc __builtin_popcount
typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;


typedef long long LL;


double wp[100],owp[100],oowp[100];
S g[100];
int n;
double sol(int a, int ex){
    int l=0,w=0;
    REP(i,n){
        if (i!=a && i!=ex){
            if (g[a][i]=='0') l++;
            else if (g[a][i]=='1') w++;
        }
    }
    return w/(w+l+0.0);
}

double solve(int ind){
    int c =0;
    double x = 0.0;
    REP(i,n){
        if (g[ind][i]!='.'){
            x += sol(i,ind);
            c++;
        }
    }
    return x/c;
}
double solv(int ind){
    int c= 0;
    double ans = 0.0;
    REP(i,n){
        if (g[ind][i]!='.'){
            ans+=owp[i];
            c++;
        }
    }
    return ans/c;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("o.txt", "w", stdout);
    int t=SS;
    FOR(T,1,t+1){
        n=SS;
        REP(i,n) cin>>g[i];
        REP(i,n){
            int x = count(ALL(g[i]),'0'),y=count(ALL(g[i]),'1');
            wp[i] = y/(x+y+0.0);
        }
        REP(i,n){
            owp[i] = solve(i);
        }
        REP(i,n){
            oowp[i] = solv(i);
        }
        cout<<"Case #"<<T<<":\n";
        REP(i,n){
            printf("%.9lf\n", .25*wp[i]+.5*owp[i]+.25*oowp[i]);
        }
    }
    return 0;
}

