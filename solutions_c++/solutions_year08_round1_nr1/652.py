#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main(){
	int h;
	cin>>h;
	for(int i=0;i<h;++i){
		int n;
		cin>>n;
		vector<int>x,y;
		for(int j=0;j<n;++j){
			int temp;
			cin>>temp;
			x.push_back(temp);
		}
		for(int j=0;j<n;++j){
			int temp;
			cin>>temp;
			y.push_back(temp);
		}
		sort(x.begin(),x.end());
		sort(y.begin(),y.end());
		long long ret=0;
		for(int j=0;j<n;++j){
			ret+=x[j]*y[n-j-1];
		}
		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}
	return 0;
}