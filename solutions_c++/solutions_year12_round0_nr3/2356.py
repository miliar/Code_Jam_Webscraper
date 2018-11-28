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
//const int MX = 1000*1000+7;
int len(int k) {
    int cnt = 0;
    while(k>0) k/=10, cnt++;
    return cnt;
}
int pow(int p) {
    int r = 1, k = 0;
    while(k<p)
        r*=10, k++;
    return r;
}
int turn(int k,int l) {
//    printf("turn %d = ", k);
    int last = k%10;
    k /= 10;
    k += last*pow(l);
//    printf("%d\n", k);
    return k;
}
void solve(int x) {
    int A,B;
    scanf("%d %d",&A,&B);
    vector<pair<int,int> > v;
    FORU(i,A,B) {
        int t = i;
        REP(j,len(i)-1) {
            if(t%10 != 0) {
                t = turn(t, len(i)-1);
                if(t < i && t>=A) 
                    v.PB(MP(t,i));
            } else {
                t = turn(t, len(i)-1);
            }
        }
    }
    sort(ALL(v));
    v.erase(unique(ALL(v)), v.end());
    printf("Case #%d: %d\n", x, SIZE(v));
}

int main() {
	int _T;
	scanf("%d",&_T);
	FORU(i,1,_T) solve(i);
	return 0;
}

