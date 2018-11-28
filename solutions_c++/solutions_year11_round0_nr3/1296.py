#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int t,u,n,i,sm,mn,xr,x;
	cin>>t;
	for (u=0; u<t; u++){
		cin>>n;
		cin>>x;
		sm=xr=mn=x;
		for (i=1; i<n; i++){
			cin>>x;
			sm+=x;
			mn=min(mn,x);
			xr^=x;
		}
		if (xr==0) printf("Case #%d: %d\n",u+1,sm-mn); else printf("Case #%d: NO\n",u+1);
	}
	return 0;
}
