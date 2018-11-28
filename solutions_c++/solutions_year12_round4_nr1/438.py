#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;
const int inf = int(1e9)+7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

const int MAXN = 100000+5;
int d[MAXN], a[MAXN], f[MAXN];
int n;
int main() {
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	
	int caseNum;
	scanf("%d", &caseNum);
	
	
	REP(ccc, 1, caseNum+1) {	
		scanf("%d", &n);		
		for (int i = 1; i <= n; ++i) {
			scanf("%d%d", d+i, a+i);
		}
		scanf("%d", d+n+1);
		++n;
		
		REP(i,1,n+1) f[i] = -1;
		f[1] = d[1];
		REP(i,1,n) {
			int mm = f[i];
			REP(j,i+1,n+1) {
				if (d[j]-d[i] <= mm && min(d[j]-d[i], a[j]) > f[j]) 
					f[j] = min(d[j]-d[i], a[j]);
			}
		}
		printf("Case #%d: ", ccc);
		if (f[n] != -1) printf("YES\n");
		else printf("NO\n");
	}
//	while (1>0) {}
	return 0;
} 
