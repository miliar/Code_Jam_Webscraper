#include<iostream>
using namespace std;

int T,N,L,H,i;
bool valid;
int note[1000];

int main() {
	cin>>T;
	for(int tc=1;tc<=T;tc++) {
		cin>>N>>L>>H;
		for(i=0;i<N;i++) cin>>note[i];
		for(i=L;i<=H;i++) {
			valid=true;
			for(int j=0;j<N;j++) {
				if(!valid) break;
				if((note[j]%i)&&(i%note[j])) valid=false;
			}
			if(valid) break;
		}
		cout<<"Case #"<<tc<<": ";
		if(valid) cout<<i<<endl;
		else cout<<"NO"<<endl;
	}
}
