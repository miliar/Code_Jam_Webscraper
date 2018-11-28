#include <iostream>
#include <stdio.h>
using namespace std;

int pow2[31];
void precalc() {
	pow2[0]=1;
	for(int i=1; i<=30; i++ ) {
		pow2[i] = pow2[i-1]*2;
	}
}
int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	precalc();
	int t,n,k;

	cin>>t;
	for( int i=0; i<t; i++ ) {
		cin>>n>>k;

		cout<<"Case #"<<i+1<<": ";
		if( (k+1)%(pow2[n]) == 0 ) {
			cout<<"ON";
		}
		else {
			cout<<"OFF";
		}
		cout<<endl;

	}

	return 0;
}