#include<iostream>
#include<vector>
using namespace std;
void computeinstance(int thiscase) {
	int n,ans,i,next;
	float newans;
	cin>>n;
	ans=0;
	for(i=0;i<n;i++) {
		cin>>next;
		if(next!=i+1) ans++;
	}
	newans=ans*1.0;
	cout<<"Case #"<<thiscase<<": "<<newans<<endl;
}
int main(void) {
	int t;
	cin>>t;
	for(int i=0;i<t;i++) {
		computeinstance(i+1);
	}
}
