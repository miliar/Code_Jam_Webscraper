#include <algorithm>
#include<iostream>
#include <cstdio>
#include <vector>
using namespace std;

#define REP(i, n) for(int (i)=0; (i)<(n); ++(i))

#define INF 100000

void testcase(){
    int n, k, b, t; scanf("%d%d%d%d", &n, &k, &b, &t);
    vector<int>x; x.resize(n);
    REP(i, n) {
        scanf("%d", &x[i]);
    }
    vector<int>v; v.resize(n);
    REP(i, n) {
        scanf("%d", &v[i]);
    }

    vector<bool> able(n, false);
    
    REP(i, n){
        if ( (b - x[i]) <= t * v[i] ) able[i] = true;
    }
    
    vector<int> w(n, 0);
    int all = 0;
    
    REP(i, n){
        if ( able[i] ) all++; else w[i] = INF;
        for(int j=i+1; j<n; ++j){
            if ( ! able[j] ) w[i]++;
        }
    }
    
    if (all < k){
        printf("IMPOSSIBLE\n");
        return;
    }
    
    int s = 0;
    sort(w.begin(), w.end());
    REP(i, k) s+=w[i];
    printf("%d\n", s);
}

int main(){
int z; scanf("%d", &z);
REP(i, z) {
    printf("Case #%d: ", i+1);
    testcase();
}
return 0;
}
