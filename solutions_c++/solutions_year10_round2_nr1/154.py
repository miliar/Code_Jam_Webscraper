
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

VS split(string s, char z) { 
    string tmp = ""; 
    VS ret; 
    s += z; 
    REP(i,SIZE(s)) if (s[i] != z) { 
        tmp += s[i]; 
    } 
    else {
        if (SIZE(tmp)) ret.PB(tmp); 
        tmp = ""; 
    } 
    return ret; 
} 

char buf[101010]; 

VS get() { 
    scanf("%s",buf); 
    return split(buf, '/'); 
} 

class node { 
    public: 
        map<string,int> M;         
} t[100100]; 

int cc; 
VS v; 

int add(int pos, int w) { 
    if (pos == SIZE(v)) return 0; 
    if (t[w].M.count(v[pos])) return add(pos+1,t[w].M[v[pos]]); 
    t[w].M[v[pos]] = ++cc; 
    return add(pos + 1, cc) + 1;    
} 

void wypisz(VS vs) { 
    FORE(e,vs) printf("%s ",e->c_str()); 
    puts("");  
} 


int main()
{
    int N,T,M; 
    scanf("%d",&T); 
    FOR(tc,1,T) { 
        vector<VS> vv; 
        scanf("%d%d",&N,&M); 
        cc = 0; 
        t[0].M.clear();
        REP(i,N) { 
            v = get();
//            wypisz(v);  
            add(0,0); 
        } 
        int ret = 0; 
        REP(i,M) { 
            v = get(); 
  //          wypisz(v); 
            ret += add(0, 0); 
        } 
        FOR(i,0,cc+1) t[i].M.clear();  
     
        printf("Case #%d: %d\n",tc,ret);
    } 


	return 0;
}

