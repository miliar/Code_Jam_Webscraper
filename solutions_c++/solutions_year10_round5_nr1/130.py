#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
using namespace std;
#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
#define CLR(c,n) memset(c,n,sizeof(c))
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define CONTAIN(container, it) (container.find(it)!=container.end())
#define MCPY(dest,src) memcpy(dest,src,sizeof(src))
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;
const double EPS=1e-9;
const double PI=acos(-1);
const int INF=0x3F3F3F3F;
bool p[1<<20];
int d, k, s[10], mx;
set<int> valid;
int gcd(int x, int y, LL &a, LL &b) { //ax+by=g;
	if (x==0) {
		a=0; b=1; return y;
	} else {
		int g=gcd(y%x, x, b, a);
		a-=y/x*b;
		return g;
	}
}
/*
void check(int mx) {
	if (k==1) REP(i,2) valid.insert(i);
	else if (k==2) {
	}
}
*/
void check(int p) {
	REP(i,k) if (s[i]>=p) return;
	if (k==1) {
		REP(i,2) valid.insert(i);
	} else if (k==2) {
		if (s[0]==s[1]) valid.insert(s[0]);
		else REP(i,2) valid.insert(i);
	} else { //k>=3
		int d2=(s[2]-s[1]+p)%p, d1=(s[1]-s[0]+p)%p;
		if (d1==0) {
			if (d2==0) {
				valid.insert(s[0]);
			} else return;
		} else {
			LL a, b;
			int g=gcd(d1,p,a,b); //g=a*d1+b*p;
			a=a*d2%p;
			b=(s[1]-s[0]*a%p+p)%p;
			a=a%p+p; b=b%p+p;
			//cerr << a << " " << b << " " << p << endl;
			bool v=1;
			FOR(i,2,k-1) if (s[i]!=(s[i-1]*a+b)%p) v=0;
			if (v) valid.insert((s[k-1]*a+b)%p);
		}
	}
	/*
	{
		REP(i,p) {
			int j=(s[1]-s[0]*i%p+p)%p;
			bool t=1;
			FOR(l,2,k-1) if (s[l]!=(s[l-1]*i+j)%p) {
				t=0;
				break;
			}
			if (t) {
				valid.insert((s[k-1]*i+j)%p);
//				cerr << i << " " << j << " " << (s[k-1]*i+j)%p << endl;
			}
		}
	}
	*/
}
int main(int argc, char *argv[])
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	CLR(p,true); p[0]=p[1]=false;
	FOR(i,2,1024) if (p[i]) for (int j=i*i; j<(1<<20);j+=i) p[j]=false;
	int test_case;
	scanf("%d", &test_case);
	for (int test_case_id=1; test_case_id<=test_case; ++test_case_id) {
		fprintf(stderr, "Case %d of %d\n", test_case_id, test_case);
		cin>>d>>k; REP(i,k) cin>>s[i]; mx=1; REP(i,d) mx*=10;
		valid.clear();
		REP(i,mx) if (p[i]) check(i);
		printf("Case #%d: ", test_case_id);
		if (SZ(valid)==1) printf("%d\n", *valid.begin());
		else printf("I don't know.\n");
	}
}

