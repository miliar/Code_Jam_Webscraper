#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

typedef __int64 ll;
int x[1000],y[1000];

int main(){
	int i,n,t,u;
	cin>>t;
	for (u=0; u<t; u++)	{
		cin>>n;
		for (i=0; i<n; i++)
			cin>>x[i];
		for (i=0; i<n; i++)
			cin>>y[i];
		sort(x,&x[n]);
		sort(y,&y[n]);
		ll sum=0;
		for (i=0; i<n; i++)
			sum+=((ll)x[i]*(ll)y[n-1-i]);
		printf("Case #%d: %I64d\n",u+1,sum);
	}
	return 0;
}