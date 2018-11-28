#include<iostream>

using namespace std;

#define REP(i, n) for(int i=0;i<n;i++)

typedef unsigned long long Int;

const int N=30;

int main(){
	int t;
	cin>>t;
	REP(i, t){
		Int n, k;
		cin>>n>>k;
		cout<<"Case #"<<i+1<<": ";
		Int d=1<<n;
		if((k+1)%d==0){
			cout<<"ON"<<endl;
		}else{
			cout<<"OFF"<<endl;
		}
	}
	return 0;
}
