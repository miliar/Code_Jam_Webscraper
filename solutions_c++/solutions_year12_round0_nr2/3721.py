#include <iostream>

using namespace std;

int main() {
	int T;
	cin>>T;
	for(int i=1; i<=T; ++i) {
		int N, S, p, cnt=0;
		cin>>N>>S>>p;
		for(int j=0; j<N; ++j) {
			int t;
			cin>>t;
			if(p==1) cnt += (t>=1);
			else if(p==0) cnt ++;
			else {
				if((t==p-2+p-2+p||t==p-2+p-1+p)&&S>0) {
					-- S;
					++ cnt;
				} else if(t>=p-1+p-1+p) ++ cnt;
			}
		}
		cout<<"Case #"<<i<<": "<<cnt<<endl;
	}
}
