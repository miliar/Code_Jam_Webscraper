
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

const int maxN=1111; 

VI v[maxN]; 
bool lf[maxN],vis[maxN]; 
int M[maxN]; 

bool dfs(int w){ 
   vis[w]=1; 
   FORE(e,v[w])
	   if(M[*e]==-1 || (!vis[M[*e]] && dfs(M[*e]) )){ 
		   M[*e]=w; 
		   M[w]=*e; 
		   return 1; 
	   } 
   return 0; 
} 

int matching(int n){
	REP(i,n) M[i]=-1; 
	bool ch=1; 
   while(ch){
	   ch=0; 
	   CLR(vis,0); 
	   REP(i,n) if(lf[i] && !vis[i] && M[i]==-1 && dfs(i))ch=1; 
    } 
    int ret =0; 
    REP(i,n) if (M[i] != -1) ++ret; 
    return ret / 2; 
} 

int n,m; 
int t[1111][1111]; 
int T; 

bool can(int a, int b) { 
    bool ok2 = 1; 
    REP(i,m) {    
        if (t[a][i] <= t[b][i]) ok2 = 0; 
    } 
    return ok2;     
} 


int main()
{
    scanf("%d", &T);     

    FOR(tc,1,T) { 
        scanf("%d%d",&n,&m); 
        REP(i,n) REP(j,m) scanf("%d",&t[i][j]); 
        REP(i,maxN) v[i].clear(); 
        REP(i,n) REP(j,n) if (can(i,j)) { 
            v[i].PB(j+n); 
            v[j+n].PB(i); 
        } 

        REP(i,n) lf[i] = 1; 
        printf("Case #%d: %d\n",tc,n-matching(2*n));         
    } 

	return 0;
}

