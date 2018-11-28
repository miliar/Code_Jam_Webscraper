#include<iostream>
#include<cmath>
using namespace std;

int main(){
	long n,k,val,t,flag,Case=1,i;
	
	cin>>t;
	while(t--){
		cin>>n>>k;
		flag=0;
		for(i=0;i<n;i++){
			val = k/pow(2,i);
			if(val%2==0){
				flag=1;
				break;
			}	
		}
		if(flag==0)
			cout<<"Case #"<<Case++<<": "<<"ON"<<endl;
		else
			cout<<"Case #"<<Case++<<": "<<"OFF"<<endl;
	}
}
