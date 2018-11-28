#include<iostream>
#include<vector>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int n,x;
		cin>>n;
		vector<int> s1,s2;
		for(int j=0;j<n;j++){
			cin>>x;
			s1.push_back(x);
		}
		for(int j=0;j<n;j++){
			cin>>x;
			s2.push_back(x);
		}
		sort(s1.begin(),s1.end());
		sort(s2.begin(),s2.end());
		long long ans=0;
		for(int j=0;j<n;j++){
			ans+=s1[j]*(long long)s2[n-1-j];
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
