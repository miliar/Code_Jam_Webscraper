#include<iostream>
using namespace std;
int main(){
	int t,n;
	unsigned long sums,sum,min,s;
	cin>>t;
	for(int i=1;i<=t;++i){
		sum=sums=0;
		min=1000000;

		cin>>n;
		for(int x=0;x<n;++x){
			cin>>s;
			sums^=s;
			sum+=s;
			min=s<min?s:min;
		}
		if(sums)
			printf("Case #%d: NO\n",i);
		else
			printf("Case #%d: %lu\n",i,sum-min);
		
	}
}
