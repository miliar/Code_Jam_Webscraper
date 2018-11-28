
// Headers {{{
#include<cassert>
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
inline int ABS(int a) { return a>0?a:-a; } 

int main()
{
    int T,n; 
    char buf[1111]; 

    scanf("%d", &T); 

    FOR(tc,1,T) { 
        scanf("%d",&n); 
        VI v;         
        REP(j,n) { 
            scanf("%s",buf); 
            int pos = 0; 
            REP(i,n) if (buf[i] == '1') pos = i;             
            v.PB(pos); 
        } 
        int res = 0; 
        REP(i,n) { 
            if (v[i] > i) { 
                FOR(j,i+1,n-1) if (v[j] <= i) { 
                    int a = v[j]; 
                    FORD(z,j,i+1) v[z] = v[z-1]; 
                    v[i] = a; 
                    res += j - i; 
                    break; 
                } 
            } 
        }  
        printf("Case #%d: %d\n",tc,res); 
    } 


	return 0;
}

