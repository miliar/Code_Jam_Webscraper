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

const int inf = 0x7fffffff;

void solve(int cas) {
	printf("Case #%d: ", cas);
	int n, tmp;
	int chk = 0;
	int sum = 0;
	int minv = inf;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &tmp);
		chk ^= tmp;
		sum += tmp;
		minv = min(minv, tmp);
	}
	if (chk) {
		puts("NO");
	} else {
		printf("%d\n", sum - minv);
	}
}

int main() {
//	freopen("D:\\in.txt","r",stdin);
//	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
//	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int cas;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; ++i) {
		solve(i);
	}
	return 0;
}
