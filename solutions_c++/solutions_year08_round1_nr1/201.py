#include<iostream>
using namespace std;
const int MXN=1000;
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t,T;
	cin>>t;
	for (T=1;T<=t;++T) {
		int n,i;
		long long x[MXN],y[MXN];
		cin>>n;
		for (i=0;i<n;++i) cin>>x[i];
		for (i=0;i<n;++i) cin>>y[i];
		sort(x,x+n);
		sort(y,y+n);
		reverse(y,y+n);
		long long ans=0;
		for (i=0;i<n;++i) ans+=x[i]*y[i];
		cout<<"Case #"<<T<<": "<<ans<<endl;
	}
}
