#include<iostream>

using namespace std;

int main(){
	int t,n,k,x;
	//int a[];
	cin>>t;
	for(int z=1;z<=t;z++){
		cin>>n>>k;
		x=1<<n;
		if((k+1)%x==0){
			cout<<"Case #"<<z<<": ON"<<endl;
		}else{
			
			cout<<"Case #"<<z<<": OFF"<<endl;
		}
	}
	return 0;
}
