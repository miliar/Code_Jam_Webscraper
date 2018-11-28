
#include<iostream>
#include<stdio.h>
using namespace std;

int arry[1005];
int T,N;

int main(){
	freopen("C-large.in", "r", stdin);
	freopen("outlarge.txt", "w", stdout);
	int cas=0,check,sum,m;

	cin>>T;
	while(cas++<T){
		cin>>N;

		check=0; sum=0; m=10000000;
		for(int i=0; i<N; i++){
			cin>>arry[i];
			sum+=arry[i];
			check^=arry[i];
			if(m>arry[i]) m=arry[i];
		}

		cout<<"Case #"<<cas<<": ";
		if(check){
			cout<<"NO"<<endl;
		}
		else{
			cout<<sum-m<<endl;
		}
	}

	return 0;

}