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
ll gcd(ll a, ll b){
	if (b == 0)
		return a;
	return gcd(b, a % b);
}
int main(){
	int T;
	scanf("%d", &T);
	rep(qwe,T){
		printf("Case #%d: ",qwe + 1);
		ll Pd, Pg;
		ll n;
		scanf("%lld%lld%lld",&n, &Pd, &Pg);
		bool fail = 0;
		if (Pg == 0 && Pd != 0)
			fail = 1;
		if (Pg == 100 && Pd != 100)
			fail = 1;
		ll H = 100;
		ll k = gcd(Pd,  H);
		H /= k;
		if (H > n)
			fail = 1;
		/*
		bool ok = 0;
		forn(d, 1, n + 1)
			if (d * Pd % 100 == 0){
				ok = 1;
				break;
			}
		if (!ok)
			fail = 1;
		*/
		if (fail)
			printf("Broken\n");
		else
			printf("Possible\n");
	}
	return 0;
}