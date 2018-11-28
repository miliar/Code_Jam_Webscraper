#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long LL;

const int AND=0;
const int OR=1;
const int INF=1<<29;
const int MAX=100000;
int type[MAX];
int cc[MAX];
bool isleaf[MAX];
int leaf[MAX];
int dp[MAX][2];
int M,V;

int go(int,int);

int orgate(int at, int v)  {
	int minv = INF;
	if (v) {
		minv = min(minv, go(2*at,0) + go(2*at+1,1));
		minv = min(minv, go(2*at,1) + go(2*at+1,0));
		minv = min(minv, go(2*at,1) + go(2*at+1,1));
	}
	else {
		minv = min(minv, go(2*at,0) + go(2*at+1,0));
	}
	return minv;
}
int andgate(int at, int v) {
	int minv = INF;
	if (v) {
		minv = min(minv, go(2*at,1) + go(2*at+1,1));
	}
	else {
		minv = min(minv, go(2*at,0) + go(2*at+1,1));
		minv = min(minv, go(2*at,1) + go(2*at+1,0));
		minv = min(minv, go(2*at,0) + go(2*at+1,0));
	}
	return minv;
}

int go(int at, int v) {
	if (isleaf[at]) {
		if (v!=leaf[at]) return INF;
		return 0;
	}
	int& ref = dp[at][v];
	if (ref!=-1) return ref;
	ref = INF;
	if (type[at]==AND) {
		ref = min(ref, andgate(at,v));
		if (cc[at]) ref = min(ref, 1 + orgate(at,v));
	}
	else {
		ref = min(ref,orgate(at,v));
		if (cc[at]) ref = min(ref, 1 + andgate(at,v));
	}
	return ref;
}

int main() {
	int NCASES;
	cin >> NCASES;
	for (int z=1;z<=NCASES;++z) {
		memset(dp,-1,sizeof dp);
		cin >> M >> V;
		for (int i=1;i<=M;++i) {
			if (i<=(M-1)/2) {
				isleaf[i]=0;
				int G,C;
				cin >> G >> C;
				cc[i] = C;
				if (G) type[i]=AND;
				else type[i]=OR;
			}
			else {
				isleaf[i]=1;
				int ll;
				cin >> ll;
				leaf[i]=ll;
			}
		}
		int res= go(1,V);
		printf("Case #%d: ", z);
		if (res>=INF) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
}
