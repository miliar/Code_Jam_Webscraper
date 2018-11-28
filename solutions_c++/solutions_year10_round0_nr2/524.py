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

int x[1000];

int gcd(int a, int b) {
	return b==0?a:gcd(b,a%b);
}

int main() {
	int tests, n;
	scanf("%d",&tests);
	FORD(curTest,1,tests) {
		scanf("%d",&n);
		REP(i,n) scanf("%d",&x[i]);
		int t = abs(x[1]-x[0]);
		FORD(i,1,n-2) t = gcd(t,abs(x[i+1]-x[i]));
		int ans = t-x[0]%t; if (ans==t) ans = 0;
		printf("Case #%d: %d\n",curTest,ans);
	}
}
