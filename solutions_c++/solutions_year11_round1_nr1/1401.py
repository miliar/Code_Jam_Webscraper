#include <iostream>
#include <cmath>

#define forr(i,a,b,c) for(int i = (a); i < (b); i+=(c))
#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define LL long long

using namespace std;

  int gcd(int a,int b)
  {
    int c;
    while(1)
    {
  	c = a%b;
  	if(c==0)
  	  return b;
  	a = b;
  	b = c;
    }
  }

int main (int argc, char const* argv[]) {
	
	LL t, kase = 1;
	cin>>t;
	while(t--) {
		LL n, pd, pg, gd, nl, nw, ntl, ntw, r;
		cin>>n>>pg>>pd;
		gd = gcd(pd,100);
		ntl = pd/gd;
		ntw = (100-pd)/gd;
		gd = gcd(pg,100);
		nl = pg/gd;
		nw = (100-pg)/gd;
		r = 1;
		if(nl&&nl<ntl) r = ceil((double)ntl/nl);
		if(nw&&nw<ntw) r = ceil((double)ntw/nw);
		ntl *= r; ntw *= r;
		cout<<"Case #"<<kase++<<": ";
		if(nl+nw>n||ntw<nw||ntl<nl) cout<<"Broken";
		else cout<<"Possible";
		cout<<endl;
	}
	
	return 0;
}
