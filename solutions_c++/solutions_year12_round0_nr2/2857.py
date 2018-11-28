#include<iostream>
#include<cstdio>
using namespace std;
int main() {
	int t;
	int T;
	cin>>t;
	T=t+1;
	int data[100];
	for(;t;t--) {
		for(int a=0; a<100; a++) data[a]= 0;
		int n,s,p;
		cin>>n>>s>>p;
		
		for(int a=0; a<n; a++) {
			int t;
			cin>>t;
			data[t]++;
		}
		
		int ret = 0;
		for(int a=max(0,p*3-2); a<=30; a++) ret += data[a];
		
		int hoge = 0;
		for(int b=max(2,p*3-4); b<p*3-2; b++) hoge += data[b];
		
		ret += min(hoge,s);
		cout<<"Case #"<<T-t<<": "<<ret<<endl;
		
	}
	return 0;
	
}
