#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
	int t,n,res,min,a;
	long sum;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>n;
		res = 0;
		sum = 0;
		min = 1000000;
		for(int j = 0;j<n;j++){
			cin>>a;
			sum+=a;
			if(a<min) { min = a;}
			res = res ^ a;
			}
		if(res == 0){
			printf("Case #%d: %d\n",i+1,(sum - min));
			}
		else{
			printf("Case #%d: NO\n",i+1);
			}
		}
	return 0;}
			
