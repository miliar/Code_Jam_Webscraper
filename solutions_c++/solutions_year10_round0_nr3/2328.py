#include<iostream>
#include<queue>
using namespace std;
int main(){
	freopen("C:/C-small-attempt2.in","r",stdin);
	freopen("C:/C-small-attempt2.out","w",stdout);
	int t,tt,r,n,k,i,g,ans;
	cin>>tt;
	for(t=1;t<=tt;t++){
		ans=0;
		queue<int> q;
		cin>>r>>k>>n;
		for(i=0;i<n;i++){
			cin>>g;
			q.push(g);
		}
		while(r--){
			int kk=0,gg;
			i=0;
			while(i<n){
				gg=q.front();
				if(kk+gg<=k){
					q.pop();
					kk+=gg;
					q.push(gg);
					i++;
				}
				else break;
			}
			ans+=kk;
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}
