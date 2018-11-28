
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

VS v; 
char buf[100000]; 
const int max_l = 20; 
set<char> s[max_l]; 
int L,D,N; 


int main()
{
    scanf("%d%d%d",&L, &D, &N); 
    REP(i,D) { 
        scanf("%s",buf); 
        v.PB(buf);         
    } 

    FOR(T,1,N) {
        scanf("%s",buf);        
        REP(i,max_l) s[i].clear(); 
        int pos = 0, l = strlen(buf), op = 0; 
        REP(i,l) { 
            if (isalpha(buf[i])) { 
                s[pos].insert(buf[i]);             
                if (!op) ++pos; 
            } 
            else { 
                if (buf[i] == '(') op = 1; 
                else if (buf[i] == ')') { 
                    op = 0; 
                    ++pos; 
                } 
            } 
        } 
        int ret = 0, ok; 

        FORE(e,v) { 
            ok = 0; 
            REP(i,L) if (s[i].count((*e)[i])) ++ok; 
            if (ok == L) ++ret; 
        } 
        printf("Case #%d: %d\n",T,ret);        
    } 




	return 0;
}

