#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <stdio.h>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i) 
#define FILL(v,x) memset((v), (x), sizeof(v));
#define INF 0x3f3f3f3f
#define EPS 1E-8
typedef long long int64;
typedef pair<int, int > pii;

long long lim[2000], cus[200][2000];
int rem[2000];
int64 pd[20][2000][20];

long long solve(int a, int b, int got) {
    if (a==-1) {
        if (rem[b]<=got) return 0;
        return INF;
    }
    if (pd[a][b][got]!=-1) return pd[a][b][got];
    
    int64 res = INF;
    res= min(res, min(solve(a-1, b*2, got+1) + solve(a-1,b*2+1,got+1) + cus[a][b],
        solve(a-1, b*2, got)+ solve(a-1, b*2+1, got)));
    
    return (pd[a][b][got]=res);
}

int main() {
    int nt, ct;
    
    scanf(" %d", &nt);
    for (ct=1; ct<=nt; ct++) {
        int p, m;
        scanf(" %d" ,&p);
        m = (1<<p);
        
        REP(i, m) {
            scanf(" %lld",&lim[i]);
            rem[i]=p-lim[i];
        }
        
        REP(i, p)
            REP(j, (1<<(p-i-1))) scanf(" %lld",&cus[i][j]);
            
        memset(pd,-1,sizeof(pd));
        int64 res = solve(p-1, 0, 0);
        
        printf("Case #%d: %lld\n",ct, res);
    }
    
    return 0;
}

