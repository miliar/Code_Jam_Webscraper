#include <iostream>
#include <cassert>
using namespace std;

int main(int argc, char *argv[]) {
	int T, N, S, p, y, t;
	cin>>T;
	for(int x=1; x<=T; x++) {
		y=0;
		cin>>N>>S>>p;
		p*=3;
		for(int i=0; i<N; i++) {
			cin>>t;
			if(t >= p-2)
				y++;
			else if( S > 0 && t>0 && t >= p-4 ) {
				S--;
				y++;
			}
		}
		cout<<"Case #"<<x<<": "<<y<<endl;
	}
	return 0;
}

