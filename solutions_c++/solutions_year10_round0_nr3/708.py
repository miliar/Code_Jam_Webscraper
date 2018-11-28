
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

const int max_n = 1011; 
const int max_l = 30; 
pair<LL, int> mv[max_l][max_n]; 
int g[max_n]; 
int N; 

int next(int a) { 
    ++a; 
    if (a == N) a = 0; 
    return a; 
} 

int main()
{
    int T,R,k; 
    scanf("%d", &T); 


    FOR(tc,1,T) { 
        scanf("%d%d%d",&R,&k,&N); 
        REP(i,N) scanf("%d",&g[i]); 
        LL sm = 0; 
        REP(i,N) sm += g[i]; 
        if (sm <= (LL)k) { 
            printf("Case #%d: %lld\n",tc,sm*R); 
            continue; 
        } 

        REP(i,N) { 
            sm = 0; 
            int a = i; 
            while (sm + g[a] <= k) { 
                sm += g[a]; 
                a = next(a); 
            } 
            mv[0][i] = MP(sm,a); 
        } 


        REP(lev,max_l-1) 
            REP(i,N) { 
                int a = mv[lev][i].SE; 
                mv[lev+1][i] = MP(mv[lev][i].FI + mv[lev][a].FI, mv[lev][a].SE); 
            } 

//        REP(lev,3) { 
  //      REP(i,N) printf("%lld %d\n",mv[lev][i].FI,mv[lev][i].SE); 
    //    puts(""); 
      //  } 

        LL ret = 0; 
        int a = 0, pw = 0; 
        while (R) { 
            if (R&(1<<pw)) { 
                R -= (1<<pw); 
                ret += mv[pw][a].FI;             
                a = mv[pw][a].SE; 
            } 
            ++pw; 
        }         
        printf("Case #%d: %lld\n",tc,ret); 
    } 

	return 0;
}

