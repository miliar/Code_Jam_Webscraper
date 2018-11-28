#include <stdio.h>      
#include <ctype.h>
#include <math.h>

#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <stack>
using namespace std;

#define ALL(x) x.begin(), x.end()
#define VAR(a,b) __typeof (b) a = b
#define REP(i,n) for (int _n=(n), i=0; i<_n; ++i)
#define FOR(i,a,b) for (int _b=(b), i=(a); i<=_b; ++i)
#define FORD(i,a,b) for (int _b=(b), i=(a); i>=_b; --i)
#define FORE(i,a) for (VAR(i,a.begin ()); i!=a.end (); ++i) 
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PII;
typedef double LD;

const int DBG = 0, INF = int(1e9);

const LD EPS = 1e-7;

bool isZero(LD d) {
	return d > -EPS && d < EPS;
}

string toString(LL k){stringstream ss;ss << k;string res;ss >> res;return res;}
int toInt(string s){stringstream ss; ss << s; int res; ss >> res; return res;}

int main() {
 	ios_base::sync_with_stdio(0);
	cout.setf(ios::fixed);
	
	int T;
	
	cin >> T;
	
	REP(q,T) {
	
		cout << "Case #" << q+1 << ": ";
	
		int r,c,d;
		
		cin >> r >> c >> d;
		
		int A[r][c];
		
		REP(i,r) {
			string s;
			cin >> s;
			assert(s.size() == c);
			REP(j,c) {
				string v = s.substr(j,1);
				A[i][j] = toInt(v);
			}
		}
		
		/*REP(i,r) {
			REP(j,c)
				cout << A[i][j] << " ";
			cout << endl;
		}*/
		
		int res = -1;
		
		REP(i,r) REP(j,c) FOR(k,3,min(r,c)) {
			if (k % 2 == 1) {
				if (i + k > r || j + k > c)
					continue;
				
				int cx = i + k / 2;
				int cy = j + k / 2;
				int a = 0, b = 0;
				REP(x,k) REP(y,k) {
					bool ok = true;
					if (x == 0 && y == 0)
						ok = false;
					if (x == 0 && y == k - 1)
						ok = false;
					if (x == k - 1 && y == 0)
						ok = false;
					if (x == k - 1 && y == k - 1)
						ok = false;
					if (ok) {
						a += (i + x - cx) * (d + A[i + x][j + y]);
						b += (j + y - cy) * (d + A[i + x][j + y]);
					}
				}
				if (a == 0 && b == 0)
					res = max(res, k);
				//if (i == 1 && j == 1)
				//	cout << a << " " << b << " " << k << endl;
			}
			else {
			
				if (i + k > r || j + k > c)
					continue;
				LD cx = LD(i) + (k / 2) - 0.5;
				LD cy = LD(j) + (k / 2) - 0.5;
				LD a = 0, b = 0;
				REP(x,k) REP(y,k) {
					bool ok = true;
					if (x == 0 && y == 0)
						ok = false;
					if (x == 0 && y == k - 1)
						ok = false;
					if (x == k - 1 && y == 0)
						ok = false;
					if (x == k - 1 && y == k - 1)
						ok = false;
					if (ok) {
						a += (LD(i + x) - cx) * LD(d + A[i + x][j + y]);
						b += (LD(j + y) - cy) * LD(d + A[i + x][j + y]);
					}
				}
				if (isZero(a) && isZero(b))
					res = max(res, k);
			}
		
		}
		
		if (res == -1)
			cout << "IMPOSSIBLE\n";
		else
			cout << res << endl;
			
		
		
	
	
	}

  	return 0;
}
