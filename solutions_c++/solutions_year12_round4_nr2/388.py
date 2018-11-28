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
int ans_x[MAXN], ans_y[MAXN];
int rs[MAXN];
struct node{
	int r, rank;
};
node pa[MAXN];
bool cmp(const node &a1, const node &a2) {
	return a1.r < a2.r;
}

int n,w,l;
int main() {
//	freopen("B.in","r",stdin);
//	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
//	freopen("B-small-attempt3.in","r",stdin);freopen("B-small-attempt3.out","w",stdout);
//	freopen("B-small-attempt4.in","r",stdin);freopen("B-small-attempt4.out","w",stdout);

	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);

	
	int caseNum;
	scanf("%d", &caseNum);
	
	
	REP(ccc, 1, caseNum+1) {	
		
		scanf("%d%d%d", &n, &w, &l);
		int flag = 0;
		if (w > l) { swap(w, l); flag = 1; }
		FOR(i,n) {
			scanf("%d", rs+i);
			pa[i].r = rs[i];
			pa[i].rank = i;
		}
		sort(rs, rs+n);
		sort(pa, pa+n, cmp);
		
		printf("Case #%d:", ccc);
		int xx = 0, yy = 0;
		int add = rs[n-1];
		for (int i = n-1; i >= 0; i--) {
		//	if (xx > l) { cerr<<"no answer!"<<endl; while (1>0) {}}
		//	printf(" %d %d", xx, yy);
		//	if (yy == 0) add = rs[i];
			if (yy) {
				yy += rs[i];
				if (yy > w) {
					yy = 0;
					xx += add;
					xx += rs[i];
					add = rs[i]; 
				}		
			}
			if (xx > l) { cerr<<"no answer!"<<endl; while (1>0) {}}
			ans_x[pa[i].rank] = xx;
			ans_y[pa[i].rank] = yy;
			
			yy += rs[i];
			
		}
		if (!flag) {
			FOR(i,n) swap(ans_x[i], ans_y[i]);
		}
		FOR(i,n) printf(" %d %d", ans_x[i], ans_y[i]);
		printf("\n");
	}
//	while (1>0) {}
	return 0;
} 
