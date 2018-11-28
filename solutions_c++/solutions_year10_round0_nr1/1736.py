#include<iostream>
#include<cmath>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int n,k;
		cin>>n>>k;
		//k++;
		cout<<"Case #"<<i<<": ";
		
		/*if((unsigned int)log2(k&-k) == n) cout<<"ON\n";
		else cout<<"OFF\n";*/
		k=k%(1<<n);
		/*int c=0;
		while(k){
		k=k&(k-1);
		c++;
		}*/
		if(k == (1<<n) - 1)
			cout<<"ON\n";
		else cout<<"OFF\n";
		
	}

}
