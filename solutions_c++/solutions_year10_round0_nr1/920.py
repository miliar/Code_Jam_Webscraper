#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define SETMIN(a,b) a = min(a,b)
#define SETMAX(a,b) a = max(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define BEND(v) v.begin(),v.end()
#define MP make_pair
#define A first
#define B second

typedef unsigned long long int ull;
typedef long double ld;

int main() {
	freopen ("snapper.in","r",stdin);
	freopen ("snapper.out","w",stdout);
	//freopen ("junk","w",stderr);
	int T;
	cin >> T;
	FOR(t,T) {
		int N,K;
		cin >> N >> K;
		int state[30];
		int power[30];
		CLR(state,0);
		CLR(power,0);
		FOR(k,K) {
			power[0] = 1;

			FOR(i,N) {
				if (power[i]) state[i] ^= 1;
			}

			FR(i,1,N) {
				power[i] = power[i-1] && state[i-1];
			}

			/*
			cerr << "P: ";
			FOR(i,N) cerr << power[i] << " ";
			cerr << endl << "S: ";
			FOR(i,N) cerr << state[i] << " ";
			cerr << endl << endl;
			*/
		}
		if (power[N-1] && state[N-1]) printf("Case #%d: ON\n", t+1);
		else printf("Case #%d: OFF\n", t+1);
	}
	return 0;
}
