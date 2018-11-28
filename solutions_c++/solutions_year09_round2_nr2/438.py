
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

char buf[100]; 

int main()
{
    int T; 
    scanf("%d",&T); 

    FOR(tc,1,T) {
        printf("Case #%d: ",tc); 
        scanf("%s",buf); 
        int d = strlen(buf); 
        if (!next_permutation(buf, buf + d)) { 
            sort(buf, buf + d); 
            string x = ""; 
            int zeros = 1; 
            REP(i,d) if (buf[i] != '0') x += buf[i]; 
            else ++zeros; 
            printf("%c",x[0]); 
            REP(i,zeros) printf("0"); 
            FOR(i,1,SIZE(x)-1) printf("%c",x[i]); 
            puts(""); 
        } 
        else printf("%s\n",buf); 
    }



	return 0;
}

