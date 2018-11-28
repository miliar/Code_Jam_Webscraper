#include<iostream>
using namespace std;
int ar[31];
int main(){
	int sum=1;
	for(int i=1; i<=30; ++i){
		ar[i]=sum;	
		sum+=ar[i]+1;
	}
	int cas,n,k;
	cin>>cas;
	for(int ca=1; ca<=cas; ++ca){
		cin>>n>>k;
		int r= k%(ar[n]+1);
		if(r==ar[n])
			printf("Case #%d: ON\n", ca);
		else
			printf("Case #%d: OFF\n", ca);
	}
}
