
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

int v[1111]; 
int x[1111]; 

int main()
{
    int T,TT,N,K,B; 
    scanf("%d",&T); 
    FOR(tc,1,T) { 
        scanf("%d%d%d%d",&N,&K,&B,&TT); 
        REP(i,N) scanf("%d", &x[i]); 
        REP(i,N) scanf("%d", &v[i]); 
        
        int ret = 0, cc = 0; 

        FORD(i,N-1,0) if ((B-x[i]) > v[i] * TT) { 
            ++cc; 
        }         
        else { 
            if (K) { 
                ret += cc;  
                --K; 
            } 
        }

        if (K == 0) { 
            printf("Case #%d: %d\n",tc,ret); 
        } 
        else  { 
            printf("Case #%d: IMPOSSIBLE\n",tc); 
        } 

    } 
	return 0;
}

