#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
#include <cstring>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define sz(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<tint> vt;
typedef vector<double> vd;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef pair<int,int> pii;

typedef long double ld;
typedef pair<ld,ld> lld;

ld X, S, R, t;
int n;
vector<lld> cor;


void init(){
	cor.clear();	
}

bool comp(const lld a, const lld b){
	return ( (a.second + R) / (a.second + S) ) > ( (b.second + R) / (b.second + S) );		
}

int main(){
	int tt; cin >> tt;
	
	forn(nc, tt){
		init();
		cin >> X >> S >> R >> t >> n;
		
		ld res = t;
		
		forn(i, n){
			ld a, b, c; cin >> a >> b >> c;
			cor.pb(mp(b - a, c));	
			X -= (b - a);
			
			res += cor[i].first / (S + cor[i].second);
		}
		cor.pb(mp(X, 0));
		res+= X / S;
		
		sort(cor.begin(), cor.end(), comp);
	
		//forn(i, n+1) cout << cor[i].first << " " << cor[i].second << endl;
		
		forn(i, n+1){
			ld tmp = t;
			if(tmp > cor[i].first / (cor[i].second + R)) tmp = cor[i].first / (cor[i].second + R);
			
			t -= tmp;
			
			res -= tmp * (cor[i].second + R) / (cor[i].second + S);
			
			if(t == 0) break;
		}
		
		res -= t;
		
		
		cout << "Case #" << nc + 1 << ": ";
		cout << setprecision(11) << res << endl;
	}

	return 0;
}	

