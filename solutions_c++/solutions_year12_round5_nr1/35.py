#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <fstream>
using namespace std;
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )
typedef long long LL;
typedef pair<int, int> pii;

double eps  = 1e-8;

double g(pii p1, pii p2) {
    return (p1.first * 100.0 / (100 - p1.second) + p2.first) * 100.0 / (100 - p2.second);
}

struct s {
    pii t;
    int index;
};

bool operator  <(const s& p1, const s& p2) {
    double r1 = g(p1.t, p2.t), r2 = g(p2.t, p1.t);
    if (fabs(r1 - r2) < eps) {
        return p1.index < p2.index;
    }
    return r1 < r2;
}

s b[2014];

int main(){
    int caseNumber;
    //scanf("%d", &caseNumber);
    cin>>caseNumber;
    int r;
    REP(caseN, caseNumber) {
    	int N;
    	cin>>N;
    	REP(i, N) {
            cin>>r;
            b[i].index = i;
            b[i].t  = make_pair(r, 0);
        }
    	REP(i, N) {
    		cin>>r;
    		b[i].t.second = r;
    	}
        //REP(i, N) REP(j, N) printf("%d %d %.4lf\n", i, j, g(b[i].t, b[j].t));
    	sort(b, b + N);
    	printf("Case #%d:", caseN + 1);
    	REP(i, N)
    		printf(" %d", b[i].index);
    	puts("");
    }
    return 0;
}