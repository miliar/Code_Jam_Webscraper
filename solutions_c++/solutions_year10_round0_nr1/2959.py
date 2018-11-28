using namespace std;

#include <set>
#include <map>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <utility>
#include <iomanip>
#include <fstream>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>

#define oo 1<<30
#define f first
#define s second
#define II inline
#define db double
#define ll long long
#define pb push_back
#define mp make_pair
#define Size(V) ((int)(V.size()))
#define all(v) v.begin() , v.end()
#define CC(v) memset((v),0,sizeof((v)))
#define CP(v,w) memcpy((v),(w),sizeof((w)))
#define FOR(i,a,b) for(int (i)=(a);(i)<=(b);++(i))
#define REP(i, N) for (int (i)=0;(i)<(int)(N);++(i))
#define FORit(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

#define IN  "code.in"
#define OUT "code.out"

int T;
ll N,K;

II void scan()
{
    freopen(IN,"r",stdin);
    freopen(OUT,"w",stdout);

}

II void solve(int Test)
{
    scanf("%lld%lld",&N,&K);
    if( !((K + 1) % (1LL<<N) ) )
        printf("Case #%d: ON\n",Test);
    else
        printf("Case #%d: OFF\n",Test);
}

int main()
{
	scan();
	scanf("%d",&T);
	FOR(i,1,T)
        solve(i);

	return 0;
}
