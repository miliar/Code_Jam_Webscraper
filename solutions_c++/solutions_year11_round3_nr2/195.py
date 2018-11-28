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

int dis[1000000];
int lef[1000000];
int dif[1000000];

void runCase()
{
    LL L,t,N,C,a[1000];

    setbuf(a,0);setbuf(dis,0);setbuf(lef,0);setbuf(dif,0);

    scanf("%I64d%I64d%I64d%I64d",&L,&t,&N,&C);
    // debug(L); debug(t); debug(N); debug(C);cerr<<endl;
    REP(i,C) scanf("%I64d",&a[i]);

    LL pos = 0;
    LL spend = 0;
    LL res = 0;
    REP(i,N) {
        dis[i] = a[i%C];
        lef[i] = dis[i]*2;

        res += lef[i];
    }

    REP(i,N) {
        spend += lef[i];
        if(spend > t) {
            pos = i;
            dif[i] = (spend-t)/2;
            break;
        }
    }

    FOR(i,pos+1,N-1) {
        dif[i] = dis[i];
    }
    vi div(N);
    REP(i,N) div[i] = dif[i];
    sort(div.begin(),div.end());

    FOR(i,N-L,N-1) res -= div[i];

    printf("%I64d\n",res);
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
