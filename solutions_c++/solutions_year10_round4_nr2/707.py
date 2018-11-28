#include  <cstdio> 
#include  <cstdlib> 
#include  <cstring> 
#include  <string> 
#include  <vector> 
#include  <cmath> 
#include  <algorithm> 
#include  <cassert> 
#include  <set> 
#include  <map> 
#include  <queue> 
#include  <iostream> 
#include <fstream> 
using namespace std; 
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )  

typedef long long LL; 
typedef pair<int,int> pii; 

int M[2048];

int dfs(int L, int R){
    bool suc = true;
    if (L == R) {
        return 0;
    }
    for (int i = L; i <= R; ++i){
        if (M[i]) {
            M[i]--;
            suc = false;
        }
    }
    if (suc)
        return 0;
    return dfs(L, (L + R) / 2) + dfs((L + R) / 2 + 1, R) + 1;
}

int main()
{
    int cn;
    scanf("%d", &cn);
    for (int ci = 1; ci <= cn; ci++) {
        printf("Case #%d: ", ci);
        int N;
        scanf("%d", &N);
        REP(i, (1 << N)) {
            scanf("%d", M + i);
            M[i] = N - M[i];
        }
        int tmp;
        REP(i, (1 << N) - 1)
            scanf("%d", &tmp);
        printf("%d\n", dfs(0, (1 << N) - 1));
    }
    return 0;
}
