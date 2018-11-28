#include<iostream>
#include<vector>
#include<iterator>
#include<algorithm>
#include<numeric>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;++i){
		long long r,k,n;
		vector<long long> g(1,0);
		cin>>r>>k>>n;
		for(int j=0;j<n;++j){
			int temp;
			cin>>temp;
			g.push_back(temp);
		}
		copy(g.begin()+1,g.end(),back_inserter(g));
		partial_sum(g.begin(),g.end(),g.begin());
		int begin=0;
		long long sum=0;
		while(r--){
			int end=upper_bound(g.begin()+begin,g.begin()+begin+n+1,g[begin]+k)-g.begin()-1;
			sum+=g[end]-g[begin];
			begin=end%n;
		}
		cout<<"Case #"<<i<<": "<<sum<<endl;
	}
	return 0;
}
