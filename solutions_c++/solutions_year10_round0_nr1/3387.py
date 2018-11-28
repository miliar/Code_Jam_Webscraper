#include<iostream>
#include<math.h>
#include<stdio.h>
using namespace std;
int check(unsigned int d, unsigned int K){
	while(K>d)
			K=K-d-1;
	if(d==K)
			return 1;
	else
			return 0;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Output.txt","w",stdout);
	unsigned int T,N,K;
	cin>>T;
	for(int i=1;i<=T;i++){
		cin>>N>>K;
		unsigned int d=(int)(pow(2,N)-1);
		if( check(d,K) )
				cout<<"Case #"<<i<<": ON\n";
		else
			cout<<"Case #"<<i<<": OFF\n";
	}
	return 0;
}
