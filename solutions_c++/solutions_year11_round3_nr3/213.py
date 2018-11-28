// Author: Swarnaprakash
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 105;
const int INF = 0x3f3f3f3f;
const bool debug=true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

void solve() {
	int n,l,h;
	scanf("%d %d %d", &n, &l, &h);
	int a[n];
	for(int i =0;i<n;++i)
		scanf("%d",&a[i]);
	for(int i=l;i<=h;++i) {
		bool ok= true;
		for(int j=0;j<n && ok;++j) if(a[j]%i!=0 && i%a[j]!=0) ok=false;
		if(ok) {
			printf("%d\n",i);
			return;
		}
	}
	puts("NO");
}

int main() {
	int tc;
	scanf("%d",&tc);
	for(int t=1;t<=tc;++t) {
		printf("Case #%d: ",t);
		solve();
	}
	return 0;
}

