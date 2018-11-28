#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<deque>
#include<map>
#include<functional>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOREACH(i,x) for(typeof(x)::iterator it=(x).begin(); it!=(x).end(); ++it)
#define EACH(i,x) REP(i,(x).size())
#define sz	size()
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define pb	push_back
#define mp	make_pair
#define eps	1e-15
#define inf 0x3FFFFFFF

typedef long long int lint;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;


bool find(int a, int b)
{
	bool ret = false;
	while( a != b ) {
		ret = !ret;
		if(a<b) swap(a,b);
		int c = a % b;
		int d = a / b;
		if( d > 1 ) return ret;
		a = b;
		b = c;
	}

	return ret;
}

void solve()
{
	int a1, a2, b1, b2;
	scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
	int result = 0;
	
	for(int i=a1; i<=a2; i++) for(int j=b1; j<=b2; j++) {
		if (find(i, j)) result++;
	}


	printf("%d\n",result);
}


int main(void)
{
	int test;
	scanf("%d",&test);
	REP(i,test) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}

