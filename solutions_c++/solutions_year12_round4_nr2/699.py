#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <sstream>
#include <memory>
#include <complex>
using namespace std;

static const double EPS = 1e-5;
typedef long long ll;

#define FOR(i,a,b)	for(int i=(a);i<(int)(b);++i)
#define FORe(i,a,b)	for(int i=(a);i<=(int)(b);++i)
#define REP(i,b)	FOR(i,0,b)
#define REP1(i,b)	FORe(i,1,b)
#define ALL(c)		(c).begin(),(c).end()
#define LET(v,x)	typeof(x) v = x
#define FROMTO(it,b,e)	for(LET(it,(b));it!=(e);++it)
#define FOREACH(it,c)	FROMTO(it,(c).begin(),(c).end())

ll gcd(ll a, ll b){
	if (a && b) for(ll x; b; b = x){
		x = a % b;
		a = b;
	}
	return a;
}
ll gcd(ll a[], int n){
	return n > 0 ? accumulate(a + 1, a + n, a[0], (ll(*)(ll,ll))gcd) : 0LL;
}

ll lcm(ll a, ll b){
	return (a && b) ? a / gcd(a, b) * b : 0LL;
}
ll lcm(ll a[], int n){
	return n > 0 ? accumulate(a + 1, a + n, a[0], (ll(*)(ll,ll))lcm) : 0LL;
}

#define SCAN(p,f)	scanf("%" #f " ",p)
#define GET(t,x,f)	t x;SCAN(&x,f)
#define GETi(x)		GET(int,x,d)
#define GETl(x)		GET(ll,x,lld)
#define GETc(x)		GET(char,x,c)
#define GETf(x)		GET(float,x,f)
#define GETd(x)		GET(double,x,lf)

double rr[1000];
double ans[1000][2];
int main(){
	srand((unsigned)time(NULL));
	GETi(TTT);
	REP1(ttt, TTT){
		GETi(N);
		GETi(W);
		GETi(L);
		REP(i,N){
			GETi(r);
			rr[i] = r;
		}
		int largest1 = (int)(max_element(rr, rr + N) - rr);
		rr[largest1] = -rr[largest1];
		int largest2 = (int)(max_element(rr, rr + N) - rr);
		rr[largest1] = -rr[largest1];
		
		ans[largest1][0] = 0;
		ans[largest1][1] = 0;
		ans[largest2][0] = W;
		ans[largest2][1] = L;
		while(true){
			REP(i,N){
				if(i != largest1 && i != largest2){
					ans[i][0] = round(rand() * 1000000.0 / RAND_MAX * W) / 1000000.0;
					ans[i][1] = round(rand() * 1000000.0 / RAND_MAX * L) / 1000000.0;
				}
			}
			bool fail = false;
			REP(i,N){
				FOR(j,i+1,N){
					double d = sqrt((ans[i][0]-ans[j][0])*(ans[i][0]-ans[j][0])+(ans[i][1]-ans[j][1])*(ans[i][1]-ans[j][1]));
					if(d - rr[i] - rr[j] < EPS){
						fail = true;
						break;
					}
				}
				if(fail)break;
			}
			if(!fail)break;
		}
		printf("Case #%d:", ttt);
		REP(i,N){
			printf(" %.6f %.6f", ans[i][0], ans[i][1]);
		}
		printf("\n");
	}
	return 0;
}
