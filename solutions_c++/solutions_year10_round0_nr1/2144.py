#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cmath>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long Int;

#define FOR(i, a, b) for(int i=a; i<b; ++i)
#define RFOR(i, a, b) for(int i=b-1; i>=a; --i)
#define FILL(a, val) memset(a, val, sizeof(a))

#define all(c) c.begin(), c.end()
#define sz(c) (int)c.size()
#define pb push_back

#define mp make_pair
#define X first
#define Y second

const double PI = acos(-1.0);
const int INF = 1000000000;


int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	FOR(t, 0, T)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		if ((k & ((1<<n) -1)) == (1<<n) -1 )
			printf("Case #%d: ON", t+1);
		else
			printf("Case #%d: OFF", t+1);
		if (t != T-1)
			printf("\n");
	}
	return 0;
}

/*

4
1 0
1 1
4 0
4 47

*/