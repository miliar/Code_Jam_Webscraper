#include <iostream>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <sstream>
#include <bitset>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
typedef unsigned long long UL;
typedef long double LD;
typedef pair<int,int> PII;

const int INF = 1000*1000*1000+1;
#define FOR(x,b,e) for (int x = (b); x < (e); ++x)
#define FORD(x,b,e) for (int x = (b); x >= (e); --x)
#define REP(x,n) for (int x = 0; x < (n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i,c) for (VAR(i,(c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

void scase() {
	int n, k;
	scanf("%d%d",&n,&k);
	k %= (1<<n);
	if (k == (1<<n)-1) printf("ON\n");
	else printf("OFF\n");
}

int main() {
	int z;
	scanf("%d",&z);
	REP(i,z) {
		printf("Case #%d: ",i+1);
		scase();
	}

	return 0;
}
