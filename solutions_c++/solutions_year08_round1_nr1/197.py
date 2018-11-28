#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<string>
#include<map>
#include<algorithm>
#include<functional>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define EACH(i,x) REP(i,(x).size())
#define sz	size()
#define all(x) (x).begin(), (x).end()
#define mp make_pair
#define pb push_back
#define eps	1e-15

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long int lint;

lint solve()
{
	int n;
	vector<lint> x;
	vector<lint> y;

	scanf("%d", &n);
	REP(i, n) {
		int t;
		scanf("%d",&t);
		x.pb(t);
	}
	REP(i, n) {
		int t;
		scanf("%d",&t);
		y.pb(t);
	}
	sort(all(x), greater<lint>());
	sort(all(y));

	lint ret = 0;
	REP(i,n) ret += x[i] * y[i];

	return ret;

}


int main(void)
{
	int test;
	int cnt = 0;
 	scanf("%d", &test);

	REP(i, test)
		printf("Case #%d: %I64d\n", ++cnt, solve());

	return 0;
}

