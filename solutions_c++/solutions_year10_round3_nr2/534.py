using namespace std;

#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>
#define FOR(i,a,n) for(int i=a; i<n; i++)
#define REP(i,n) FOR(i,0,n)
#define MAX 1000
#define GI ({int _; scanf("%d", &_);_;})
#define INF (LL)1e18
#define sz size()
#define pb push_back
#define mkp make_pair
#define eps 1e-15
#define DINF 1e100
typedef long long LL;
typedef vector<int> VI;

int k, mem[1002][1002];
int go(int a, int b) {
	if(a * k >= b) return 0;
	if(mem[a][b] != -1) return mem[a][b];
	int ret = b-a, fnd, last;
VI v;
for( int p=a;  p< b; p*=k) {
    for(int i = 0; i <= 1; i++) v.pb(p+i);
}
for( int p=b;  p>a; p/=k) for(int i = 0; i <= 1; i++) v.pb(p+i);

    REP(j,v.sz) { 
    	int i = v[j];
	    if(a >= i || b <= i) continue;
		int g1 = go(a,i), g2 = go(i,b), g = max(g1,g2) + 1;
		if(ret > g) {
			ret = g, fnd = i;		
		}
        if(ret == g) last = i;
	}
	if(0 || a == 63 && b == 1000) {
//	cout << a << " "<< b << ", "<<fnd <<" to " << last <<" -> "<<ret << endl;
    }
	return mem[a][b] = ret;

}
int main() {
	LL kases = GI+1;	
	FOR(kase, 1, kases) {
		int a = GI, b = GI;
		 k = GI;
		 memset(mem,-1,sizeof(mem));
//		cout << go(a,b) << endl;
		printf("Case #%d: %d\n", kase, go(a,b));		
		continue;
		int c=0;
		while(1) {
			int mid, cur = b;
			if(cur%k == 0) cur /= k;
			else cur = cur/k + 1;
			if(cur <= a) break;
			b = cur;
			c++;
cout << b <<  " ";
		}

		printf("Case #%d: %d\n", kase, c);
	}
}
