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

int m[110][110], m2[110][110];

int main() {
    int nt, ct;
    
    scanf(" %d", &nt);
    for (ct=1; ct<=nt; ct++) {
        int r;
        scanf(" %d",&r);
        FILL(m, 0);
        
        int x1,x2,y1,y2;
        REP(i,r) {
            scanf(" %d %d %d %d", &x1,&y1,&x2,&y2);
            FOR(p, x1, x2)
                FOR(q, y1, y2) m[p][q]=1;
        }
        
        int res=0;
        while (1) {
            bool deu=true;
            
            REP(i, 101)
                REP(j, 101) if (m[i][j]==1) deu=false;
                
            if (deu) break;
            res++;
            
            REP(i, 101)
                REP(j, 101) {
                    if (i && j && m[i][j]==1 && m[i-1][j]==0 && m[i][j-1]==0) m2[i][j]=0;
                    else if (i && j && m[i][j]==0 && m[i-1][j]==1 && m[i][j-1]==1) m2[i][j]=1;
                    else m2[i][j]=m[i][j];
                }
                
            memcpy(m, m2, sizeof(m));
        }
        
        printf("Case #%d: %d\n",ct, res);
    }
    
    return 0;
}

