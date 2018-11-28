
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

const int max_s = 111; 
int t[2][max_s][max_s]; 

int main()
{
    int T,R; 
    scanf("%d", &T); 
    FOR(tc,1,T) { 
        CLR(t,0); 
        
        scanf("%d", &R); 
        int N = 0; 
        REP(ii,R) { 
             int x1,y1,x2,y2; 
             scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
             N = max(N, x2); N = max(N, y2); 
             FOR(i,x1,x2) FOR(j,y1,y2) t[0][j][i] = 1;      
        } 

        int x = 0, y = 1, iters = 0; 

        while (1) { 
            FOR(i,1,N) FOR(j,1,N) t[y][i][j] = 0; 
            bool ok = 0; 
            FOR(i,1,N) FOR(j,1,N) { 
                if (t[x][i][j] && (t[x][i-1][j] || t[x][i][j-1])) { 
                    t[y][i][j] = 1; 
                    ok = 1; 
                } 

                if (t[x][i-1][j] && t[x][i][j-1]) { 
                    t[y][i][j] = 1; 
                    ok = 1; 
                } 
             } 
            ++iters; 
            swap(x,y);  
            if (!ok) break; 
            //FOR(i,1,N) { FOR(j,1,N) printf("%d ",t[y][i][j]); puts(""); } 
            //puts("");             
//            if (iters == 10) break; 
        }          

        printf("Case #%d: %d\n",tc,iters); 

    } 

	return 0;
}

