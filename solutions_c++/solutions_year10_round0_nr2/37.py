#include<iostream>
using namespace std;

long long int T,t,N,i,panjang;
string fpb,ans;
string ar[1002];

int gcd(int a, int b) {
	if(b==0) return a;
	return gcd(b,a%b);
}

int main() {
	cin>>T;
	for(t=1;t<=T;t++) {
		cin>>N;
		panjang=0;
		for(i=0;i<N;i++) {
			cin>>ar[i];
			if(ar[i].length()>panjang) panjang=ar[i].length();
		}
		for(i=0;i<N;i++) while(ar[i].length<panjang) ar[i]="0"+ar[i];
		sort(ar,ar+N);
		fpb=ar[1]-ar[0];
		for(i=2;i<N;i++) {
			fpb=gcd(fpb,ar[i]-ar[i-1]);
		}
		ans=0;
		if(ar[0]%fpb>0) ans=(fpb-ar[0]%fpb);
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}
