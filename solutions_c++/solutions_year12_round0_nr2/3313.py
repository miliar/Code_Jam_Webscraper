#include <iostream>

using namespace std;
int main()
{
	int T,tc,S,N,p,ar[101],i;
	cin>>T;
	tc=1;
	while(tc <= T){
		cin>>N>>S>>p;
		for(i=0;i<N;i++) cin>>ar[i];
		int minp,maxp;
		
		if(p < 2) minp = p;
		else minp = 3*p-4;
		
		if(p < 2) maxp = p;
		else maxp = 3*p-2;
		
		int cnt = 0;
		for(i=0;i<N;i++) {
			if( ar[i] >= maxp ) {
				cnt++;
			}
			else if( S &&  (ar[i] == (3*p-4) || ar[i] == (3*p-3) ) && ar[i])
			{
				cnt++;
				S--;
			}
		}
		cout<<"Case #"<<tc<<": "<<cnt<<"\n";
		tc++;
	}
	return 0;
}

