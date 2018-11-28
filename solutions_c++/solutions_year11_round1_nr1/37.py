#include <iostream>
using namespace std;
typedef long long ll;
ll gcd(ll a,ll b){
	return a==0?b:gcd(b%a,a);
}
int main(){
	int tnum,tcou=0;cin>>tnum;
	while (tnum--){
		ll n,pD,pG;
		cin>>n>>pD>>pG;
		bool can=true;
		if (pG==0 || pG==100){
			can=(pG==pD);
		}
		else{
			can=((100/gcd(pD,100))<=n);
		}
		cout<<"Case #"<<++tcou<<": ";
		if (can)
			cout<<"Possible"<<endl;
		else
			cout<<"Broken"<<endl;
	}
	return 0;
}
