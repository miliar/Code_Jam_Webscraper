#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
#include <string>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int (i)=(a);(i)<(b);++(i))
#define FORE(i,a,b) for (int (i)=(a);(i)<=(b);++(i))
#define FOREACH(it,v) for (typeof((v).begin()) it=(v).begin();(it)!=(v).end();++(it))
#define ALL(v) v.begin(),v.end()
#define MSET(v,x) memset((v),(x),sizeof((v)))

typedef double D;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef set<int> SI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<double> VD;
typedef map<int,int> MII;
typedef long long ll;
typedef vector<PII> VP;
typedef queue<PII> QP;

int diamond1[51][51];
int diamond2[51][51];
int diamond3[51][51];
int diamond4[51][51];

bool symmetric1(int d) {
	FOR (i,0,d) {
		FOR (j,0,d) {
			if (diamond1[i][j]!=diamond1[d-j-1][d-i-1]) return false;
		}
	}
	return true;
}

bool symmetric2(int d) {
	FOR (i,0,d) {
		FOR (j,0,d) {
			if (diamond2[i][j]!=diamond2[d-j-1][d-i-1]) return false;
		}
	}
	return true;
}

bool symmetric3(int d) {
	FOR (i,0,d) {
		FOR (j,0,d) {
			if (diamond3[i][j]!=diamond3[d-j-1][d-i-1]) return false;
		}
	}
	return true;
}

bool symmetric4(int d) {
	FOR (i,0,d) {
		FOR (j,0,d) {
			if (diamond4[i][j]!=diamond4[d-j-1][d-i-1]) return false;
		}
	}
	return true;
}

int main () {
	int T;
	cin >> T;
	FORE(t,1,T) {
		int k;
		cin >> k;
		FOR(i,0,k) {
			FORE (j,0,i) {
				cin >> diamond1[i-j][j];
			}
		}
		FOR(i,1,k) {
			FOR (j,i,k) {
				cin >> diamond1[k-j+i-1][j];
			}
		}
		FOR(i,0,k) FOR (j,0,k) {
			diamond2[i][k-j-1]=diamond1[i][j];
			diamond3[k-i-1][k-j-1]=diamond1[i][j];
			diamond4[k-i-1][j]=diamond1[i][j];
		}
		int bestsym1=0;
		int bestsym2=0;
		FORE(a,1,k) {
			if (symmetric1(a)) bestsym1=a;
			if (symmetric3(a)) bestsym1=a;
			if (symmetric2(a)) bestsym2=a;
			if (symmetric4(a)) bestsym2=a;
		}
		//cerr << bestsym1 << " " << bestsym2 << endl;
		int extra=2*k-bestsym1-bestsym2;
		cout << "Case #"<<t<<": "<< (k+extra)*(k+extra)-k*k <<endl;
	}
}
