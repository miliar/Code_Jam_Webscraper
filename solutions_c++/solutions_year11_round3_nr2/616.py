#include <iostream>

#define forr(i,a,b,c) for(int i = (a); i < (b); i+=(c))
#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define LL long long

using namespace std;

LL small(LL a, LL b) {
	return a<b?a:b;
}

LL pos(LL a) {
	return a>0?a:0;
}

int main (int argc, char const* argv[]) {
	
	int t, kase = 1;
	cin>>t;
	while(t--) {
		LL l, t, n, c, tot = 0, a[1010], s[1010], min;
		cin>>l>>t>>n>>c;
		REP(i,c) { cin>>a[i]; a[i] *= 2; }
		REP(i,n) s[i] = tot, tot += a[i%c];
		min = tot;
		if(l==0) {}
		else if(l==1) REP(i,n) {
			int a1=0;
			if(s[i]>=t) a1=a[i%c]/2;
			else if(s[i]+a[i%c]>=t) a1 = (a[i%c]-(t-s[i]))/2;
			min = small(min,tot-a1);
		}
		else if(l==2) REP(i,n) REP(j,n) if(i!=j) {
			int a1=0, a2=0;
			if(s[i]>=t) a1=a[i%c]/2;
			else if(s[i]+a[i%c]>=t) a1 = (a[i%c]-(t-s[i]))/2;
			if(s[j]>=t) a2=a[j%c]/2;
			else if(s[j]+a[j%c]>=t) a2 = (a[j%c]-(t-s[j]))/2;
			min = small(min,tot-a1-a2);
		}
		cout<<"Case #"<<kase++<<": "<<min<<endl;
	}
	
	return 0;
}
