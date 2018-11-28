#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;

void fuck(){
	int n, ans=0;
	cin >> n;
	for(int i=1; i<=n; i++){
		int t;
		cin >> t;
		if(t!= i){
			ans++;
		}
	}
	cout<<ans<<".00000"<<endl;
}
int main(){
	int ncase;
	cin>>ncase;
	for(int i=0; i<ncase; i++){
		cout<<"Case #"<<i+1<<": ";
		fuck();
	}
}
