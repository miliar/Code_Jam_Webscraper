#include <algorithm>
#include <iostream>
#include <iomanip>
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

const int maxn = 100 + 50;

map<int, int> isop[maxn];
long double wp[maxn], owp[maxn], oowp[maxn], nop[maxn];
int n;

void init(){
	forn(i, maxn){
		isop[i].clear();
		wp[i] = owp[i] = oowp[i] = 0;	
		nop[i] = 0;
	}
}

long double calc(int a, int b){
	if(isop[a].find(b) == isop[a].end()) return 0;
	
	long double res = 0, tmp = 0;

	forn(k, n){
		if(k == a || isop[b].find(k) == isop[b].end()) continue;	
		tmp ++;
		res += isop[b][k];
	}	
	res = res / tmp;

	return res;
}

int main(){
	int t; cin >> t;
	forn(tt, t){
		init();
		
		cin >> n;
		forn(i, n) forn(j, n){
			char c; cin >> c;		
			if(c == '1') { isop[i][j] = 1; wp[i]++; nop[i]++; }
			else if(c == '0') { isop[i][j] = 0; nop[i]++; }
		}
		
		forn(i, n){
			wp[i] /= nop[i];
			forn(j, n) owp[i] += calc(i, j);
			owp[i] /= nop[i];			
		}
		
		forn(i, n){
			forn(j, n) if(isop[i].find(j) != isop[i].end()) oowp[i] += owp[j];
			oowp[i] /= nop[i];	
		}
		cout << "Case #" << tt+1 << ": " << endl;
		forn(i, n){
			//cout << wp[i] << " " << owp[i] << " " << oowp[i] << " ";
			long double ea = 4; wp[i] /= ea; oowp[i] /= ea;
			ea = 2; owp[i] /= ea;
			cout << setprecision(11) << wp[i] + owp[i] + oowp[i] << endl; 	
		}
		
	}	

	return 0;	
}
