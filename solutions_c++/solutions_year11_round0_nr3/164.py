#include<iostream>
#include<vector>
using namespace std;
void computeinstance(int thiscase) {
	long long n,ci,i,b,imin,sum;
	cin>>n;
	sum=0;
	imin=-1;
	b=0;
	for(i=0;i<n;i++) {
		cin>>ci;
		sum=sum+ci;
		if(imin==-1||imin>ci) imin=ci;
		b=b^ci;
	}
	if(b!=0)
		cout<<"Case #"<<thiscase<<": NO"<<endl;
	else {
		cout<<"Case #"<<thiscase<<": "<<sum-imin<<endl;
	}
}
int main(void) {
	int t;
	cin>>t;
	for(int i=0;i<t;i++) {
		computeinstance(i+1);
	}
}
