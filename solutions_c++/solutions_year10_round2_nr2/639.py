#include <iostream>
using namespace std;
int x[55],v[55],f[55];
int main(){
	freopen("c:/B-large.in","r",stdin);
	freopen("c:/B-large.out","w",stdout);
	int t,tt,n,k,b,c,r,i,j,guahu;
	cin>>tt;
	for(t=1;t<=tt;t++){
		memset(f,0,sizeof(f));
		r=0;
		cin>>n>>k>>b>>c;
		for(i=0;i<n;i++)
			cin>>x[i];
		for(i=0;i<n;i++)
			cin>>v[i];
		guahu=0;
		for(i=n-1;i>=0;i--){
			if(x[i]+v[i]*c>=b){
				f[i]=1;
				guahu++;
				for(j=i+1;j<n;j++){
					if(v[j]<v[i]&&f[j]==0) r++;
				}
			}
			if(guahu>=k) break;
		}
		cout<<"Case #"<<t<<": ";
		if(guahu<k) cout<<"IMPOSSIBLE"<<endl;
		else cout<<r<<endl;
	}
}
