/*
Author : Prem Kumar
language : C++
*/
#include<iostream>
#include<math.h>
using namespace std;

int toggle(int a[],int i){
	if(a[i]==1)
		return 0;
	else
		return 1;	
}

int main(){
	unsigned int T,N,K;
	cin>>T;
int ind =1;

while(ind<=T){
	cin>>N>>K;
	
	unsigned int ans=0;
	double ans1 = (K+1.0)*1.0/pow(2,N);
	ans = ans1;
	double temp;
	temp = ans;

	if(temp==ans1)
	cout<<"Case #"<<ind<<": ON\n";
	else
	cout<<"Case #"<<ind<<": OFF\n";
ind++;
}

return 0;
}
