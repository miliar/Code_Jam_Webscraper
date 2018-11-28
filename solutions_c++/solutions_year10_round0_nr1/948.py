#include<iostream>
using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,n,k,i,j,tt,x2[50];
	cin >> t;

	x2[0]=1;
	for(i=1 ; i<=30 ; i++){
		x2[i]=x2[i-1]<<1;
	}
	for(tt=1 ; tt<=t ; tt++){
		cin >> n >> k;
		if((k%x2[n])==x2[n]-1) cout << "Case #" << tt << ": ON" << endl;
		else cout << "Case #" << tt << ": OFF" << endl;
	}
}
