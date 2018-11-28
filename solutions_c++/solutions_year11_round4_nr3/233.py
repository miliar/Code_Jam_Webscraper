#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <cstring>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

long long N;
bool criba[1001001];
vector<ll> primos;

int loga(ll a, ll b) {
	int res = 0;
	while (a >= b) {
		a /= b;
		res++;
	}
	return res;
}

int main() {
	int casos;
	CLEAR(criba, true);
	criba[0] = criba[1] = false;
	for (int i = 2; i <= 1000000; i++) if (criba[i]) {
		primos.pb(i);
		for (int j = 2*i; j <= 1000000; j += i) criba[j] = false;
	}
	cin >> casos;
	REP(caso, casos) {
		ll delta = 1;
		cin >> N;
		REP(i, SZ(primos)) {
			if (primos[i]*primos[i] > N) break;
			delta += max(0,loga(N,primos[i])-1);
		}
		if (N == 1) delta = 0;
		cout << "Case #" << caso+1 << ": " << delta << endl;
	}
	return 0;
}
