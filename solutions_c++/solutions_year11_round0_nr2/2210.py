#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <queue>
#include <cstring>
#include <stack>
#include <assert.h>
using namespace std;

#define IT(c) typeof((c).begin())

#define For(i, a, b) for(int (i) =  int(a); i < int(b); ++i)
#define rep(x, n) For(x,0,n)
#define foreach(i, c) for(IT(c) i = (c).begin(); i != (c).end(); ++i)

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define F first
#define S second

typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef long long ll;

int main(){
int np;cin>>np;
rep(tp,np){
	map<pair<char,char>, char> comb;
	map<char, set<char> >op;
	int n;cin>>n;
	string s;
	rep(i,n){
		cin>>s;
		comb[mp(s[0], s[1])] = s[2];
		comb[mp(s[1], s[0])] = s[2];
	}
	cin>>n;
	rep(i,n){
		cin>>s;
		op[s[0]].insert(s[1]);
		op[s[1]].insert(s[0]);
	}
	cin>>n;
	cin>>s;
	vector<char> v;
	rep(i,n){
		v.pb(s[i]);
		if(sz(v) >=2 ){
			pair<char,char> key = mp(v[sz(v)-1], v[sz(v)-2]);
			if(comb.find(key) != comb.end()){
				v.pop_back(); v.pop_back();
				v.pb(comb[key]);
			}
		}

		if(sz(v) >= 1){
			char b = v[sz(v)-1];
			bool clear=false;
			rep(k, sz(v)){
				if(op[b].count(v[k])) clear=true;
			}
			if(clear) v.clear();
		}
	}


	printf("Case #%d: [", tp+1);
	rep(i, sz(v)){
		if(i) printf(", ");
		printf("%c", v[i]);
	}
	printf("]\n");
}
}
