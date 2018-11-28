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

const int maxn = 10000 + 100;
tint n, l, h;
tint freq[maxn];

bool check(tint a, int i){
	return ((a % freq[i] == 0) || (freq[i] % a == 0));	
	
}

int main(){
	int t; cin >> t;
	forn(tt, t){
		cin >> n >> l >> h;
		forn(i, n) cin >> freq[i];
		
		tint res = -1;
		
		for(tint a = l; a <=h; a++){
			bool tmp = true;
			forn(i, n) if(!check(a, i)){ tmp = false; break; }
			if(tmp) { res = a; break; }	
		}		
		cout << "Case #" << tt+1 << ": ";
		if(res == -1) cout << "NO" << endl;
		else cout << res << endl;
	}
	
	return 0;
}
