#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <cctype>
#include <cassert>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i = 0; i < (n); i++)
#define repr(i,b,e) for(int i = (b); i <= (e); i++)
#define INF (1001001001)
#define EPS (1e-15)

#define pr(x) do{cout << (#x) << " = " << (x) << endl;}while(0)
#define pri(x,i) do{cout << (#x) << "[" << i << "] = " << (x[i]) << endl;}while(0)
#define pra(x,n) rep(__i,n) pri(x,__i);
#define prar(x,b,e) repr(__i,b,e) pri(x,__i);

typedef long long llint;
typedef pair<int, int> pint;
typedef vector<int> vint;

int in() {
	int a;
	scanf("%d ", &a);
	return a;
}

int main() {
	int T = in();
	rep(tst, T) {
		printf("Case #%d: ", tst + 1);
		
		int C = in();
		int D = in();
		
		double anstime = 0;
		double mostright = -INF;
		rep(i, C) {
			int P = in();
			int V = in();
			llint dist = (llint)(V - 1) * D;
			double spreadtime = dist / 2.;
			
			double moretime = anstime > spreadtime ? anstime - spreadtime : 0;
			double left = P - spreadtime;
			
			if(spreadtime > anstime) {
				mostright -= spreadtime - anstime;
				anstime = spreadtime;
			}
			
			if(left < mostright) {
				left = left + moretime > mostright ? mostright : left + moretime;
			}
			else {
				left = left - moretime < mostright ? mostright : left - moretime;
			}
			
			spreadtime = anstime;
			if(left < mostright) {
				double timeneeded = (mostright - left) / 2.;
				left += timeneeded;
				spreadtime += timeneeded;
			}
			
			double right = left + dist;
			
			mostright = right + D;
			if(spreadtime > anstime) {
				anstime = spreadtime;
			}
		}
		
		printf("%.9f\n", anstime);
	}
	return 0;
}
