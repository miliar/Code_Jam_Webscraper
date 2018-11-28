#include<iostream>
#include<vector>

using namespace std;


int fin( long long l, long long p, int C){
	long long num=1;
	int res=0;

	while( l*num<p) { num*=C; res++;}
	return res;
}

int main(){

	int numcases;
	cin>>numcases;
	for (int c=1; c<=numcases; c++){
		cout<<"Case #"<<c<<": ";

		long long l, p;
		int C;

		cin>>l>>p>>C;

		int N=fin(l,p,C);
		long long ans=fin(1,N,2);

		cout<<ans<<endl;

	}
	return 0;
}
