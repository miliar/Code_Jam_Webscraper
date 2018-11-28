#include<iostream>
using namespace std;
int main(){
	int t,n,k,loop[31],count;
	loop[1]=2;
	for(int x=2;x<31;++x)
		loop[x]=loop[x-1]<<1;
	cin>>t;
	for(int tt=1;tt<=t;++tt){
		cin>>n>>k;
		if((k+1)%loop[n]==0)
			printf("Case #%d: ON\n",tt);
		else
			printf("Case #%d: OFF\n",tt);
	}

}
