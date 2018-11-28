#include <iostream>
#include <iomanip>
using namespace std;
int ps[1024];
typedef long double ld;
ld rs[1024];
int main()
{
	rs[1]=0;
	for(int i=2; i<1024; ++i) {
		ld r=1 + rs[i-1];
		for(int j=2; j<i; ++j)
			r += 1 + rs[j] + rs[i-j];
		rs[i] = r / (i-1);
	}
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		int n;cin>>n;
		for(int i=0; i<n; ++i) cin>>ps[i],--ps[i];
		ld r=0;
		bool done[1024]={};
		for(int i=0; i<n; ++i) {
			if (done[i]) continue;
			int c=i;
			int k=0;
			do {
				done[c]=1;
				c = ps[c];
				++k;
			} while(c!=i);
			if (k>1) r += 1+rs[k];
		}
		cout<<"Case #"<<a<<": "<<fixed<<setprecision(15)<<r<<'\n';
	}
}
