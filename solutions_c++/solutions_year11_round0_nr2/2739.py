#include<cstdio>
#include<iostream>
#include<queue>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<sstream>
#include<cmath>
#include<cctype>
#include<cassert>

using namespace std;

#define pf printf
#define sf scanf
#define VI vector<int>
#define pb push_back
#define fo(a,b) for(a=0;a<b;a++)

const int inf = 1000000000;

int base[300][300];
int oppose[300][300];

int main() {
	int t, cases;
	cin >> t;
	for( cases = 1; cases <= t; cases++ ) {
		int i, j;
		for(i='A'; i<='Z'; i++) 
			for(j='A'; j<='Z'; j++)
				base[i][j] = oppose[i][j] = 0;
		int c; cin >> c; 
		while(c--) {
			string s; cin >> s;
			char a, b; a = s[0]; b = s[1];
			base[a][b] = base[b][a] = s[2];
		}
		cin >> c;
		while(c--) {
			string s; cin >> s;
			char a, b; a = s[0]; b = s[1];
			oppose[a][b] = oppose[b][a] = 1;
		}

		int n; cin >> n; string s; cin >> s;
		vector<char> V; V.clear();
		for(i=0;i<n;i++) {
			V.pb(s[i]);
			if( V.size() >= 2 && base[ V.back() ][ V [V.size()-2]] ) {
				char c = base[ V.back() ][ V [V.size()-2]];
				V.pop_back(); V.pop_back();
				V.pb(c);
			}
			else {
				bool yes = false;
				int i;
				for(i=0;i+1<V.size();i++) if( oppose[ V[i] ][ V.back() ] ) yes = true;
				if( yes ) V.clear();
			}


		}
		pf("Case #%d: ", cases);
		pf("[");
		for(i=0;i<V.size();i++) {
			if(i) pf(", ");
			pf("%c", V[i]);
		}
		pf("]\n");
	}
	return 0;
}
