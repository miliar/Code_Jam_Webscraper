#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <list>

using namespace std;

void solve();
void runCase();

typedef long long LL;
#define FOR(i,a,b) for(LL i = (a); i <= (b); i++)
#define REP(i,n) for(LL i = 0; i < (n); i++)

#define debug( x ) cerr << "" << x << " "
#define dbg( c ) cerr << " " << c << " ";

#define setbuf(buf,num) memset(buf,num,sizeof(buf))
#define vi vector< LL >
#define vvi vector< vi >
#define PB push_back
#define SZ(x) ((int)x.size())

void runCase()
{
    LL N,L,H;
    scanf("%I64d %I64d %I64d", &N, &L, &H);
    //debug(N);debug(L); debug(H); cerr<<endl;
    vi a(N,0);
    LL x;
    REP(i,N) scanf("%I64d",&a[i]);
    //REP(i,N) debug(a[i]); cerr << endl;

    LL res = 0;
    bool can = false;
    FOR(i,L,H) {
        bool ok = true;
        REP(j,N) {
            if(a[j]%i!=0 && i%a[j]!=0) {
                ok = false;
            }
        }
        if(ok) {
            res = i;
            can = true;
            break;
        }
    }

    if(can) printf("%I64d\n",res);
    else printf("NO\n");
}

void solve()
{
	int n;
	scanf("%d",&n);
	getchar();

	for(int i = 0; i < n; i++) {
		printf("Case #%d: ",i+1);
		runCase();
	}
}

int main()
{
	solve();
	return 0;
}
