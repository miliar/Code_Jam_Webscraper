
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

const int P = 100003; 

const int max_n = 500; 
int c[666][666]; 
int pas[666][666]; 

int main()
{
    int T,n; 
    scanf("%d", &T); 
    CLR(pas,0); 
    FOR(i,0,max_n) pas[i][0] = pas[i][i] = 1; 
    FOR(i,2,max_n) FOR(j,1,i-1) pas[i][j] = (pas[i-1][j] + pas[i-1][j-1])%P; 

    CLR(c,0); 
    FOR(i,2,max_n) c[i][1] = 1;     

    FOR(nn,3,max_n) { 
        FOR(last,2,nn) FOR(cc,1,last) if (c[last][cc]) { 
            c[nn][last] = (c[nn][last] + (LL)c[last][cc] * pas[nn-last-1][last-cc-1]) % P; 
        } 
    } 

    FOR(tc,1,T) { 
        scanf("%d",&n);
        int sm = 0; 
        FOR(i,1,n) sm += c[n][i]; 
        printf("Case #%d: %d\n",tc,sm%P); 

    } 

	return 0;
}

