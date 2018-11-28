#include<iostream>
#include<cmath>
#include<string>
using namespace std;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
//	freopen("1.txt","r",stdin);
	int T,N;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		cin>>N;
		int sum1 = 0, sum2 = 0;
		int minv = 10000000, v;
		for(int i=0;i<N;i++)
		{
			cin>>v;
			minv = min(minv,v);
			sum1 += v;
			sum2 ^= v;;
		}

		cout<<"Case #"<<cas<<": ";
		if(sum2 != 0) cout<<"NO\n";
		else cout<<sum1-minv<<"\n";		
	}
	return 0;
}