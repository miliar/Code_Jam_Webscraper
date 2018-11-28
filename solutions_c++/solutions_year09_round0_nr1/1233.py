
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set> 
#include<queue>
#include<cstring>
#include<stack>
#include<sstream>
#include<complex>
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it) 
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; }
#define fup(i,a,b) for(int i=(a);i<=(b);i++)
#define fdo(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) ((int)a.size())
#define inf 1000000000
#define SQR(a) ((a)*(a))

using namespace std;
typedef long long lli;
typedef double ld;
#define maxn 20
bool ok[20][200];
string t[5005];
vector<char> wczytaj() {
	char c; cin >> c;
	if (c == '(') {
		vector<char> odp;
		while (cin >> c) {
			if (c == ')') break;	
			else odp.PB(c);
		}
		return odp;
	} else {
		vector<char> x; x.PB(c);
		return x;
	}
}
int main(){
	int l, d, n;
	cin >> l >> d >> n;
	fup(i, 1, d) cin >> t[i];
	fup(i, 1, n) {
		CLR(ok);
		fup(j, 1, l) {
			vector<char> x = wczytaj();
			FORE(it, x) ok[j][*it] = 1;
		}
		int sum = 0;
		fup(i, 1, d) {
			bool tak = 1;
			fup(j, 0, siz(t[i]) - 1) {
				if (ok[j + 1][t[i][j]] == 0) tak = 0;
			}
			sum += tak;
		}

		printf("Case #%d: %d\n", i, sum);
	}

	return 0;	
}


