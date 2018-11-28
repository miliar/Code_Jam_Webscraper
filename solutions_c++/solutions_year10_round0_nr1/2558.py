#include<iostream>
using namespace std;

unsigned int ans[32];

int main(){

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int n,i=0,j;
	int N,K;

	for(j=1,ans[0]=1; j<32; j++){
		ans[j]=ans[j-1]<<1;
		//cout<<ans[j]<<endl;
	}


	cin>>n;

	while(i++<n){
		cin>>N>>K;
		cout<<"Case #"<<i<<": ";
		if(K%ans[N]==ans[N]-1) cout<<"ON"<<endl;
		else cout<<"OFF"<<endl;
	}

	return 0;
}
			