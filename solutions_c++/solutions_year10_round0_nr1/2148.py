#include <iostream>
#include <queue>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int t;
	long long a[100],n,k;
	a[0]=0;
	for(int i=1; i<32; i++){
		a[i]=2*a[i-1]+1;
	}
	cin>>t;
	for(int i=0; i<t; i++){
		cin>>n>>k;
		k%=a[n]+1;
		if(k!=a[n]){
			cout<<"Case #"<<i+1<<": "<<"OFF"<<endl;
		}else{
			cout<<"Case #"<<i+1<<": "<<"ON"<<endl;
		}
	}
	return 0;
}