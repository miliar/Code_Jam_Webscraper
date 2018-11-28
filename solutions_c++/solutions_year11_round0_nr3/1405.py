#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>

using namespace std;

int main(){
	int T, N, C;
	cin>>T;
	for(int i=0; i<T; i++){
		cin>>N;
		int minc=10000000;
		int xord=0;
		long long sum=0;
		for(int j=0; j<N; j++){
			cin>>C;
			if(C<minc)minc=C;
			sum+=C;
			xord^=C;
		}
				
		cout<<"Case #"<<i+1<<": ";
		if(xord==0){
			cout<<(sum-minc)<<"\n";
		} else{
			cout<<"NO\n";
		}
	}
	
}
