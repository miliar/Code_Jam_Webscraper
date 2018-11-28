#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
	int T; cin>>T;
	for(int num=1;num<=T;num++){
		int n; cin>>n;
		vector<__int64> x(n),y(n);
		for(int i=0;i<n;i++){
			cin>>x[i];
		}
		for(int i=0;i<n;i++){
			cin>>y[i];
		}
		
		sort(x.begin(),x.end());
		sort(y.begin(),y.end());
		
		__int64 ans=0;
		for(int i=0;i<n;i++){
			ans+=x[i]*y[n-i-1];
		}
		
		cout<<"Case #"<<num<<": "<<ans<<endl;
	}
	
	return 0;
}
