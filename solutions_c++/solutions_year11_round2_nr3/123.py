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

string toString(LL k){stringstream ss;ss << k;string res;ss >> res;return res;}
int toInt(string s){stringstream ss; ss << s; int res; ss >> res; return res;}

const int MAXN = 2001;

int n,m;

vector<PII> V;

int A[MAXN][MAXN];

set<VI> W;

VI C;

VI rs;

int res;

bool found;

void check() {
	if (found)
		return;
	FORE(it,W) {
		set<int> S;
		FORE(jt,(*it))
			S.insert(C[*jt]);
		if (S.size() < res)  
			return;
	}
	found = true;
	rs = C;
}

void walk(int step) {
	if (found)
		return;
	if (step == n + 1)
		check();
	else {
		REP(i,res) {
			C[step] = i + 1;
			walk(step + 1);
		}
	} 
}


int main() {
 	ios_base::sync_with_stdio(0);
	cout.setf(ios::fixed);
	
	int Q;
	
	cin >> Q;
	
	REP(q,Q) {
	
		cout << "Case #" << q + 1 << ": ";
		
		cin >> n >> m;
		
		V = vector<PII>(m);
		
		REP(i,m)
			cin >> V[i].ST;
			
		REP(i,m)
			cin >> V[i].ND;
			
		FOR(i,1,n) FOR(j,1,n)
			A[i][j] = 0;
			
		FOR(i,1,n - 1)
			A[i][i + 1] = A[i + 1][i] = 1;
			
		A[1][n] = A[n][1] = 1;
			
		REP(i,m)
			A[V[i].ST][V[i].ND] = A[V[i].ND][V[i].ST] = 1;
			
		VI P(n);
		
		REP(i,n)
			P[i] = i + 1;
			
		do {
		
			
			FOR(j,3,n) {
			
				bool ok = true;
				
				REP(a,j - 1)
					if (!A[P[a]][P[a + 1]])
						ok = false;
						
						
				if (!A[P[0]][P[j - 1]])
					ok = false;
					
				REP(a,j) REP(b,a - 1)
					if (a != j - 1 || b != 0)
						if (A[P[a]][P[b]]) 
							ok = false;
							
					
							
				if (ok) {
					VI H;
					REP(a,j)
						H.PB(P[a]);
					sort(ALL(H));
					W.insert(H);
				} 
			}
		} while (next_permutation(ALL(P)));
		/*FORE(it,W) {
			FORE(jt,(*it))
				cout << *jt << " " ;
			cout << endl;
		}*/
		
		C = VI(n + 1,-1);
		
		res = INF;
		
		FORE(it,W)
			res = min(res, int(it->size()));
			
		found = false;
			
		while (!found) {
			found = false;
			walk(1);
		}
		
		cout << res << endl;
		
		cout << rs[1];
		FOR(i,2,n)
			cout << " " << rs[i];
		cout << endl;
		
		W.clear();
	
	}

 	return 0;
}
