#include <string>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <stack>
#include <queue>
#include <algorithm>
#include <deque>
#include <utility>
#include <sstream>
#include <vector>
#include <map>
#include <ctime>
#include <set>
using namespace std;
#define sz size()
#define vi vector<int>
#define vs vector<string>
#define dsz size()-1
#define pb push_back
#define maxn(a,b) (a) = ((a) < (b) ? (b) : (a))
#define FUP(ii,ss,ff) for ((ii) = (ss);(ii) <= (ff);(ii)++)
#define FDOWN(ii,ss,ff) for ((ii) = (ss);(ii) >= (ff);(ii)--)
#define FALL(ii, vv) for ((ii) = 0;signed (ii) <= signed ((vv).dsz);(ii)++)
#define ITERATE(__it,__container) for(__it=__container.begin(); __it!=__container.end(); __it++)
#define EPS 1e-12
#define INF 2147483647
#define sgn(x) ((x)>0 ? 1 : (x)==0 ? 0 : -1)
#define sq(x) ((x)*(x))
#define sorta(a) sort(a.begin(), a.end())
#define cleara(a, b) memset(a, b, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define absd(a) ((a)<0?-(a):(a))
#define absm absd
#define mp make_pair
typedef unsigned int uint;
typedef long long ll;

#define MOD 100003
int R(int a) {
	return a%MOD;
}

int dpt[1000][1000];
int bnt[1000][1000];

long long bn(int n, int k) {
	if (n == k || k == 0) return 1;
	int& res = bnt[n][k];
	if (res) {
		return res-1;
	}
	res = R(bn(n-1,k) + bn(n-1, k-1));
	return res++;
}

int dp(int i, int n) {
	if (n == 1) return 1;
	int& res = dpt[i][n];
	if (res) {
		return res-1;
	}
	int w;
	FUP(w, 0, min(i-1, n-i-1)) {
		res = R(res + dp(i-w-1, i) * bn(n-i-1, w));
	}
	return res++;
}

int main() {
	int t, i, n;
	scanf("%d", &t);
	FUP(i,1,t) {
		scanf("%d", &n);
		int res = 0,c;
		FUP(c, 1, n-1) {
			res = R(res+dp(c,n));
		}
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}