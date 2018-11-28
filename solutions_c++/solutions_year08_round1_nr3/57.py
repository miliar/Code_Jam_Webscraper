#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
using namespace std;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,n) FOR(i,0,(n)-1)
#define FS(i,v) for(__typeof((v).begin())i=(v).begin();i!=v.end();++(i))
#define ALL(a) (a).begin(),(a).end()
#define SZ(a) ((int)(a).size())
#define MK make_pair
#define FI first
#define SE second
typedef long long ll;
typedef long double ldouble;
/*long double wart = 5.236067977499789696409173668731;
ldouble modpow(ll n) {
	if(n == 1) return wart;
	ldouble tmp = modpow(n/2);
	tmp *= tmp;
	tmp = fmod(tmp, (ldouble)1000000.0);
	if(n&1) return fmod(tmp * wart, (ldouble)1000000.0);
	return tmp;
}*/
int tab[] = {0,5,27,143,751,935,607,903,991,335,47,943,471,55,447,463,991,95,607,263,151,855,527,743,351,135,407,903,791,135,647};
void lecim(int numer) {
	ll n;
	scanf("%lld",&n);
	printf("Case #%d: %03d\n", numer, tab[n]);
//	printf("Case #%d: %03d\n", numer, (int)floor(modpow(n)+1e-15));
//	printf("Case #%d: %llf\n", numer, modpow(n)+1e-15);
}
int main() {
	int t;
	scanf("%d",&t);
	REP(i,t) lecim(i+1);
	return 0;
}
