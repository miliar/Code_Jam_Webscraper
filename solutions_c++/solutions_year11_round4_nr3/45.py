#include <iostream>
using namespace std;

typedef long long ll;
#define int ll
ll primes[1<<20];
int P;
bool nonp[1<<20];
int calc(int n) {
	if (n==1) return 0;
	int r=1;
	for(int i=0; primes[i]*primes[i]<=n; ++i) {
		int p = primes[i];
//		cout<<"asd "<<p<<'\n';
		int k=p;
		while((k *= p) <= n) {
			++r;
//			cout<<"adding @ "<<k<<'\n';
		}
	}
	return r;
}

main()
{
	nonp[0]=nonp[1]=0;
	for(int i=2; i<1<<10; ++i) {
		if (nonp[i]) continue;
		for(int j=i*i; j<1<<20; j+=i) {
			nonp[j]=1;
		}
	}
	for(int i=2; i<1<<20; ++i) if (!nonp[i]) primes[P++]=i;

	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		int n;cin>>n;
//		cout<<"Case #"<<a<<": "<<big(n)-small(n)<<'\n';
		cout<<"Case #"<<a<<": "<<calc(n)<<'\n';
	}
}
