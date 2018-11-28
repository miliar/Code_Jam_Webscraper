#include<iostream>
using namespace std;
int main(){
	int t,n,m;
	long long unsigned L,P,C;
	int table[1000];
	int ansx[32]={0,1,2,2,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5};
	int ans,count;
	cin>>t;
	for(int tt=1;tt<=t;++tt){
		cin>>L>>P>>C;
		count=0;
		ans=0;
		while((L*=C)<P)
			count++;
		printf("Case #%d: %d\n",tt,ansx[count]);
	}
	
}
