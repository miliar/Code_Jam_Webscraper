#include<iostream>
using namespace std;

unsigned int T,N,impossible,mini,total,x;

int main() {
	cin>>T;
	for(int tc=1;tc<=T;tc++) {
		cin>>N;
		impossible=0;
		mini=2000000000;
		total=0;
		for(int i=0;i<N;i++) {
			cin>>x;
			total+=x;
			//cout<<"x,total: "<<x<<" "<<total<<endl;
			mini=min(mini,x);
			impossible=impossible^x;
		}
		//cout<<"total,mini: "<<total<<" "<<mini<<endl;
		cout<<"Case #"<<tc<<": ";
		if(impossible) cout<<"NO"<<endl;
		else cout<<(total-mini)<<endl;
	}
}
