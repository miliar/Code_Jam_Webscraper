#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>
#include <cctype>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
typedef long long LL;
#define PB push_back

int len, s, r, t, n, m;
typedef pair< pair<int, int>, int> P;
P a[111111];
#define st first.first
#define en first.second
#define v second

typedef pair<int, int> PII;
PII b[111111];

int main() {
int nt, tt=0; scanf("%d", &nt); while(nt--){
	scanf("%d%d%d%d%d", &len, &s, &r, &t, &n);
	FOR(i,0,n){
		scanf("%d%d%d", &a[i].st, &a[i].en, &a[i].v);
	}
	a[n].st = len; a[n].en = len; a[n].v = 0;
	n++;

	sort(a,a+n);
	int cur = 0;
	m = 0;
	FOR(i,0,n){
		if(cur < a[i].st){
			b[m++] = make_pair(s, a[i].st-cur);
		}
		cur = a[i].st;
		if(cur < a[i].en){
			b[m++] = make_pair(s+a[i].v, a[i].en-cur);
		}
		cur = a[i].en;
	}
	
	//sort(b,b+m,greater<PII>());
	sort(b,b+m);

	

	double le = t;
	double ans = 0;
	FOR(i,0,m){
		double tl = b[i].second;
		double bv = b[i].first;
		double u = min(le, tl/(bv -s+r));
		double kl = tl - u*(bv -s+r);
		ans += u + kl / bv;
		le -= u;
		//printf(" %.4f : %.4f - %.5f\n", tl, bv, u);
	}

	printf("Case #%d: %.10f\n", ++tt, ans);
}
	return 0;
}


