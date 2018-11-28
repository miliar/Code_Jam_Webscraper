#include <iostream>

using namespace std;

int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int cola[1000];
	int nc;
	cin>>nc;
	for(int c=1;c<=nc;c++){
		int R,k,n,res=0;
		cin>>R>>k>>n;
		for(int i=0;i<n;i++)
			cin>>cola[i];
		int ind=0,tmpr=0,indl=0;
		for(int i=0;i<R;){
			if(tmpr+cola[ind]<=k){
				tmpr+=cola[ind];
			//	cout<<cola[ind]<<"+";
				ind=ind+1<n?ind+1:0;
				if(indl==ind){
					res+=tmpr;
					tmpr=0;
					i++;
					indl=ind;
				}
			}else{
				res+=tmpr;
			//	cout<<"="<<tmpr;
				tmpr=0;
				i++;
				indl=ind;
			}
		}
		cout<<"Case #"<<c<<": "<<res<<endl;
	}
	return 0;
}
