#include<iostream>
#include<cmath>
long long int n;
bool count_set(int k){
	int i=0;
	
	for(i=0;i<n;i++){
		if(1<<i & k);
		else break;
	}
	if(i<n)return false;
	return true;
}	
			
using namespace std;
int main(){
	long long int k,test;
	int count=1;
	cin>>test;
	while(test--){
		cin>>n>>k;
		if(count_set(k)){
			printf("Case #%d: ON\n",count);
		}
		else 
			printf("Case #%d: OFF\n",count);
		count++;
	}
	return 0;
}	