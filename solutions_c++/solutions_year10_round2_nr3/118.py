#include <algorithm>
#include<iostream>
#include <cstdio>
#include <vector>
using namespace std;

#define REP(i, n) for(int (i)=0; (i)<(n); ++(i))

int T[520][520];

void compute(){
    REP(i, 510) T[i][0] = 0;
    REP(i, 510) T[0][i] = 1;
    for(int i=1; i<510; ++i) for(int j=1; j<510; ++j){
        T[i][j] = 0;
        for(int k=max(0, i-j); k<i; ++k) T[i][j] = (T[i][j] + T[k][j]) % 100003;
    }
    
    //REP(i, 16) { REP(j, 16) cout << T[i][j] << ' '; cout << endl; }
}

int testcase(){
    int n; scanf("%d", &n); n--;
    int s = 0;
    REP(i, n){
        s += T[i][n-i];
        s%=100003;
    }
    return s;
}

int main(){

compute();

int z; scanf("%d", &z);
REP(i, z) {
    printf("Case #%d: %d\n", i+1, testcase());
}
return 0;
}

