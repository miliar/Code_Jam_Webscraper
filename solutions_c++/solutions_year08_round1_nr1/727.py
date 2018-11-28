#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
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
using namespace std;
template<class T> inline const T& Max(const T& a, const T& b){return a > b ? a : b;}
template<class T> inline const T& Min(const T& a, const T& b){return a < b ? a : b;}
template<class T> inline T sqr(const T a) {return a * a;}
const double PI = acos(-1);
const int MAXINT = 0x7fffffff;
const double INF = 1e100;
const double EPS = 1e-10;

int X[1000];
int Y[1000];
int n;
int ans;
	FILE *fp = fopen("pro1.txt", "w");
	FILE *ff = fopen("data1.in", "r");
void input()
{
	scanf("%d", &n);
	int i;
	for (i=0; i<n; ++i) {
		scanf("%d", X + i);
	}
	for (i=0; i<n; ++i) {
		scanf("%d", Y + i);
	}
}

void doit()
{
	sort(X, X + n);
	sort(Y, Y + n);
	reverse(Y, Y + n);
	ans = 0;
	for (int i=0; i<n; ++i) {
		ans += X[i] * Y[i];
	}
}


int main()
{

	int testcase;
	scanf( "%d", &testcase);
	int cc;
	for (cc=1; cc<=testcase; ++cc) {
		input();
		doit();
		printf("Case #%d: %d\n", cc, ans);
		fprintf(fp, "Case #%d: %d\n", cc, ans);
	}
	return 0;
}
