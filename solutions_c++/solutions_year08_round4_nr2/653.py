#include<iostream>
#include<stdlib.h>

typedef long long ll;

using namespace std;

main(int argc, char **argv){
	int C;
	ll A,M,N,s,q;

	cin>> C;

	for(int c=0;c<C;c++){
		cin>>N>>M>>A;
		if(N*M<A) cout << "Case #"<<c+1<<": IMPOSSIBLE"<<endl;
		else{
			s=A/N;
			q=(s+1)*N-A;
			if(q==N) cout<<"Case #"<<c+1<<": 0 0 "<<
				N << " 0 0 " << s << endl;
			else cout<<"Case #"<<c+1<<": 0 0 "<<
				N << " 1 " << q << " " << s+1 << endl;
		}
	}
}	
