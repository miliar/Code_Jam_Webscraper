/* Michał Adamczyk, saddam */
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#include<set>
#include<map>
#include<utility>
#include<ext/numeric>
#include<tr1/unordered_map>

using namespace std;
using namespace std::tr1;
using namespace __gnu_cxx;

#define REP(i,n) for(int i=0;i<(n);++i)
#define PER(i,n) for(int i=(n)-1;i>=0;--i)
#define FORU(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define ALL(X) (X).begin(),(X).end()
#define SIZE(X) (int)(X).size()
#define VAR(V,init) __typeof(init) V=(init)
#define FOREACH(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

typedef unsigned long long ULL;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

LL nwd(LL a,LL b) { return !b?a:nwd(b,a%b); }
inline int CEIL(int a,int b) { return a%b ? a/b+1 : a/b; }

const int INF = 1000000007;
void solve(int k) {

    int n,s,p,t;
    LL cnt=0;
    scanf("%d%d%d",&n,&s,&p);
    REP(i,n) {
        scanf("%d",&t);
        if((t%3) == 0) {
            if(t/3 >= p) cnt++;
            else if(s>0 && t/3-1>=0 && t/3+1 >= p) cnt++, s--;                
        } else if((t%3) == 1) {
            if(t/3+1 >= p) cnt++;
        } else {
            if(t/3+1 >= p) cnt++;
            else if(s>0 && t/3+2 >= p) cnt++, s--;
        }
//        printf("%lld ", cnt);
    }
//  printf("\n");

    printf("Case #%d: %lld\n", k, cnt);
}

int main() {
	int _T;
	scanf("%d\n",&_T);
    FORU(i,1,_T) solve(i);
	return 0;
}

