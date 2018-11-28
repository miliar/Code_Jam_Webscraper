
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
char t[555];
int ile[555][21];
string x = " welcome to code jam";
const int mod = 10000;

int main(){
	int cas;
	cin >> cas;
	cin.getline(t + 1, 10000);
	fup(c, 1, cas) {
		cin.getline(t + 1, 10000);
		int len = strlen(t + 1);
		CLR(ile);
		ile[0][0] = 1;
		fup(i, 1, len) {
			fup(j, 0, 19) ile[i][j] += ile[i - 1][j];
			fup(j, 0, 18) if (t[i] == x[j + 1]) ile[i][j + 1] += ile[i - 1][j]; 
			fup(j, 0, 19) ile[i][j] %= mod;
		}

		printf("Case #%d: %04d\n", c, ile[len][19]);
	}
	return 0;	
}


