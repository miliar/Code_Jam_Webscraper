#include <iostream>

#define forr(i,a,b,c) for(int i = (a); i < (b); i+=(c))
#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define LL long long

using namespace std;

int n, m;
string g[55];

bool replace(int x, int y) {
	if(x==n-1||y==m-1) return 1;
	REP(i,2) REP(j,2) if(g[x+i][y+j]!='#') return 1;
	g[x][y] = g[x+1][y+1] = '/';
	g[x+1][y] = g[x][y+1] = '\\';
	return 0;
}

int main (int argc, char const* argv[]) {
	
	int t, kase = 1;
	cin>>t;
	while(t--) {
		cin>>n>>m;
		REP(i,n) cin>>g[i];
		bool ok = true;
		REP(i,n) REP(j,m) if(g[i][j]=='#') if(replace(i,j)) ok &= false;
		cout<<"Case #"<<kase++<<":"<<endl;
		if(!ok) cout<<"Impossible"<<endl;
		else REP(i,n) cout<<g[i]<<endl;
	}
	
	return 0;
}
