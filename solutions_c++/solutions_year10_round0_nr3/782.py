#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define pb push_back
#define pii pair<int, int>
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

int runs, cap, n;
int group[1111];

ll dp[1111]; // money starting in i
int nextpos[1111];

ll solve()
{
    FOR(i, 0, n){
        int p = 0, pos = i;
        int c = 0;
        while( (p += group[pos]) <= cap){
            c += group[pos];
            pos = (pos+1)%n;
            if(pos == i) break;
        }
        dp[i] = (ll)c;
        nextpos[i] = pos;
    }

    int visited[1111];
    memset(visited, -1, sizeof(visited));

    int pos = 0;
    ll money[1111];
    money[0] = 0;

    int cyclestart = -1;
    int cyclelen;
    ll cyclemoney;

    FOR(i, 0, runs){

        if(visited[pos] != -1){
            cyclestart = pos;
            cyclelen = i - visited[pos];
            cyclemoney = money[i - 1];
            if(visited[pos] > 0) cyclemoney -= money[visited[pos] - 1];

            break;
        }

        visited[pos] = i;
        if(i == 0) money[i] = dp[pos];
        else money[i] = money[i - 1] + dp[pos];
        
        pos = nextpos[pos];
    }

    // Hasnt cycled
    if(cyclestart == -1) return money[runs - 1];

    ll resp = 0;
    
    if(visited[pos] > 0) resp += money[visited[pos] - 1];

    int runsleft = runs - visited[pos];
    
    resp += cyclemoney * (runsleft/cyclelen);
    
    runsleft = runsleft%cyclelen;

    pos = cyclestart;
    FOR(i, 0, runsleft){
        resp += dp[pos];
        pos = nextpos[pos];
    }
    
    return resp;
}

int main()
{
    int testcases;
    scanf("%d", &testcases);

    for(int testcase = 1; testcase <= testcases; testcase++){
        scanf("%d %d %d", &runs, &cap, &n);
        for(int i = 0; i < n; i++){
            scanf("%d", &group[i]);
        }

        printf("Case #%d: %lld\n", testcase, solve());
    }
    return 0;
}

