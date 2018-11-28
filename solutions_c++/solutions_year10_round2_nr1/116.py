#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<sstream>
#include<queue>
#include<string>
#include<cmath>

using namespace std;

#define pb push_back
#define re return
#define sf scanf
#define pf printf

int N, M;

struct node {
	string name;
	vector<node> V;
	node() {
		V.clear();
	}
};

node R;
int res;
vector<string> vs;

void grow(node &R, int d) {
	int i;
	if( d == vs.size() ) return;

	for(i=0;i<R.V.size();i++) {
		if( R.V[i].name == vs[d] ) {
		  grow(R.V[i], d+1);
		  return;
	  	}
	}
	node A; A.name = vs[d];
	R.V.pb(A);
	grow( R.V[ R.V.size() - 1], d+1);
	res++;
}

int main() {
	int t, i, j;
	int cases = 1;
	for( sf("%d", &t); t--;) {
		cin >> N >> M;
		string s;
		R.name = "pocha";
		R.V.clear();
		for(i=0; i<N; i++) {
			cin >> s;
			vs.clear();
			for(j=0;j<s.size();j++) if( s[j] == '/' ) s[j] = ' ';
			stringstream S(s);
			while( S >> s ) {
				vs.pb(s);
			}
			grow(R, 0);
		}
		res = 0;
		for(i=0;i<M;i++) {
			cin >> s;
			vs.clear();
			for(j=0;j<s.size();j++) if( s[j] == '/' ) s[j] = ' ';
			stringstream S(s);
			while( S >> s ) {
				vs.pb(s);
			}
			grow(R, 0);
		}

		pf("Case #%d: %d\n", cases++, res);
	}
	return 0;
}
