#include<iostream>
#include<vector>
using namespace std;
void candy(int cases);
int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
		candy(i);
	}
}

void candy(int cases) {
	int n;
	int min=10000000;
	int sum=0;
	int x=0;
	cin >>n;
	for(int i=0;i<n;i++) {
		int temp;
		cin>>temp;
		if(temp<min) {
			min = temp;
		}
		sum+=temp;
		x^=temp;
	}
	cout<<"Case #"<<cases<<": ";
	if(x!=0) {
		//impossible
		cout<<"NO"<<endl;
	}else {
		cout<<sum-min<<endl;
	}

}
