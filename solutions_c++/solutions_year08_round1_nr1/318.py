#include <algorithm>
#include <bitset>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define PB push_back
#define iss istringstream
#define SZ(a) (int)a.size()
#define ALL(a) a.begin(),a.end()
#define CLEAR(a) memset(a,0,sizeof(a))
#define ll long long
#define ii pair<int,int>

int cases;
ll x[999];
ll y[999];
int n;

/*
ll prod() {
	ll ret=0;
	REP(i,n) {
		ret+=(x[i]*y[i]);
	}
	return ret;
}
*/
ll largesolve() {
	ll ret=0;
	
	REP(i,n) {
		ret+=(x[i]*y[i]);
	}
	return ret;
}

int main() {
	FILE * fin=fopen("A-large.in","r");
	FILE * fout=fopen("A-large.out","w");
	
	fscanf(fin,"%d ",&cases);
	REP(i,cases) {
		fscanf(fin,"%d ",&n);
		//ll best=(1LL<<62);
		REP(j,n) {fscanf(fin,"%lld ",&x[j]);}
		REP(j,n) {fscanf(fin,"%lld ",&y[j]);}
		sort(x,x+n);
		reverse(x,x+n);
		sort(y,y+n);
		/*do {
			best<?=prod();
		}	while (next_permutation(y,y+n));*/
		fprintf(fout,"Case #%d: %lld\n",i+1,largesolve());
	}
	

	return 0;
}
