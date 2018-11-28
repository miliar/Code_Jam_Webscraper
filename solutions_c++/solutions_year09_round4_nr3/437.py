// Author: Adam Polak
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <cmath>
#include <ctime>
#include <cstdlib>
using namespace std;
const int NIL = (-1);

#define REP(i,n) for(int i=0;i<(n);i++)
#define SIZE(c) ((int)((c).size()))

#define mp make_pair
#define st first
#define nd second
#define pb push_back

int n,k;
const int INF = 1000*1000*1000;
const int N = 111;
int p[N][N];
int g[N][N];

bool eee(int a, int b) {
    if (a==b) return 0;
    REP(i,k) {
        if (p[a][i]==p[b][i]) return 1;
        if ((p[a][i]>p[b][i])!=(p[a][0]>p[b][0])) return 1;
    }
    return 0;
}



int color() {
    stack<int> s;
    int d[N];
    REP(i,n) {
        d[i]=0;
        REP(j,n) d[i]+=g[i][j];
    }
    REP(z,n) {
        int best=0;
        REP(i,n) if(d[i]<d[best]) best = i;
        s.push(best);
        REP(i,n) if(g[best][i]) d[i]--;
        d[best]=INF;
    }
    int c[N];
    REP(i,n) c[i]=NIL;
    while(!s.empty()) {
        int v = s.top(); s.pop();
        REP(i,n) d[i]=0;
        REP(i,n) if(g[v][i]&&c[i]!=NIL) d[c[i]]=1;
        c[v] = 0;
        while(d[c[v]]) c[v]++;
    }
    int best = c[0];
    REP(i,n) best=max(best,c[i]);
    return best+1;
}



void scase(int case_num) {
    scanf("%d%d",&n,&k);
    REP(i,n) 
        REP(j,k) scanf("%d",&p[i][j]);
    REP(i,n) REP(j,n) g[i][j]=eee(i,j);
    
    printf("Case #%d: %d\n",case_num,color());
}

int main() {
    int cases; 
    scanf("%d",&cases);
    //cin >> cases;
    REP(case_num,cases) 
        scase(case_num+1);
    return 0;
}

    
