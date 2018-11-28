#include <vector>
#include <functional>
#include <algorithm>
#include <iostream>
using namespace std;

int main(int argc, char **argv) {
	int T=0;
	cin>>T;
	for (int X=1; X<=T; X++) {
		int n=0;
		cin>>n;
		vector<int> v1(n, 0);
		vector<int> v2(n, 0);
		for (int i=0; i<n; i++) {
			cin>>v1[i];
		}
		for (int i=0; i<n; i++) {
			cin>>v2[i];
		}
		sort(v1.begin(), v1.end());
//		for (int i=0; i<n; i++) {
//			cout<<v1[i]<<" ";
//		}
		sort(v2.begin(), v2.end(), greater<int>());
//		cout<<endl;
//		for (int i=0; i<n; i++) {
//			cout<<v2[i]<<" ";
//		}
//		cout<<endl;
		int SP=0;
		for(int i=0;i<n;i++){
			SP+=v1[i]*v2[i];
		}
		cout<<"Case #"<<X<<": "<<SP<<endl;
	}
	return 0;
}

