#define TSK "c"

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

#define ll long long
#define db double
#define rep(i,n) for(int (i) = 0;  (i) < (n); ++ (i))
#define forn(i,a,n) for(int (i) = (a);  (i) < (n); ++ (i))
#define tr(i,a) for(__typeof((a).begin()) i = (a).begin(); i != (a).end(); ++ i)
#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define PI pair<int,int>
#define fi first
#define se second
#define VPI vector<PI >
#define VVPI vector<VPI >
#define VI vector<int>
#define VII vector<VI >
#define VB vector<bool> 
#define VD vector<db>
#define VS vector<string>
#define INF 1000000000
#define deb(x) cerr <<"[line: " << __LINE__ << "] " #x " = " << x << endl
#define MAXN 1100
int a[MAXN];
int main(){
	int T;
	scanf("%d", &T);
	rep(qwe,T){
		printf("Case #%d: ",qwe + 1);
		int n;
		scanf("%d",&n);
		rep(i,n)
			scanf("%d",&a[i]);
		sort(a, a + n);
		int t = 0;
		rep(i, n)
			t ^= a[i];
		if (t){
			printf("NO\n");
			continue;
		}
		ll sum = 0;
		forn(i, 1, n)
			sum += (ll)a[i];
		printf("%lld\n", sum);
	}
	return 0;
}