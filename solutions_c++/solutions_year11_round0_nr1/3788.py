const int Debug = 1;
/*
 * SOUR:
 * ALGO:
 * DATE:2011 5月07 20时05分46秒
 * COMM:
 * */
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cassert>
#include<cmath>
#include<queue>
#include<vector>
#include<map>
#include<stack>
#include<set>
using namespace std;
#define pb(x) push_back(x)
#define fi first
#define se second
#define rab(i,a,b) for(int i(a), _n(b); i <= (_n); i++)
#define rep(i,n) rab(i,0,(n)-1)
 
typedef std::vector < int >vi;
typedef std::pair < int, int > pii;
typedef long long LL;
 
template <class T> void ckmin(T &a,T b) { if (a > b) { a = b; } }
template <class T> void ckmax(T &a,T b) { if (a < b) { a = b; } }
template <class T> void pr(T &a) { cout << a << ' '; }
template <class T> void print(T &a) { a.__str__(); }
template <class T> int size(const vector<T> &v) { return (int)v.size(); }
#define fpr(...) \
	fprintf(stderr, "%s(%d)-%s: ",__FILE__,__LINE__,__FUNCTION__); \
fprintf(stderr, __VA_ARGS__);
int countbit(int n) { return n == 0 ? 0 : 1 + countbit(n & (n - 1)); }
 
const int maxint = 0x7fffffff;
const long long max64 = 0x7fffffffffffffffll;
/*Every problem has a simple, fast and wrong solution.*/
/*std::ios::sync_with_stdio(false);*/
 
const int N = 128;
int seq[N][2], n, x[2];

int sgn(int x)
{
	if (x > 0) { return  1;}
	if (x < 0) { return -1;}
	return 0;
}

int next(int idx, int c)
{
	for (int i = idx;i <= n;i++) {
		if (seq[i][0] == c) {
			return sgn(seq[i][1] - x[c]);
		}
	}
	return 0;
}

int main()
{
	int testcase, t;
	char c[8];

	scanf("%d", &testcase);

	for (int T = 1;T <= testcase;T++) {
		scanf("%d", &n);

		for (int i = 1;i <= n;i++) {
			scanf("%s %d", c, &t);
			seq[i][0] = (c[0] == 'O');
			seq[i][1] = t;
		} 

		int ans = 0;
		x[0] = 1, x[1] = 1;
		for (int top = 1;top <= n;ans++) {
			int stat = 0;
			if (seq[top][0] == 0) {
				if (x[0] == seq[top][1]) {
					top++;
					stat = 1;
				}
			}else {
				if (x[1] == seq[top][1]) {
					top++;
					stat = 2;
				}
			}
			if (stat != 1) x[0] += next(top, 0);
			if (stat != 2) x[1] += next(top, 1);
		}
		printf("Case #%d: %d\n", T, ans);
	} 
    return 0;
}

