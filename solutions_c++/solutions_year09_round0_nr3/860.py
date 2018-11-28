
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

const string pt = "welcome to code jam"; 
const int max_n = 1111; 
const int MD = 10000; 

int res[max_n][22]; 
char buf[max_n]; 

bool newline(char z){ 
    return z == 10 || z == 13; 
} 


int main()
{
    int N; 

    scanf("%d", &N); 
    fgets(buf, max_n - 1, stdin); 

    FOR(T,1,N) {        
        fgets(buf, max_n - 1, stdin); 
        int ss = 0;  
        string s = ""; 
        while (isalpha(buf[ss]) || buf[ss] == ' ') { 
            s += buf[ss]; 
            ++ss; 
        }
        CLR(res, 0); 
        res[0][0] = 1; 
        REP(i,SIZE(s)) { 
            REP(j,SIZE(pt)) 
                if (s[i] == pt[j]) { 
                    res[i + 1][j + 1] = (res[i + 1][j + 1] + res[i][j]) % MD; 
                }        
            REP(j,SIZE(pt) + 1)  {
                res[i + 1][j] = (res[i + 1][j] + res[i][j]) % MD; 
            } 
        }     
        printf("Case #%d: %.4d\n",T,res[SIZE(s)][SIZE(pt)]); 
    } 

	return 0;
}

