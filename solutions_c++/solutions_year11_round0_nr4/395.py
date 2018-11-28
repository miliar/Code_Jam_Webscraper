#include <iostream>
#include <cmath>
using namespace std;

int main(){
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int T,N;
	cin>>T;

	for(int t = 0; t < T; ++ t)
	{
		cin>>N;
		int ndata[1000];
		int res = N;
		for(int n = 0; n < N; ++ n)
		{
			cin>>ndata[n];
			if (ndata[n] - 1 == n) -- res;
		}

		cout<<"Case #"<<t+1<<": "<<res<<".000000"<<endl;
	}
	return 0;
}