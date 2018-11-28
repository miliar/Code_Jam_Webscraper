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

int c, d, n;
char str[110];
char com[128][128];
bool opp[128][128];
char stk[110];

void solve(int cas) {
	printf("Case #%d: ", cas);
	memset(com, 0, sizeof(com));
	memset(opp, 0, sizeof(opp));
	scanf("%d", &c);
	for (int i = 0; i < c; ++i) {
		scanf("%s", str);
		com[str[0]][str[1]] = 
			com[str[1]][str[0]] = str[2];
	}
	scanf("%d", &d);
	for (int i = 0; i < d; ++i) {
		scanf("%s", str);
		opp[str[0]][str[1]] = 
			opp[str[1]][str[0]] = 1;
	}
	scanf("%d%s", &n, str);
	int top = 0;
	for (int i = 0; i < n; ++i) {
		if (top == 0) {
			stk[top++] = str[i];
		} else {
			if (com[stk[top - 1]][str[i]]) {
				stk[top - 1] = com[stk[top - 1]][str[i]];
			} else {
				stk[top++] = str[i];
			}
		}
		for (int j = 0; j < top - 1; ++j) {
			if (opp[stk[top - 1]][stk[j]]) {
				top = 0;
				break;
			}
		}
	}
	printf("[");
	if (top) printf("%c", stk[0]);
	for (int i = 1; i < top; ++i) {
		printf(", %c", stk[i]);
	}
	puts("]");
}

int main() {
//	freopen("D:\\in.txt","r",stdin);
//	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	int cas;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; ++i) {
		solve(i);
	}
	return 0;
}
