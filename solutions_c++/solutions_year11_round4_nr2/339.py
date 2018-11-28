#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <cmath>

#include <cstring>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef long long LL;
typedef stringstream SS;


#define pb(x) push_back(x)
#define ins(x) insert(x)
#define sz size()
#define len length()

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a),_d=((a)<(b))?1:-1; _d*i<=_d*(b); i+=_d)
#define FOREACH(it,s) for (typeof((s).begin()) it = (s).begin(); it != (s).end(); ++it)
#define SORT(x) (sort((x).begin(),(x).end()))
#define UNIQ(x) ((x).erase(unique((x).begin(),(x).end()),(x).end()))

#define INF 2147450751

int X, Y, D, M[500][500];


long long CX[501][501];
long long CY[501][501];
long long MASS[501][501];


void compute() {
	memset(CX, 0, sizeof(CX));
	memset(CY, 0, sizeof(CY));
	memset(MASS, 0, sizeof(MASS));	

	for(int x= 0; x < X; x++)
		for(int y = 0; y < Y; y++) {
			MASS[x+1][y+1] = MASS[x][y+1] + MASS[x+1][y] - MASS[x][y] + M[x][y];
			CX[x+1][y+1] = CX[x][y+1] + CX[x+1][y] - CX[x][y] + x*M[x][y];
			CY[x+1][y+1] = CY[x][y+1] + CY[x+1][y] - CY[x][y] + y*M[x][y];
		}
}



bool possible(int x, int y, int s) {
	long long cx = CX[x+s][y+s] - CX[x][y+s] - CX[x+s][y] + CX[x][y];
	long long cy = CY[x+s][y+s] - CY[x][y+s] - CY[x+s][y] + CY[x][y];
	long long m = MASS[x+s][y+s] - MASS[x][y+s] - MASS[x+s][y] + MASS[x][y];

	cx -= M[x][y]*x + M[x+s-1][y]*(x+s-1) + M[x][y+s-1]*x + M[x+s-1][y+s-1]*(x+s-1);
	cy -= M[x][y]*y + M[x+s-1][y]*(y) + M[x][y+s-1]*(y+s-1) + M[x+s-1][y+s-1]*(y+s-1);
	m -= M[x][y] + M[x+s-1][y] + M[x][y+s-1] + M[x+s-1][y+s-1];
//	cerr << x << " " << y << " " << s << " " << cx << " " << cy << " " << m << "|" << 2*cx << " " << (s-1)*m <<  endl;
	
	
	return (2*cx == (2*x + s-1) * m) && (2*cy == (2*y + s-1) * m);
}

int solve() {
	for(int s = min(X, Y); s >= 3; s--) 
		for(int x = 0; x <= X - s; x++)
			for(int y = 0; y <= Y - s; y++) {
	//			cerr << x << " " << y << " " << s << endl;
				if(possible(x, y, s)) return s;
			}
	return 0;
}


int main() {
/*
	for(int i = 0; i < 500; i++) {
		for(int j = 0; j < 500; j++)
			cout << rand()%9;
		cout << endl;
	}
*/

	cout.precision(16);
	int N;
	cin >> N;
	for(int i = 1; i <= N; i++) {
		cin >> Y >> X >> D;
		for(int j = 0; j < Y; j++)  {
			string S;
			cin >> S;
			for(int k = 0; k < X; k++) M[k][j] = D + S[k] - '0';
		}
		compute();
		int s = solve();
		if(s) cout << "Case #" << i << ": " << s << endl;
		else cout << "Case #" << i << ": IMPOSSIBLE" << endl;

  }
}
