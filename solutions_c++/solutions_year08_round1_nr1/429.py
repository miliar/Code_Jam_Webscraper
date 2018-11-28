#include<iostream>
#include<stdio.h>
using namespace std;

long long int n,i,ar1[1000],ar2[1000],x,tc,prod;

int main() {
	freopen("prod.out","w",stdout);
	cin>>tc;
	for(x=1;x<=tc;x++) {
		cin>>n;
		cout<<"Case #"<<x<<": ";
		for(i=0;i<n;i++) cin>>ar1[i];
		for(i=0;i<n;i++) {
			cin>>ar2[i];
			ar2[i]=-ar2[i];
		}
		sort(ar1,ar1+n);
		sort(ar2,ar2+n);
		prod=0;
		for(i=0;i<n;i++) prod+=(-ar2[i]*ar1[i]);
		cout<<prod<<endl;
	}
	fclose(stdout);
}

