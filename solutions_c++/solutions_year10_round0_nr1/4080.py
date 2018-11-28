#include <iostream>
using namespace std;

int main(){
	long long int n,k,t,i;
	cin >> t;
	for(int tn=1;tn<=t;tn++){
		cin >> n >> k;
		k += 1;
		for(i=0;i<n;i++){
			if(k%2 == 1){
				cout<<"Case #"<<tn<<": OFF"<<endl;
				break;
			}
			k /= 2;
		}
		if(i==n){
			cout<<"Case #"<<tn<<": ON"<<endl;
		}
		
	}
	
}
