#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define ll long long
using namespace std;
int main(){
	int N;
	cin>>N;
	for(int z=1;z<=N;z++){
		int n;
		cout<<"Case #"<<z<<": ";
		vector<ll> v1,v2;
		cin>>n;
		int temp;
		for(int i=0;i<n;i++){
			cin>>temp;
			v1.push_back(temp);		
		}
		for(int i=0;i<n;i++){
			cin>>temp;
			v2.push_back(temp);		
		}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		ll count=0;
		for(int i=0;i<n;i++){
			count+=v1[i]*v2[n-i-1];	
		}
		cout<<count<<endl;
	}
}
