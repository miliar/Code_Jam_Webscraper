#include<iostream>
#include<cstdio>
using namespace std;

int calc(int A,int n,int B) {
	int p = n;
	
	int r = 1;
	while(r<B) r*=10;
	r/=10;
	
	int ret = 0;
	while(1) {
		 
//		cout<<p<<endl;
		p = p/10 + (p%10)*r;
		if(n<p && p<=B) ret++;
		
		if(n==p) break;
	}
	
	return ret;
	
}


int main() {
	int T,t;
	cin>>t;
	T = t+1;
	for(;t;t--) {
		
		int ret = 0;
		
		int A,B;
		cin>>A>>B;
		for(int n=A; n<B; n++) ret += calc(A,n,B);
		
		
		cout<<"Case #"<<T-t<<": "<<ret<<endl;
	}
	return 0;
}


