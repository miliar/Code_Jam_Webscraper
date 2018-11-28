#pragma comment(linker, "/STACK:16777216")

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <functional>
#include <numeric>

using namespace std;

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << (int)*i << " "; cout << endl; }

typedef long long ll;

const double eps = 1e-10;
const int inf  = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3fLL;

#define fr(x,y,z) for(int(x)=(y);(x)<(z);(x)++)
#define rep(x,n) fr(x,0,n)
#define cast(x,t) *({stringstream ss;static t __ret;ss<<x,ss>>__ret;&__ret;})

#define dbg(x) cout << #x << " == " << x << endl
#define print(x) cout << x << endl

// var

int brute(int n) {
	int rmin = 10000, rmax = -10000;
	vector<int> vet;
	rep(i,n) vet.push_back(i+1);
	do {
		int now = vet[0], call = 1;
		rep(i,vet.size()) if(i) {
			rep(j,i+1) if(now % vet[j]) {
				call++;
				while(true) {
					now++;
					int ok = 1;
					rep(k,i+1) if(now % vet[k]) {ok = 0; break; }
					if(ok) {break;}
				}
				break;
			}
		}
		//if(call == 6) { dbg(call); pv(vet.begin(),vet.end()); }
		rmin = min(rmin, call);
		rmax = max(rmax, call);
	} while( next_permutation(vet.begin(),vet.end()) );
	dbg(n); dbg(rmin); dbg(rmax); dbg(rmax - rmin);
}


int is_prime(int n) {
	if(n < 2) return 0;
	if(n % 2 == 0) return n == 2;
	for(int i = 3; i*i <= n; i++) if(n % i == 0) return 0;
	return 1;
}

int N;

int read() {
	cin >> N;
	return 1;
}

void process() {
	static int caso = 1;
	printf("Case #%d:", caso++);
	int rmax = 1, rmin = (N == 1);
	for(int i = 2; i <= N; i++) if(is_prime(i)) { rmin++; for(int take = i; take <= N; take *= i) rmax++; }
	
	//dbg(rmax); dbg(rmin);
	printf(" %d\n",rmax - rmin);
}

int main() {
	// solve
	int t; scanf("%d",&t);
	while(t-- && read()) {
		process();
	}
	
	//brute(11);
	
	return 0;
}

