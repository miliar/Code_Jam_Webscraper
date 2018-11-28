#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <queue>
#include <assert.h>
#include <hash_map>
#define rep(x,n) for(int x=0;x<n;x++)
#define mem(a, b) memset(a, b, sizeof(a))
#define mp(x,y) make_pair(x,y)
#define getBit(code, i) (code & (1 << i))
#define setBit(code, i) (code | (1 << i))
#define resetBit(code, i) (code & ~(1 << i))
#define PI acos(-1.0)
using namespace std;
using namespace  stdext;

unsigned long double l, t, n, c, sol;
unsigned long double dists[1001];
unsigned long double times[1001];

unsigned long double best(int cur)
{
	unsigned long double tmpSol;
	if(times[cur] >= t)
		return dists[cur];
	else{
		unsigned long double dif = t - times[cur];
		unsigned long double d = dif / 2;
		unsigned long double tmp = sol - (dists[cur] * 2);
		tmp += (d * 2);
		tmp += (dists[cur] - d);
		tmpSol = min(sol, tmp);
	}
	return sol - tmpSol;
}

unsigned long double l1()
{
	unsigned long double tmpSol = sol;
	rep(i, n){
		tmpSol = min(tmpSol, min(sol, sol - best(n - i - 1)));
	}
	return tmpSol;
}

unsigned long double l2()
{
	unsigned long double tmpSol = sol;
	rep(i, n){
		rep(j, n) if(i != j){
			int cur1 = n - i - 1;
			int cur2 = n - j - 1;
			if(cur2 < cur1) swap(cur1, cur2);
			unsigned long double dif1 = best(cur1);
			times[cur2] -= dif1;
			unsigned long double dif2 = best(cur2);
			tmpSol = min(tmpSol, min(sol, sol - (dif1 + dif2)));
			times[cur2] += dif1;
		}
	}
	return tmpSol;
}

void gcjSolve()
{
	cin >> l >> t >> n >> c;
	rep(i, c) cin >> dists[i];
	for(int i = c; i < n; i++){
		dists[i] = dists[i - (int)c];
	}

	sol = 0;
	rep(i, n){
		times[i] = sol;
		sol += (dists[i] * 2);
	}
	if(l == 0)
		cout << (unsigned long long)sol << endl;
	else if(l == 1)
		cout << (unsigned long long)l1() << endl;
	else
		cout << (unsigned long long)l2() << endl;
}

int main(){

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	int k;
	cin >> k;
	rep(kase, k){
		printf("Case #%d: ", kase + 1);
		gcjSolve();
	}
	return 0;
}