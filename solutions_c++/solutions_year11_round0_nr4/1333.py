#include<iostream>
#include<stdio.h>
#include<cmath>
using namespace std;
int main(){
	int t,n,fixed,a;
	cin>>t;
	for(int i = 0;i<t;i++){
		cin>>n;
		fixed = 0;
		for(int j = 0;j<n;j++){
			cin>>a;
			if(a == j+1) fixed++;
			}
		printf("Case #%d: %.6f\n",i+1,(float)(n-fixed));
	}
return 0;
}
		 
