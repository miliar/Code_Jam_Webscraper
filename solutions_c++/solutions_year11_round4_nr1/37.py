//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <cstring>
#include <sstream>
#include <complex>
#include <vector>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define F first
#define S second

using namespace std;
typedef pair<int, int> joft;
typedef complex<double> point;

const int MAX_N = 1000 + 10;

int ord[MAX_N];
int s[MAX_N], e[MAX_N], w[MAX_N];

bool isl_w(int a, int b){
	return w[a] < w[b];
}

int main(){
	int testN;
	cin >> testN;
	FOR(test, testN){
		double t;
		long long x, sv, rv, n;
		cin >> x >> sv >> rv >> t >> n;
		FOR(i, n){
			cin>> s[i] >> e[i] >> w[i];
			ord[i] = i;
		}
		double rem = x;
		FOR(i, n){
			double len = (e[i] - s[i]);
			rem -= len;
		}
		s[n] = 0;
		e[n] = rem;
		w[n] = 0;
		ord[n] = n;
		n++;
		sort(ord, ord + n, isl_w);
		
		double ans = 0;
		FOR(j, n){
			int i = ord[j];
			double len = (e[i] - s[i]);
			double tm = len / (w[i] + rv);
			if(tm <= t){
				ans += tm;
				t -= tm;
			}else{
				len -= t * (w[i] + rv);
				ans += t;
				ans += len / (w[i] + sv);
				t = 0;
			}
			//cerr<< len << " " << ans << endl;
		}
		
		printf("Case #%d: %0.7lf\n", test + 1, ans);
	}
	return 0;
}
