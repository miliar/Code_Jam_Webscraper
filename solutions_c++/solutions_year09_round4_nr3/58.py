
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
#define FOR fup

using namespace std;
typedef long long lli;
typedef double ld;
#define maxn 105
int n, k;
int t[maxn][maxn];

// MATCHING CODE PASTED
template<int MAXN>
struct Match{//dozwolone indeksy > 0 !
int wyb[MAXN+7],n;
bool byl[MAXN+7],uz[MAXN+7];
vector<int> kraw[MAXN+7];

Match(int n):n(n+1){CLR(wyb); CLR(uz);}

void add(int a,int b){kraw[a].PB(b);}

bool go(int x){
	byl[x]=true;
	FORE(l,kraw[x]) if(wyb[*l] != x)
			if(!wyb[*l] || (!byl[wyb[*l]] && go(wyb[*l]))) {wyb[*l]=x; return true;}
	return false;
}

int match(){
	int res=0;
	bool ok;
	do{
		ok=false;
		CLR(byl);
		FOR(i,1,n) if(!uz[i] && go(i)) {uz[i]=true; ok=true; res++;}
	}while(ok);
	return res;
	}
};
bool ok(int a, int b) {
	fup(i, 1, k) {
		if (t[a][i] >= t[b][i]) return false;
	}
	return true;
}
int main(){
	int cas;
	cin >> cas;
	fup(i, 1, cas) {
		Match<102> M(102);
		cin >> n >> k;
		fup(i, 1, n) fup(j, 1, k) {
			cin >> t[i][j];
		}
		fup(i, 1, n) fup(j, 1, n) if (ok(i, j)) M.add(i, j);
		printf("Case #%d: %d\n", i, n - M.match());
	}

	return 0;	
}


