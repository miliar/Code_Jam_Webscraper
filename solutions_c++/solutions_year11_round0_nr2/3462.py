const int Debug = 1;
/*
 * SOUR:
 * ALGO:
 * DATE:2011 5月07 22时59分42秒
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
 
set<int> opp[N];
map<pii, int> trans;
char elem[N];
int n;

void del(int beg, int end, int &top)
{
	int len = beg;
	for (int i = end;i < n;i++) {
		elem[len++] = elem[i];
	}
	top = len;
}

int main()
{
	char s[N];
	memset(s, 0,sizeof(s));
	int testcase, m;
	scanf("%d", &testcase);

	for (int T = 1;T <= testcase;T++) {
		trans.clear();
		for (int i = 0;i < N;i++) { opp[i].clear(); }

		scanf("%d", &m);
		while (m--) {
			scanf("%s", s);
			trans[pii(s[0], s[1])] = s[2];
			trans[pii(s[1], s[0])] = s[2];
		}

		scanf("%d", &m);
		while (m--) {
			scanf("%s", s);
			opp[s[0]].insert(s[1]);
			opp[s[1]].insert(s[0]);
		}

		scanf("%d %s", &n, s);
		int top = 0;
		for (int i = 0;i < n;) {
			if (top >= 1) {
				char t = trans[pii(s[i], elem[top - 1])];
				if (t != 0) {
					s[i] = t;
					top --;
					continue;
				}

				bool flag = 0;
				for (int j = 0;j < top;j++) {
					if (opp[s[i]].find(elem[j]) != opp[s[i]].end()) {
						i++;
						top = 0;
						flag = 1;
						break;
					}
				}
				if (flag) { continue; }
			}
			elem[top++] = s[i++];
		} 
		printf("Case #%d: [", T);
		for (int i = 0;i < top;i++) {
			if (i != 0) { printf(", "); }
			putchar(elem[i]);
		}
		printf("]\n");
	}
	return 0;
}
