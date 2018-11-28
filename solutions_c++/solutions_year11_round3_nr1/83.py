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

const int maxn = 100;
char pic[maxn][maxn];
int r, c;

bool conv(int i, int j){
	if(i+1 >= r || j+1 >= c) return false;
	if(pic[i+1][j] != '#' || pic[i][j+1] != '#' || pic[i+1][j+1] != '#') return false;
	pic[i][j] = '/';	
	pic[i+1][j] = '\\';
	pic[i][j+1] = '\\';
	pic[i+1][j+1] = '/';
	
	return true;	
}

int main(){
	int t; cin >> t;
	forn(tt, t){
		cin >> r >> c;
		forn(i, r) forn(j, c) cin >> pic[i][j];
		
		bool res = true;
		forn(i, r){
			forn(j, c){
			if(pic[i][j] == '#') if(!conv(i, j)) {res = false; break; }	
			}
			if(res == false) break;
		}	
		cout << "Case #" << tt+1 << ":" << endl;
		if(!res) cout << "Impossible" << endl;
		else{
			forn(i, r){ forn(j, c) cout << pic[i][j]; cout << endl; }
		}
	}	
	
	
	return 0;
}
