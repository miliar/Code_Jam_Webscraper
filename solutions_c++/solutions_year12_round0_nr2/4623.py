#include<iostream>
using namespace std;

int T,N,S,P,ans;

int main() {
	cin>>T;
	for(int tc=1;tc<=T;tc++) {
		cin>>N>>S>>P;
		ans=0;
		for(int i=0;i<N;i++) {
			int temp;
			cin>>temp;
			if(temp/3>=P) ans++;
			else if(temp%3>0&&temp/3==P-1) ans++;
			else if(S>0&&((temp%3==2&&temp/3==P-2)||(temp>0&&temp%3==0&&temp/3==P-1))) {
				ans++; S--;
			}
		}
		cout<<"Case #"<<tc<<": "<<ans<<endl;
	}
}
