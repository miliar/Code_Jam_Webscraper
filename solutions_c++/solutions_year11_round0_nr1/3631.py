#include <iostream>

#define forr(i,a,b,c) for(int i = (a); i < (b); i+=(c))
#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()

using namespace std;

int positive(int a) {
	return a>0?a:-a;
}

int small(int a, int b) {
	return a<b?a:b;
}

int main (int argc, char const* argv[]) {
	
	int t, kase = 1;
	cin>>t;
	while(t--) {
		int n, o = 1, b = 1, pos[110], od[110], bd[110];
		char c[110];
		cin>>n;
		REP(i,n) cin>>c[i]>>pos[i];
		od[n] = bd[n] = -1;
		for(int i=n-1;i>=0;i--) if(c[i]=='O') od[i] = pos[i], bd[i] = bd[i+1]; else bd[i] = pos[i], od[i] = od[i+1];
		long long ans = 0, m, t3;
		REP(i,n)
			if(c[i]=='O') m = positive(od[i]-o), ans += m+1, o = od[i], t3 = small(m+1,positive(b-bd[i])), b += b<bd[i]?t3:-t3;
			else m = positive(bd[i]-b), ans += m+1, b = bd[i], t3 = small(m+1,positive(o-od[i])), o += o<od[i]?t3:-t3;
		cout<<"Case #"<<kase++<<": "<<ans<<endl;
	}
	
	return 0;
}
