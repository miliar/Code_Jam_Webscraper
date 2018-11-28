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
#define MAXN 1100
int a[MAXN];
int b[MAXN];
#define EPS 10E-5
int cmp(db a,db b){
	db tmp = a - b;
	if (fabs(tmp) < EPS)
		return 0;
	else if (tmp > 0)
		return 1;
	else return -1;
}
int main(){
	freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);
	int C;
	cin >> C;

	rep(qwer,C){
		int n;
		cin >> n;
		rep(i,n)
			cin >> a[i] >> b[i];
		int ans = 0;
		rep(i,n)
			rep(j,n)
				if (a[i] > a[j] && b[i] < b[j] || a[i] < a[j] && b[i] > b[j])
					++ans;
		ans /= 2;
		printf("Case #%d: %d\n",qwer+1,ans);
	}
	return 0;
}