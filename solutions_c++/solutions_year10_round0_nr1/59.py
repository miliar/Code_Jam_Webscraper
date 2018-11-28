#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
typedef long long ll;

int main(){
	int t; cin>>t;
	for(int tt=1;tt<=t;tt++){
		ll n,k;
		scanf("%lld %lld",&n,&k);
		cout<<"Case #"<<tt<<": ";
		if((k+1)%(1LL<<n)==0) cout<<"ON"<<endl;
		else cout<<"OFF"<<endl;
	}
}
