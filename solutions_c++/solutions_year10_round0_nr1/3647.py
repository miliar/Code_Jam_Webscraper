#include <iostream>
using namespace std;

long long unsigned int arr[31];

int main(){
	
	arr[0] = 1;
	
	for(long long unsigned int i=1;i<=30; i++){
		arr[i] = arr[i-1]*2;
	}
	
	long long unsigned int T,N,K;
	
	cin>>T;
	
	for(long long unsigned int i=0; i<T; i++){
		cin>>N>>K;
		
		cout<<"Case #"<<i+1<<": ";
		
		if((K+1)%arr[N]==0){
			cout<<"ON"<<endl;
		}
		else{
			cout<<"OFF"<<endl;
		}
	}
	
	return 0;
}
	
