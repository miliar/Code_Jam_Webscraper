#include <algorithm>
#include <iostream>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define sz(a) int((a).size())
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define UN(v) sort(all(v)),(v).erase(unique((v).begin(),(v).end()),(v).end())
#define CL(a,b) memset(a,b,sizeof a)
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

int main()
{
#ifdef LocalHost
freopen("a-large.in", "r", stdin);//-small-attempt
freopen("a-large.out", "w", stdout);//-large
#endif
	int T;
	scanf("%d", &T);
REP(it, T)
{
	int n,k;
	scanf("%d%d", &n, &k);
	printf("Case #%d: ", it+1);
	if((k+1) % (1<<n) == 0) printf("ON\n");
	else printf("OFF\n");
}
	return 0;
}
