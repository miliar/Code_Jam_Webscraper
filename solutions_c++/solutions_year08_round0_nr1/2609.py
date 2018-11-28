#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef long long int64;

int64 memo[101][1001];

vector<string> names;
vector<string> queries;

int64 DP(int s, int i) {    
    if(i<0)
        return 0;
    else {
        if(memo[s][i] != INT_MAX) return memo[s][i];
        for(int k=0; k<names.size(); ++k) {
            if(names[k] == queries[i]) continue;
            memo[s][i] = min(memo[s][i], s==k?DP(k, i-1):DP(k, i-1)+1);
        }
        return memo[s][i];
    }
}

int main(int argc, char ** argv) {
    freopen("A.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int N;
    scanf("%d", &N);
    for(int iCaso=0; iCaso<N; ++iCaso) {
        int S;
        scanf("%d\n", &S);
        names = vector<string>(S);
        char buffer[128];
        for(int i=0; i<S; ++i) {
            fgets(buffer, sizeof(buffer), stdin);
            names[i] = string(buffer);
        }
        int Q;
        scanf("%d\n", &Q);
        queries = vector<string>(Q);
        for(int i=0; i<Q; ++i) {
            fgets(buffer, sizeof(buffer), stdin);
            queries[i] = string(buffer);
        }
        for(int i=0; i<101; ++i) for(int j=0; j<1001; ++j) memo[i][j] = INT_MAX;
        for(int i=0; i<S; ++i)
            DP(i, Q-1);
            
        int mini = 0;
        for(int i=1; i<S; ++i){
            if(memo[mini][Q-1] > memo[i][Q-1])
                mini = i;
        }
        printf("Case #%d: %d\n", iCaso+1, memo[mini][Q-1]);
    }
    return 0;
}
