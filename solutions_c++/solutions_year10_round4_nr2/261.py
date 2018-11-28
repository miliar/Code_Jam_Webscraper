
// Headers {{{
#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
using namespace std;
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define VAR(V,init) __typeof(init) V=(init)
#define FORE(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define CLR(A,v) memset((A),v,sizeof((A)))
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define SIZE(x) (int)(x.size())
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long LL;
typedef long double LD; 
typedef vector<string> VS;
// }}}

const int max_P = 12; 
const int inf = (1<<29); 
int miss[(1<<max_P)], res[max_P][(1<<max_P)]; 
int cost[(1<<max_P)]; 

int main()
{
    int T,P; 
    scanf("%d", &T); 

    FOR(tc,1,T) { 
        scanf("%d",&P); 
        int sh = (1<<(P-1)); 
        REP(i,sh*2) { 
            scanf("%d",&miss[sh*2+i]); 
        } 
        int tmp = sh; 

        REP(j,max_P) REP(i,sh*2) res[j][i] = inf; 

        while (tmp) { 
            REP(i,tmp) scanf("%d", &cost[tmp+i]); 
            tmp /= 2; 
        }

        REP(i,sh) { 
            int mm = min(miss[sh*2+i*2], miss[sh*2+i*2+1]); 
            res[mm][sh+i] = cost[sh+i]; 
            if (mm > 0) res[mm-1][sh+i] = 0; 
        } 

        FORD(m,sh-1,1) { 
            REP(l,P+1) REP(r,P+1) { 
                int mm = min(l,r); 
                res[mm][m] = min(res[mm][m], res[l][m*2] + res[r][m*2+1] + cost[m]); 
                if (mm > 0) res[mm-1][m] = min(res[mm-1][m], res[l][m*2] + res[r][m*2+1]); 
            }                 
        } 
        /* 
        FOR(i,1,sh*2-1) { 
            printf("%d : ", i); REP(j,P) printf("%d ",res[j][i]); 
            puts(""); 
        }
        */ 

        int ret = inf; 

        REP(i,P+1) ret = min(ret, res[i][1]); 
        printf("Case #%d: %d\n",tc,ret);      
    } 
  

	return 0;
}

