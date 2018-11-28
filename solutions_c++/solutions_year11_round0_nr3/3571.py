#include <iostream>

#define forr(i,a,b,c) for(int i = (a); i < (b); i+=(c))
#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()

using namespace std;

int small(int a, int b) {
	return a<b?a:b;
}

int main (int argc, char const* argv[]) {
	
	int t, kase = 1;
	cin>>t;
	while(t--) {
		int n, a;
		cin>>n;
		int min = 1<<30, tot = 0, x = 0;
		REP(i,n) { cin>>a; x ^= a; tot += a; min = small(min,a); }
		cout<<"Case #"<<kase++<<": ";
		if(x) cout<<"NO"<<endl;
		else cout<<tot-min<<endl;
	}
	
	return 0;
}
