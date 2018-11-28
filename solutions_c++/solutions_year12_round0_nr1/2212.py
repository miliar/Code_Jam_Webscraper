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
char code[] = {'y','h','e','s','o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
    'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
char buff[200];
void solve(int k) {
    printf("Case #%d: ", k);
    fgets(buff, 200, stdin);
    REP(i,strlen(buff))
        if(buff[i] >= 'a' && buff[i]<= 'z') 
            buff[i] = code[buff[i]-'a'];
    printf("%s", buff);
}

int main() {
	int _T;
	scanf("%d\n",&_T);
    FORU(i,1,_T) solve(i);
	return 0;
}

