#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(v) (int(v.size()))
#define pch putchar
#define gch getchar()
#define FORD(i,a,b) for (int i=(a); i<=(b); i++)
#define FORP(i,a,b) for (int i=(a); i>=(b); i--)
#define REP(i,n) for (int i=0; i<(n); i++)
#define clean(v) memset(v,0,sizeof(v))

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

template<typename T> T sqr(const T& c) {return c*c;} 

typedef long long ll;
typedef double lf;

int x[50], v[50];
lf tme[50];
bool ok[50];

int main() {
	int tests, n, k, b, t;
	scanf("%d",&tests);
	FORD(curTest,1,tests) {
		printf("Case #%d: ",curTest);
		scanf("%d%d%d%d",&n,&k,&b,&t);
		REP(i,n) scanf("%d",&x[i]);
        REP(i,n) scanf("%d",&v[i]);
		//sort(all(ch),comp);
		int good = 0;
		REP(i,n) {
			ok[i] = (x[i]+t*v[i]>=b);
			if (ok[i]) good++;
		}
		if (good<k) {
			puts("IMPOSSIBLE");
			continue;
		}
		int ans = 0, cur_ok = 0, cur_bad = 0;
		FORP(i,n-1,0) {
			if (ok[i]) cur_ok++, ans += cur_bad;
			else cur_bad++;
			if (cur_ok==k) break;
		}
		printf("%d\n",ans);
		
	}

}
