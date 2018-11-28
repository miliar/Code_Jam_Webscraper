#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<pii> vpii;
typedef vector<vector<pii> > vvpii;

#define DEBUG 0
#define forn(i, n) for(int i = 0; i < n; i++)
#define fors(i, c) for(int i = 0; i < (c).size(); i++)
#define fab(i,a,b) for(int i = a; (a<=b&&i<b) || (a>b&&i>=b); (a<=b)?i++:i--)
#define tr(i, c) for((typeof (c).begin()) i = (c).begin(); i != (c).end(); i++)
#define all(c) (c).begin(), (c).end()

int mem[16][2048];
int P;
int M[1024];
int L[1024];

int costo(int n){
	return L[n];
}

int rec(int resta, int m){
	if (m >= 1<<P){
		if(DEBUG) cout << "Estoy en el hijo " << m-(1<<P) << ", resta = " << resta << endl;
		return (M[m-(1<<P)] >= P-resta)?0:-1;
	}
	if (DEBUG) cout << "Estoy en el partido " << m << endl;
	if (mem[resta][m] != -1) return mem[resta][m];
	
	if (rec(resta, m*2) == -1 || rec(resta, m*2+1) == -1){
		if (rec(resta+1, m*2) == -1 || rec(resta+1, m*2+1) == -1)
			return mem[resta][m] = -1;
		return mem[resta][m] = costo(m)+rec(resta+1, m*2)+rec(resta+1, m*2+1);
	}
	int pago = min(costo(m)+rec(resta+1, m*2)+rec(resta+1, m*2+1), rec(resta, m*2)+rec(resta, m*2+1));
	
	if (DEBUG) cout << "Si voy, cuesta " << costo(m) << " más " << rec(resta+1, m*2) << " más " << rec(resta+1, m*2+1) << endl;
	if (DEBUG) cout << "Si no voy cuesta " << rec(resta, m*2) << " más " << rec(resta, m*2+1) << endl;
	
	return mem[resta][m] = pago;
}


int main(){
	int C;
	cin >> C;
	forn(cc, C){
		cin >> P;
		memset(M, 0, 1024);
		memset(mem, -1, sizeof(mem));
		memset(L, 0, sizeof(L));
		for(int i = 0; i < 1<<P; i++)
			cin >> M[i];
		vvi C(P);
		for(int i = 0; i < P; i++){
			for(int j = 0; j < 1<<(P-i-1); j++){
				int a;
				cin >> a;
				C[P-i-1].push_back(a);
			}
		}
		int k = 1;
		forn(i, P){
			forn(j, C[i].size())
				L[k++] = C[i][j];
		}
		if (DEBUG) forn(i, k) cout << L[i] << ' ';
		
		cout << "Case #" << cc+1 << ": " << rec(0, 1) << endl;
	}
}