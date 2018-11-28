#include<iostream>
using namespace std;

int main(){
	int T,r,n,i,x,ans;
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	for(r=1;r<=T;r++){
		cin>>n;
		ans=0;
		for(i=1;i<=n;i++){
			cin>>x;
			if(x!=i)
				ans++;
		}
		cout<<"Case #"<<r<<": "<<ans<<endl;
	}
}