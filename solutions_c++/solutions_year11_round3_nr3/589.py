#include <iostream>

#define forr(i,a,b,c) for(int i = (a); i < (b); i+=(c))
#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define LL long long

using namespace std;

int big(int a, int b) {
	return a>b?a:b;
}

int small(int a, int b) {
	return a<b?a:b;
}


int main (int argc, char const* argv[]) {
	
	LL t, kase = 1;
	cin>>t;
	while(t--) {
		LL n, l, h, a[110];
		cin>>n>>l>>h;
		REP(i,n) {
			cin>>a[i];
		}
		cout<<"Case #"<<kase++<<": ";
		bool ok;
		for(int i =l; i<=h;i++) {
			ok = true;
			REP(j,n) if(big(a[j],i)%small(a[j],i)) ok &= false;
			if(ok) { cout<<i<<endl; break; }
		}
		if(!ok) cout<<"NO"<<endl;
	}
	
	return 0;
}
