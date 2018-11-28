#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

const int N = 1010;
int n;

main(){
	int t,a;
	scanf("%d",&t);
	FOR(q,1,t){
		scanf("%d",&n);
		int sum  =0;
		int sxor =0;
		int najmn = 1000000;
		REP(i,n){
			scanf("%d",&a);
			sum += a;
			sxor ^= a;
			najmn = min(a,najmn);
		}
		printf("Case #%d: ",q);
		if(sxor == 0)
			printf("%d\n",sum  - najmn);
		else printf("NO\n");
	}
	return 0;
}
