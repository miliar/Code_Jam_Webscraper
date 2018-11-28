#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main() {
	long long int T;
	cin>>T;
	for(long long int t=0;t<T;t++) {
		long long int ans=0;
		long long int N;
		cin>>N;
		vector<pair<long long int, long long int> > wires(N);
		for(long long int i=0;i<N;i++) {
			cin>>wires[i].first>>wires[i].second;
		}
		for(long long int i=0;i<N;i++) {
        	for(long long int j=i+1;j<N;j++) {
				//cout<<(wires[i].first-wires[j].first)*(wires[i].second-wires[j].second)<<"\n";
				if((wires[i].first-wires[j].first)*(wires[i].second-wires[j].second)<0) {
					ans++;
				}
			}
		}
		cout<<"Case #"<<t+1<<": "<<ans<<"\n";
	}
	cin>>T;
	return 0;
}
		
	
