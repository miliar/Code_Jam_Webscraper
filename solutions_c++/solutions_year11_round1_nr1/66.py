#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <ctime>
#include <climits>
#include <cassert>
//#pragma comment(linker, "/STACK:640000000")
#ifdef _Win32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fs first
#define sc second
#define mp make_pair
#define pb push_back
#define next ksdjgsd
#define prev lsfnasd
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pi;
const ld E=1e-8;
const int inf=(int)1e9;
ll gcd(ll a, ll b){
	if(b==0) return a;
	else return gcd(b, a%b);
}
void doit(ll &p, ll &q){
	ll d=gcd(q, p);
	p/=d;
	q/=d;
}

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int tn;
	scanf("%d", &tn);
	for(int tt=1;tt<=tn;tt++){
		ll n, p1, p2;
		scanf("%I64d%I64d%I64d", &n, &p1, &p2);
		if(p2==0 || p2==100){
			if(p1==p2) printf("Case #%d: Possible\n", tt);
			else printf("Case #%d: Broken\n", tt);
			continue;
		}
		ll q1=100, q2=100;
		doit(p1, q1);
		doit(p2, q2);
		ll d=gcd(q1, q2);
		p2*=q1/d;
		q2*=q1/d;
		/*if(p1>p2){
			ll k=(p1-1)/p2+1;
			p2*=k;
			q2*=k;
		}
		if(q1-p1>q2-p2){
			ll k=(q1-p1-1)/(q2-p2)+1;
			p2*=k;
			q2*=k;
		}  */
		if(q1<=n) printf("Case #%d: Possible\n", tt);
		else printf("Case #%d: Broken\n", tt);
	}


	return 0;
}



