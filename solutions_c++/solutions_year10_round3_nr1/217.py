#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <cstring>
#include <ctime>
using namespace std;
#define pb push_back
#define INF 1000000000
#define L(s) (int)((s).end()-(s).begin())
#define FOR(i,a,b) for (int _n(b), i(a); i <= _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define C(a) memset((a),0,sizeof(a))
#define llint long long
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define VI vector<int>
#define ppb pop_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
#define x first
#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pi 3.1415926535897932384626433832795028841971
#define tt (ll+rr)/2
#define rnd() ((rand() << 16) ^ rand())

int main()
{
	freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);
	
	int tc, TC;
	cin >> TC;
	rep(tc, TC)
	{
		int ans = 0;
		int n;
		scanf("%d",&n);
		VI a(n), b(n);
		rept(i, n) scanf("%d%d",&a[i], &b[i]);
		rept(i, n)
			rept(j, n)
			{	
				if (a[i] < a[j] && b[i] > b[j]) ans++;
				if (a[i] > a[j] && b[i] < b[j]) ans++;	
			}
		ans /= 2;
		printf("Case #%d: ",tc);
		printf("%d\n", ans);
	}
	
	return 0;
}






