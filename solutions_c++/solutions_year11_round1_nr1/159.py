#include <vector> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <cassert> 
using namespace std;

#define SZ(X) ((int)(X.size()))
#define PB(X) push_back(X)
#define two(X) (1<<(X))
#define MP make_pair
#define FILL(a, b) memset(a, b, sizeof(a))
#define ALL(X) (X).begin(), (X).end()
#define IT iterator

typedef long long LL;
const double pi = acos(-1.0);

int T, pd, pg;
int tst;
LL n;

int gcd(int x, int y) {
	if(!y) return x;
	else return gcd(y,x%y);
}

int main()
{

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	cin>> T;
	while(tst < T) {
		printf("Case #%d: ", ++tst);
		cin>> n>> pd>> pg;
		int gg = gcd(pd, 100);
		int d = 100/gg;
		if(d > n) {puts("Broken");continue;}
		int lose = d-pd/gg;
		if(lose > 0 && pg == 100) {puts("Broken");continue;}
		if(d-lose>0 && pg == 0) {puts("Broken");continue;}
		puts("Possible");
	}
	
	return 0;
}
