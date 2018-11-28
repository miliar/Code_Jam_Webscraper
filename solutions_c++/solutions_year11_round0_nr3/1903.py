#include <iostream>
#include <cstdio>
#include <string>
#include <stack>
#include <vector>

using namespace std;

int main () {
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=0; t<T; t++) {
		int ans=0,m=0,n=0,a=0,xor=0,sum=0;
		cin>>n;
		cin>>m;
		xor=m;
		sum=m;
		for (int i=1; i<n; i++) {
			cin>>a;
			xor^=a;
			if (a<m) m=a;
			sum+=a;
		}
		if (xor) cout<<"Case #"<<t+1<<": "<<"NO"<<endl;
		else cout<<"Case #"<<t+1<<": "<<sum-m<<endl;
	}
}