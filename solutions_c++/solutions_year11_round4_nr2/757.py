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

const int maxr = 600;

int mat[maxr][maxr];
int r, c, d;

bool check(int a, int b, int k){
	if( ((a + k) > r) || ((b + k) > c) ) return false;
	
	//cout << a << " " << b << " " << k << endl;
	
	int r1 = 0, r2 = 0;
	int coef = 0;
	forsn(i, a, a+k){
		forsn(j, b, b+k){
			if( (i==a && j==b) || (i==a && j == b+k-1) || (i==a+k-1 && j==b) || (i==a+k-1&&j==b+k-1)) continue;
			r1 += (2*i-2*a - k + 1) * (d + mat[i][j]);
			r2 += (2*j-2*b - k + 1) * (d + mat[i][j]);
			
			coef += mat[i][j];
		}	
	}
	
	//if((a * coef == r1 * 2) && (b * coef == r2 * 2)) return true;
	if(r1 == 0 && r2 == 0) return true;
	else return false;
	
}


int main(){
	int tt;
	cin >> tt;
	
	forn(nc, tt){
		cin >> r >> c >> d;
		
		forn(i, r) forn(j, c){ char c; cin >> c; mat[i][j] = int(c - '0'); }
		
		int res = -1;
		
		forsn(k, 3, min(r, c)+1){
			forn(i, r){
				forn(j, c){
					if(check(i, j, k)) res = k;
				}
			}
		}
		//cout << r << " " << c << endl;
		
		cout << "Case #" << nc + 1 << ": ";
		if(res == -1) cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;
	}
	
	return 0;
}
