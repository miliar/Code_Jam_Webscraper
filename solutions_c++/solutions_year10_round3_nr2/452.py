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


using namespace std;

#define INF 999999
#define pb push_back
#define sz(x) ((int)((x).size()))
#define all(x) (x).begin(),(x).end()
#define db double
#define ll long long
#define rep(i,n) for (int (i)=0; (i)<(n); ++(i))
#define forn(i,a,n) for (int (i)=(a); (i)<(n); ++(i))
#define VI vector<int>
#define VB vector<bool>

#define EPS 10E-5
int cmp(db a,db b){
	db tmp = a - b;
	if (fabs(tmp) < EPS)
		return 0;
	else if (tmp > 0)
		return 1;
	else return -1;
}
int ans;
int c;
#define MAXN 1100
int mem[MAXN][MAXN];
int per(int l, int r){
	if (l*c >= r)
		return 0;
	if (mem[l][r] != 0)
		return mem[l][r];
	int pans = INF;
	for (int i = l+1; i < r-1; ++ i){
		pans = min(pans,max(per(l,i),per(i,r)));
	}
	return mem[l][r] = pans + 1;
}
void reset(){
	rep(i,MAXN)
		rep(j,MAXN)
			mem[i][j] = 0;
}
int main(){
	freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);
	int C;
	cin >> C;

	rep(qwer,C){
		int l,p;
		cin >> l >> p >> c;
		reset();
		ans = per(l,p);
		printf("Case #%d: %d\n",qwer+1,ans);
	}
	return 0;
}