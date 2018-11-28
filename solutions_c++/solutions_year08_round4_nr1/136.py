// GCJ '08 
// Question A
// Solution by sql_lall
#include <map>
#include <cmath>
#include <queue>
#include <deque>
#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int nCases;

int gate[10001];
int canChange[10001];
int minToMake[10001][2];
int M, V; 

inline int AND(int a, int b){return a & b;}
inline int OR(int a, int b){return a | b;}
inline int min(int a, int b, int c){return min(a, min(b, c));}

int solve(){
    scanf("%d %d", &M, &V);
    int i = 0;
    while(i < (M-1)/2){
        scanf("%d %d", gate + i, canChange + i);
        i++;
    }
    while(i < M){
        scanf("%d", gate + i); canChange[i] = 3;
        i++;
    }
    
    int INF = 5 * M;
    for(int i = M - 1; i >= 0; i--){
        minToMake[i][0] = minToMake[i][1] = INF;
        int lc = 2 * i + 1, rc = lc + 1;
        if(canChange[i] == 3){ // leaf
            minToMake[i][gate[i]] = 0;
        } else {
            int or0 = minToMake[lc][0] + minToMake[rc][0];
            int or1 = min( minToMake[lc][1] + minToMake[rc][0], 
                           minToMake[lc][0] + minToMake[rc][1],
                           minToMake[lc][1] + minToMake[rc][1]);                                       
            int nd1 = minToMake[lc][1] + minToMake[rc][1];
            int nd0 = min( minToMake[lc][1] + minToMake[rc][0], 
                           minToMake[lc][0] + minToMake[rc][1],
                           minToMake[lc][0] + minToMake[rc][0]);     
            if(gate[i] == 0){
                minToMake[i][0] = or0;
                minToMake[i][1] = or1;
                if(canChange[i] == 1){
                    minToMake[i][0] = min(or0, 1 + nd0);
                    minToMake[i][1] = min(or1, 1 + nd1);
                }
            } else if(gate[i] == 1){
                minToMake[i][0] = nd0;
                minToMake[i][1] = nd1;
                if(canChange[i] == 1){
                    minToMake[i][0] = min(1 + or0, nd0);
                    minToMake[i][1] = min(1 + or1, nd1);
                }
            }
        }
    }
    
    int ret = minToMake[0][V];
    if(ret >= INF) return -1;
    return ret;
}

int main(){
    scanf("%d", &nCases);
    for(int c = 1; c <= nCases; c++){
        printf("Case #%d: ", c);
        int soln = solve();
        if(soln == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", soln);
    }
}
