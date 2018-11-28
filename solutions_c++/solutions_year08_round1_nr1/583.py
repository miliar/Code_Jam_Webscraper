#include<iostream>
#include<algorithm>
using namespace std;
int main(){
	long long int a[900],b[900],x,ans,i,n,t,cs=1;
	cin>>t;
	for(cs=1;cs<=t;cs++){
		cin>>n;
		for(i=0;i<n;i++){
			cin>>a[i];
		}
		for(i=0;i<n;i++){
			cin>>b[i];
		}
		sort(a,a+n);
		sort(b,b+n);
		ans=0;
		for(i=0,x=n-1;i<n;i++,x--){
			ans+=a[i]*b[x];
		}
		cout<<"Case #"<<cs<<": "<<ans<<endl;
	}
	return 0;
}

