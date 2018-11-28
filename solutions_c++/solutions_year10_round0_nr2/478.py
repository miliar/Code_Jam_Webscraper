
#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

typedef long long ll;

ll gcd(ll a, ll b){
	if(b<a)swap(a,b);
	while(a){
		b=b%a;
		swap(a,b);
	}
	return b;
}

int main(){
	int nn;scanf("%d",&nn);
	while(nn--){
		int n;scanf("%d",&n);
		ll v[n];
		for(int i=0;i<n;i++)scanf("%lld",v+i);

		ll diff[n-1];
		for(int i=0;i<n-1;i++)diff[i]=abs(v[i]-v[i+1]);
		//for(int i=0;i<n-1;i++)cout<<diff[i]<<" n"<<n<<" "<<v[i]<<" "<<v[i+1]<<endl;

		ll gcdval=diff[0];
		for(int i=1;i<n-1;i++)gcdval=gcd(gcdval,diff[i]);

		ll maxv=0;
		for(int i=0;i<n;i++)maxv=max(maxv,v[i]);

		//cout<<"gcdval"<<gcdval<<endl;
		ll ans=(maxv+gcdval-1)/gcdval*gcdval-maxv;

		static int npr=1;
		printf("Case #%d: %lld\n",npr++,ans);
	}
	return 0;
}
