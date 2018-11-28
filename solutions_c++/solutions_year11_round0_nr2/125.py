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
char comb[50][50], opp[50][50], magic[110], tmp[50], on[110];
int c, d, n;

int read() {
	memset(comb,0,sizeof comb), memset(opp,0,sizeof opp);
	cin >> c;
	rep(i,c) {
		cin >> tmp; tmp[0] -= 'A', tmp[1] -= 'A';
		comb[tmp[0]][tmp[1]] = comb[tmp[1]][tmp[0]] = tmp[2];
	}
	cin >> d;
	rep(i,d) {
		cin >> tmp; tmp[0] -= 'A', tmp[1] -= 'A';
		opp[tmp[0]][tmp[1]] = opp[tmp[1]][tmp[0]] = 1;
	}
	cin >> n >> magic;
	rep(i,n) magic[i] -= 'A';
	return 1;
}

int caso = 1;
char pilha[110];

void process() {
	int tp = 0;
	rep(i,n) {
		pilha[tp++] = magic[i];
		loop:
		// do comb
		if(tp >= 2 && comb[pilha[tp-2]][pilha[tp-1]]) {
			pilha[tp-2] = comb[pilha[tp-2]][pilha[tp-1]] - 'A', tp--;
		}
		// do opp
		for(int j = tp-1; j >= 0; j--) if(opp[pilha[j]][pilha[tp-1]]) {
			tp = 0; break;
		}
	}
	printf("Case #%d: [",caso++);
	for(int i = 0; i < tp; i++) {
		if(i) printf(", "); printf("%c",pilha[i]+'A');
	}
	printf("]\n");
}

int main() {
	// solve
	int t; cin >> t;
	while(t-- && read()) {
		process();
	}
	return 0;
}

