#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <fstream>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <limits>
#include <queue>
#include <deque>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

#define SIZE(X) ((int)X.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)

typedef long long LL;
typedef pair<int,int> PII;

template<class T> void out(T A[],int n) {cout<<"{"; for (int i=0;i<n;i++){ cout<<A[i];if (i==n-1) cout<<"}"; else cout<<",";} cout<<endl;}
template<class T> void out(T A[],int n, int m) {for(int i=0;i<n;++i) out(A[i],m); cout<<endl;}\
template<class T> void out(vector<T> A,int n=-1) {if (n<0 || n>SIZE(A)) n=SIZE(A);cout<<"{";for (int i=0;i<n;i++) {cout<<A[i];if (i==n-1) cout<<"}"; else cout<<",";} cout<<endl;}

const int MAXN = 110;
const int INF = 1000000000;
const double EPS = 1e-8;
const double PI = acos(-1.0);

int T, a1, a2, b1, b2;

map< pair< pair<int,int>, bool >, bool > mp;

bool go(int a, int b, bool turn) { // true: a
	pair< pair<int,int>, bool > p = MP(MP(a, b), turn);
	if (mp.count(p) != 0) return mp[p];
	bool &ret = mp[p];
	if (a <= 0 || b <= 0) return ret = turn;
	if (a > b) {
		if (a % b == 0) return ret = turn;
		if (go(a % b, b, !turn) == turn) return ret = turn;
		if (a > 2 * b) {
			if (go(a % b + b, b, !turn) == turn) return ret = turn;
		}
// 		for (int k = 1; ; ++k) {
// 			int na = a - k * b;
// 			if (na <= 0) break;
// 			int nb = b;
// 			if (go(na, nb, !turn) == turn) return ret = turn;
// 			if (na <= 0) break;
// 		}
		return ret = !turn;
	} else if (b > a) {
		if (b % a == 0) return ret = turn;
		if (go(a, b % a, !turn) == turn) return ret = turn;
		if (b > 2 * a) {
			if (go(a, b % a + a, !turn) == turn) return ret = turn;
		}
// 		for (int k = 1; ; ++k) {
// 			int na = a;
// 			int nb = b - k * a;;
// 			if (nb <= 0) break;
// 			if (go(na, nb, !turn) == turn) return ret = turn;
// 		}
		return ret = !turn;
	} else return ret = !turn;
}
int gcd(int a, int b) {
	return b ? gcd(b, a % b) : a;
}
int main ()
{
	freopen("C-small.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		mp.clear();
		scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
		int ans = 0;
		for (int a = a1; a <= a2; ++a) {
			for (int b = b1; b <= b2; ++b) {
				if (go(a, b, true)) {
					//int g = gcd(a, b);
					//printf("%d %d\n", a, b);
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}