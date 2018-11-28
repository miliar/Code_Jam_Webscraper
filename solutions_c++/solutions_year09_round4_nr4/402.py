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

int n;
double x[3],y[3],r[3];

double g(int a, int b) {
    return 0.5*(r[a]+r[b]+sqrt((x[a]-x[b])*(x[a]-x[b])+(y[a]-y[b])*(y[a]-y[b])));
}

double f() {
    if (n==1) return r[0];
    if (n==2) return max(r[0],r[1]);
    double best = 1000000.0;
    best = min(best,max(r[0],g(1,2)));
    best = min(best,max(r[1],g(2,0)));
    best = min(best,max(r[2],g(0,1)));
    return best;
}

void scase(int case_num) {
    scanf("%d",&n);
    REP(i,n) scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
    printf("Case #%d: %0.6lf\n",case_num,f());
}

int main() {
    int cases; 
    scanf("%d",&cases);
    //cin >> cases;
    REP(case_num,cases) 
        scase(case_num+1);
    return 0;
}

    
