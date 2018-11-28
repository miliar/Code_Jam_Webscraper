#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define clr(a) memset(a, 0, sizeof(a))
#define fil(a, b) memset(a, b, sizeof(a));
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define se(x) cout<<#x<<" = "<<x<<endl

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair <int, int> pii;

const double eps = 1e-8;
ll n;
int pd, pg;

int dcmp(double x) {
	if (x < -eps) return -1;
	else return x > eps;
}

ll gcd(ll a, ll b) {
	return b ? gcd(b, a % b) : a;
}

void solve(int cas) {
	printf("Case #%d: ", cas);
	scanf("%lld%d%d", &n, &pd, &pg);
	int chk = gcd(pd, 100);
	int z = 100 / chk;
	if (n < z) {
		for (int i = 2; i <= n && z != 1; ++i) {
			if (i % z == 0) {
				z = 1;
				break;
			}
		}
		if (z != 1) {
			puts("Broken");
			return;
		}
	}
	if (pd == pg) {
		puts("Possible");
		return;
	}
	if (pg == 100) {
		if (pd != 100){
			puts("Broken");
			return;
		}
	}
	if (pg == 0) {
		if (pd == 0) puts("Possible");
		else puts("Broken");
		return;
	}
	double a = -pg * 1.0 / (pg - pd);
	double b = (100.0 - pg) / (pg - pd);
//	printf("%lf,%lf\n", a, b);
	if (pg - pd < 0) {
		swap(a, b);
	}
	if (dcmp(a - b) >= 0) {
		puts("Broken");
		return;
	}
	if (dcmp(a) <= 0 && dcmp(b) >= 0) {
		puts("Possible");
		return;
	}
	if (dcmp(a - 1) <= 0 && dcmp(1 - b) <= 0) {
		puts("Possible");
		return;
	}
	if (dcmp(a) >= 0 && dcmp(a - 1) <= 0) {
		puts("Possible");
		return;
	}
	if (dcmp(b) >= 0 && dcmp(b - 1) <= 0) {
		puts("Possible");
		return;
	}
	puts("Broken");

}

int main() {
//	freopen("in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int cas;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; ++i) {
		solve(i);
	}
	return 0;
}
